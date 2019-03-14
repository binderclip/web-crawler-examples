import scrapy
import requests


class WeiboDetailPageSpider(scrapy.Spider):
    name = "weibo-detail-page"
    start_urls = [
        'https://weibo.com/6498488043/HkKgdE2Jp'
    ]

    def parse(self, response):
        text = response.xpath('//div[@node-type="feed_list_content"]/text()').get() or ''
        text = text.strip()
        video_short_url = response.xpath('//i[@class="W_ficon ficon_cd_video"]/../@href').get() or ''
        video_url = ''
        if video_short_url:
            headers = {
                "User-Agent": "spider",
            }
            r = requests.get(video_short_url, headers=headers)
            if r and r.url:
                video_url = r.url
        yield {
            'text': text,
            'video_url': video_url,
        }
