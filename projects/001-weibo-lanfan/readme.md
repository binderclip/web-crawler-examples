# readme


## notes

```python
import requests

headers = {
    "User-Agent": "spider",
}
r = requests.get('http://t.cn/EMYvoP2', headers=headers)
print(r.url)
```


```text
https://weibo.com/6498488043/HkKgdE2Jp

r.css('div.W_f14::text').get()
r.xpath('//div[@node-type="feed_list_content"]/text()').get()
t.stripe()

r.xpath('//i[@class="W_ficon ficon_cd_video"]/../@href').get()

http://t.cn/EMYvoP2

https://weibo.com/lanfanmeishi?is_all=1
```

## refs

- [Selectors — Scrapy 1.6.0 documentation](https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors)
- [Scrapy Tutorial — Scrapy 1.6.0 documentation](https://docs.scrapy.org/en/latest/intro/tutorial.html)
- [小技巧绕过Sina Visitor System(新浪访客系统)](https://bindog.github.io/blog/2014/10/15/set-the-ua-to-bypass-sina-visitor-system/)
- [xpath - How to get immediate parent node with scrapy in python? - Stack Overflow](https://stackoverflow.com/questions/44418433/how-to-get-immediate-parent-node-with-scrapy-in-python)
