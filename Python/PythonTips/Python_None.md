## None

```
success = False
if success:print "pass"             # no output
if success is not None:print "pass" # pass
print False is None                 # False
```
```
#解析头条视频用户json
def getUserInfo(self, obj):
    def get_one_info(self, json_con):
        url_list = []
        for json_content in json_con["data"]:
            u                 = json_content["article_url"]
            duration          = json_content['video_duration']
            publish_time      = json_content["publish_time"]
            video_watch_count = json_content["video_detail_info"]["video_watch_count"]
            video_like_count  = json_content["video_like_count"]
            name              = json_content["title"]
            media_name        = json_content["media_name"]
            comment_count     = json_content["comment_count"]
            bury_count        = json_content["bury_count"]
            digg_count        = json_content["digg_count"]
            if self.isInTimeRange(publish_time) == 2:
                url_list.append(u)
                self.writeObj2Item(ShortVideoBaseData(url=u,
                                                      duration=duration,
                                                      release_time=publish_time,
                                                      play_times=video_watch_count,
                                                      favorite=video_like_count,
                                                      name=name,
                                                      releaser=media_name,
                                                      commentNum=comment_count,
                                                      releaserUrl=obj.url,
                                                      down=bury_count,
                                                      channel=self.taskData.channel,
                                                      channelType=Constants.TypeUser))
        return url_list
    url = obj.url.rstrip("&format=html")
    json_content = self.getPageDict(url)
    name         = json_content["user_info"]["name"]
    fans         = json_content["user_info"]["followers_count"]
    list_urls    = get_one_info(self, json_content)
    next_url = url + "&format=json&max_behot_time={}".format(json_content["data"][-1]["behot_time"])
    while len(list_urls) < obj.maxNum and next_url:
        jso = self.getPageDict(next_url)
        list_urls.extend(get_one_info(self, jso))
        if jso["data"]:
            next_url = url + "&format=json&max_behot_time={}".format(jso["data"][-1]["behot_time"])
        else:
            next_url = None
    self.writeObj2Item(ShortVideoUserBaseData(name=name,
                                              url=obj.url,
                                              fans=fans,
                                              videoUrl=list_urls,
                                              channel=self.taskData.channel,
                                              sortType=obj.sortType))

```