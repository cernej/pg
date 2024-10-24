import requests
from lxml import html

res = requests.get("http://search.seznam.cz?q=seznam")
tree = html.fromstring(res.content)

print(tree)

urls = tree.xpath('//a/@href')

print(urls)