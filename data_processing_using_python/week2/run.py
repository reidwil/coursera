import requests
from week2.crawl import Crawler
import json



#!# this formatting sucks. ideally, it would be all in the correct dirs
with open('proxy.txt') as proxies:
    for line in proxies:
        proxy = json.loads(line)
with open('urls.txt') as f:
    urls = [line.strip() for line in f]

checker = {url: Crawler(url, proxy) for url in urls}
