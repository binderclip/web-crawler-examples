import json
import logging
import os
from typing import Dict

import requests
import scrapy

CONFIG_FILE_PATH = os.path.expanduser('~/.lanfan-weibo-crawler-config.json')


def trans_weibo_short_url(short_url: str) -> str:
    headers = {
        "User-Agent": "spider",
    }
    try:
        r = requests.get(short_url, headers=headers)
    except Exception as e:
        logging.error(f'request error: {e}')
        return ''
    if r and r.url:
        return r.url


def _read_config() -> Dict[str, str]:
    try:
        with open(CONFIG_FILE_PATH) as f:
            return json.load(f)
    except FileNotFoundError:
        _write_config({})
        return {}


def _write_config(data: Dict[str, str]):
    with open(CONFIG_FILE_PATH, 'w') as f:
        json.dump(data, f)


def mark_weibo_as_operated(text: str, url: str):
    config = _read_config()
    config[text] = url
    _write_config(config)


def check_if_weibo_operated(text: str) -> bool:
    config = _read_config()
    return text in config


class WeiboDetailPageSpider(scrapy.Spider):
    name = "weibo-lanfan-homepage"
    start_urls = [
        'https://weibo.com/lanfanmeishi?is_all=1'
    ]

    def parse(self, response):
        # 遍历微博卡片节点
        for node in response.xpath('//div[@class="WB_feed_detail clearfix" and @node-type="feed_content"]'):
            # 获取微博发送时间
            date = (node.xpath('.//a[@node-type="feed_list_item_date"]/text()').get() or '').strip()
            if not '今天' in date:
                continue
            # 判断是不是转发微博
            sub_forward_node = node.xpath('.//div[@node-type="feed_list_forwardContent"]')
            if sub_forward_node:
                continue
            # 获取微博文字
            lines = node.xpath('.//div[@class="WB_text W_f14" and @node-type="feed_list_content"]/text()').getall()
            text = '\n'.join(lines).strip(' \n\u200b')
            # 获取视频链接
            short_url = node.xpath('.//i[@class="W_ficon ficon_cd_video"]/../@href').get()
            url = trans_weibo_short_url(short_url)
            if not url:
                continue
            if check_if_weibo_operated(text):
                continue
            mark_weibo_as_operated(text, url)
            yield {
                'text': text,
                'url': url,
            }
