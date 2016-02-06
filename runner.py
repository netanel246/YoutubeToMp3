from requests import get
from os.path import join
import json
from urllib import request as req

json_responses = []
base_url = "http://www.youtubeinmp3.com/fetch/?format=JSON&video="
res_folder = "/home/netanel/songs/"


class MP3Song:
    """

    """
    def __init__(self, title, link, start=None, end=None):
        self._title = title
        self._link = link

        if start is not None:
            self._start = start

        if end is not None:
            self._end = end

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def link(self):
        return self._link




with open(r"files/youtube_urls.txt", "r") as urls_file:
    for url in urls_file.readlines():
        #res = req.urlope0n(join(base_url, url))
        res = get(join(base_url, url))
        json_responses.append(res.text)


res_dict = json.loads(json_responses[0])
req.urlretrieve(res_dict["link"],
                join(res_folder, res_dict["title"] + ".mp3"))
