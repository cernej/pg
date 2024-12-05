from unittest.mock import MagicMock
import requests


class Result:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content


def stahuj(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.content
    else:
        return ""


def test_stahuj():
    requests.get = MagicMock(return_value=Result(200, "obsah stranky"))
    assert stahuj("https://python.cz") == "obsah stranky"
    requests.get = MagicMock(return_value=Result(500, ""))
    assert stahuj("https://python.cz") == ""


if __name__ == "__main__":
    print(stahuj("https://python.cz"))