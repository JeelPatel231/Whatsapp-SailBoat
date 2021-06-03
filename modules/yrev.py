import main
import requests,json
from .getsticker import getsticker

def yrev(args):
    try:
        main.replied_media()
        name = "sticker/replied.png"
    except:
        name = "sticker/" + getsticker("x") 

    searchUrl = 'https://yandex.ru/images/search'
    files = {'upfile': ('blob', open(name, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)
    if "captcha" in response.json():
        main.send_msg("```fucking captcha!```")
    else:
        query_string = json.loads(response.content)['blocks'][0]['params']['url']
        img_search_url= searchUrl + '?' + query_string
        main.send_msg(img_search_url)

def help():
    main.send_msg("```Uploads Image to Yandex and sends link to look up```")