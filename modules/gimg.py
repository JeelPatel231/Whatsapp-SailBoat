import main
from bs4 import BeautifulSoup
import requests


def gimg(args):
    image_request = requests.get(f'https://www.google.com/search?tbm=isch&q={args}',headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    html = BeautifulSoup(image_request.text)
    avail_imgs = html.find_all('img',{"class":"rg_i Q4LuWd"})
    avail_sources = []
    for source in avail_imgs:
        if "data-src" in str(source):
            avail_sources.append(str(source.get("data-src")))
    for link in avail_sources[:5]:
        open('download.png', 'wb').write(requests.get(link, allow_redirects=True).content)
        main.send_media('download.png')
        main.time.sleep(1)
        main.click_send()

def help():
    main.send_msg("```Searches and sends back images of the text input```")