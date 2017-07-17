## scrapy-redis 源码笔记
scrapy-redis 做的事情就是在任务记录在redis里准备好后(准备阶段;需要按照格式)，调用scrapy来进行后续，准备阶段的事需要自己来处理。
简单地把redis和scrapy结合一下。

```
from scrapy_redis.spiders import RedisSpider

class MySpider(RedisSpider):
    name = 'myspider'
    def parse(self, response):
        pass
```
作者重写了Spider部分代码，添加redis的相关操作。使用redis来控制crawler 和 urls。
最重要的代码在/scrapy-redis/src/scrapy_redis/spiders.py:
```
class RedisSpider(RedisMixin, Spider):
class RedisCrawlSpider(RedisMixin, CrawlSpider):
Mixin 继承。重写的部分 from_crawler，都是进行redis初始化。

class RedisMixin(object)：
比较重要的部分：
def setup_redis(),上面两个类用到的redis初始化。
def next_requests()： 从redis读取一条记录(调用redis的spop或lpop)，调用scrapy的make_requests_from_url解析。
def schedule_next_requests(self)：
def spider_idle(self)：这两个函数调用scrapy来进行crawler的后续处理(解析url，拿到数据后)
```