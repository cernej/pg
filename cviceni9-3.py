from unittest.mock import MagicMock
from sixth import download_url_and_get_all_hrefs
import requests


class Result:
    def __init__(self, status_code, content):
        self.ok = status_code == 200
        self.content = content




def test_download_url_and_get_all_hrefs():
    requests.get = MagicMock(return_value=Result(200, 'ahoj <a href="http://ahoj.cz">ahoj</a> ahoj'))
    assert download_url_and_get_all_hrefs("https://python.cz") == ["http://ahoj.cz"]
    requests.get = MagicMock(return_value=Result(500, ''))
    assert download_url_and_get_all_hrefs("https://python.cz") == []


