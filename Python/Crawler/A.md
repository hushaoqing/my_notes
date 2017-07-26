爬取头条视频存在的问题:获取数据重复量太高,大多是在浪费时间.
观察翻页链接之后,发现可以模拟浏览器的行为,如果翻页失败,就刷新当前页.
对应于爬虫就是回去不到下页url就sleep(2),然后重新访问上条url,这样头条会重新给你推送新的url.
这种方案适合头条这种推荐机制(可以不停刷新).

```
def get_urls(self, url, maxNum):
    if not url:return []
    # list_data = []
    resp = UrlUtils(self.taskData.taskId).getPageResponse(url, interval = 3)
    tt_webid = '6429519418531530241'
    if resp is not None:
        tt_webid = re.search(r'tt_webid=(.+?);', resp.headers["Set-Cookie"]).group(1)
    else:
        self.error('tt_webid error : %s'%resp)
    __tasessionId = "".join(random.sample(string.digits + string.letters, 16))[:9] + str(int(round(time.time() * 1000)))
    cookie = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
        "Cookie":'__tasessionId={};tt_webid={}'.format(__tasessionId, tt_webid)}
    count = 0
    while 1:
        if count > maxNum:
            break
        content = self.getPageDict(url, head=cookie)
        if content and "data" in content:
            for u in content["data"]:
                count = count + 1
                ToutiaoItem().getItemInfo(u)
                # list_data.append(u)
            if "next" in content and "max_behot_time" in content["next"]:
                if content["next"]["max_behot_time"] == 0:
                    time.sleep(2)
                    # url = url 重新访问链接,相当于在浏览器中刷新
                else:
                    if url.endswith("&max_behot_time=0"):
                        url = url[:-1] + str(content["next"]["max_behot_time"])
                    else:
                        url = url[:-10] + str(content["next"]["max_behot_time"])
            else:break
        else:break
```