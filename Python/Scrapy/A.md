# Scrapy

## 追踪链接两种方式：

```
import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/",
    ]
    def parse(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(response.url, href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)
    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item

 # second
def parse_articles_follow_next_page(self, response):
    for article in response.xpath("//article"):
        item = ArticleItem()

        ... extract article data here

        yield item

    next_page = response.css("ul.navigation > li.next-page > a::attr('href')")
    if next_page:
        url = response.urljoin(next_page[0].extract())
        yield scrapy.Request(url, self.parse_articles_follow_next_page)
```

## Scrapy Tools
全局命令:
* startproject
* settings
* runspider
* shell
* fetch
* view
* version

项目(Project-only)命令:
* crawl
* check
* list
* edit
* parse
* genspider
* bench

## Spider, CrawlSpider
爬取规则(Crawling rules)
```
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']

    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)

        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item
```
## 选择器(Selectors)
response.selector.(xpath, css, re).(extract, extract_first, re_first)
## Scrapy Items
```
import scrapy
class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
```
```
 # 爬取不同页面的item
def parse_page1(self, response):
    item = MyItem()
    item['main_url'] = response.url
    request = scrapy.Request("http://www.example.com/some_page.html",
                             callback=self.parse_page2)
    request.meta['item'] = item
    return request

def parse_page2(self, response):
    item = response.meta['item']
    item['other_url'] = response.url
    return item
```
## Item Loaders
Item Loaders 被设计用来提供一个既弹性又高效简便的构件， 以扩展或重写爬虫或源格式(HTML, XML之类的)等区域的解析规则， 这将不再是后期维护的噩梦。
```
from scrapy.loader import ItemLoader
from myproject.items import Product

def parse(self, response):
    l = ItemLoader(item=Product(), response=response)
    l.add_xpath('name', '//div[@class="product_name"]')
    l.add_xpath('name', '//div[@class="product_title"]')
    l.add_xpath('price', '//p[@id="price"]')
    l.add_css('stock', 'p#stock]')
    l.add_value('last_updated', 'today') # you can also use literal values
    return l.load_item()
```
## Item Pipeline, Feed Exports
```
from scrapy.exceptions import DropItem

class PricePipeline(object):

    vat_factor = 1.15

    def process_item(self, item, spider):
        if item['price']:
            if item['price_excludes_vat']:
                item['price'] = item['price'] * self.vat_factor
            return item
        else:
            raise DropItem("Missing price in %s" % item)
```

## 使用 trackref 调试内存泄露
prefs()
```
class object_ref(object):
    """Inherit from this class (instead of object) to a keep a record of live
    instances"""

    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        live_refs[cls][obj] = time()
        return obj
        
class Request(object_ref):
class Response(object_ref)
class Spider(object_ref):
class BaseItem(object_ref):
class Selector(_ParselSelector, object_ref)
```

sudo pip install guppy

## 部署 Scrapyd, Scrapy cloud 
## 中间件（下载中间件， Spider中间件）


# Scrapy core

based on [Twisted](http://www.ituring.com.cn/book/miniarticle/7467)(Twisted是用Python实现的基于事件驱动的网络引擎框架) ex:tornado, gevent

# code
```
def create_deprecated_class(name, new_class, clsdict=None,
                            warn_category=ScrapyDeprecationWarning,
                            warn_once=True,
                            old_class_path=None,
                            new_class_path=None,
                            subclass_warn_message="{cls} inherits from "\
                                    "deprecated class {old}, please inherit "\
                                    "from {new}.",
                            instance_warn_message="{cls} is deprecated, "\
                                    "instantiate {new} instead."):
    """
    Return a "deprecated" class that causes its subclasses to issue a warning.
    Subclasses of ``new_class`` are considered subclasses of this class.
    It also warns when the deprecated class is instantiated, but do not when
    its subclasses are instantiated.

    It can be used to rename a base class in a library. For example, if we
    have

        class OldName(SomeClass):
            # ...

    and we want to rename it to NewName, we can do the following::

        class NewName(SomeClass):
            # ...

        OldName = create_deprecated_class('OldName', NewName)

    Then, if user class inherits from OldName, warning is issued. Also, if
    some code uses ``issubclass(sub, OldName)`` or ``isinstance(sub(), OldName)``
    checks they'll still return True if sub is a subclass of NewName instead of
    OldName.
    """

    class DeprecatedClass(new_class.__class__):

        deprecated_class = None
        warned_on_subclass = False

        def __new__(metacls, name, bases, clsdict_):
            cls = super(DeprecatedClass, metacls).__new__(metacls, name, bases, clsdict_)
            if metacls.deprecated_class is None:
                metacls.deprecated_class = cls
            return cls

        def __init__(cls, name, bases, clsdict_):
            meta = cls.__class__
            old = meta.deprecated_class
            if old in bases and not (warn_once and meta.warned_on_subclass):
                meta.warned_on_subclass = True
                msg = subclass_warn_message.format(cls=_clspath(cls),
                                                   old=_clspath(old, old_class_path),
                                                   new=_clspath(new_class, new_class_path))
                if warn_once:
                    msg += ' (warning only on first subclass, there may be others)'
                warnings.warn(msg, warn_category, stacklevel=2)
            super(DeprecatedClass, cls).__init__(name, bases, clsdict_)

        # see http://www.python.org/dev/peps/pep-3119/#overloading-isinstance-and-issubclass
        # and http://docs.python.org/2/reference/datamodel.html#customizing-instance-and-subclass-checks
        # for implementation details
        def __instancecheck__(cls, inst):
            return any(cls.__subclasscheck__(c)
                       for c in {type(inst), inst.__class__})

        def __subclasscheck__(cls, sub):
            if cls is not DeprecatedClass.deprecated_class:
                # we should do the magic only if second `issubclass` argument
                # is the deprecated class itself - subclasses of the
                # deprecated class should not use custom `__subclasscheck__`
                # method.
                return super(DeprecatedClass, cls).__subclasscheck__(sub)

            if not inspect.isclass(sub):
                raise TypeError("issubclass() arg 1 must be a class")

            mro = getattr(sub, '__mro__', ())
            return any(c in {cls, new_class} for c in mro)

        def __call__(cls, *args, **kwargs):
            old = DeprecatedClass.deprecated_class
            if cls is old:
                msg = instance_warn_message.format(cls=_clspath(cls, old_class_path),
                                                   new=_clspath(new_class, new_class_path))
                warnings.warn(msg, warn_category, stacklevel=2)
            return super(DeprecatedClass, cls).__call__(*args, **kwargs)

    deprecated_cls = DeprecatedClass(name, (new_class,), clsdict or {})

    try:
        frm = inspect.stack()[1]
        parent_module = inspect.getmodule(frm[0])
        if parent_module is not None:
            deprecated_cls.__module__ = parent_module.__name__
    except Exception as e:
        # Sometimes inspect.stack() fails (e.g. when the first import of
        # deprecated class is in jinja2 template). __module__ attribute is not
        # important enough to raise an exception as users may be unable
        # to fix inspect.stack() errors.
        warnings.warn("Error detecting parent module: %r" % e)

    return deprecated_cls
```