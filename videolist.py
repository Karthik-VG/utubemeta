from youtubesearchpython import VideosSearch


class videolist:
    def __init__(self,keyword):
        self.keyword=keyword
    def search(self):
        videosSearch = VideosSearch(self.keyword, limit = 20)
        res=(videosSearch.result())
        links_youtube = []
        channel_name = []
        for i in (res['result']):
            links_youtube.append(i["link"])
            channel_name.append(i["channel"]["name"])
        return links_youtube,channel_name