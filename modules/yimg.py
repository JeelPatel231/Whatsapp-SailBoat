# import main
from bs4 import BeautifulSoup
import requests

light_useragent = """Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/\
MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 \
Mobile Safari/537.36"""
heavy_ua1 = """Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"""
heavy_ua2 = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"""


def img(args):
    image_request = requests.get(f'https://yandex.com/images/search?text={args}',headers={"User-Agent": light_useragent})
    html = BeautifulSoup(image_request.text)
    print(html.div)

img("pumpkin pie")