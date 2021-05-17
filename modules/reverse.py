import main
import requests
from bs4 import BeautifulSoup
from .getsticker import getsticker

def reverse(args):
    try:
        uri = main.replied_media()
        bytes = main.get_file_content_chrome(uri)
        f = open("sticker/reverse.png","wb")
        f.write(bytes)
        f.close()
        name = "sticker/reverse.png"
    except:
        name = "sticker/" + getsticker("x") 
    print(name)
    searchUrl = "https://www.google.com/searchbyimage/upload"
    multipart = {"encoded_image": (name, open(name, "rb")), "image_content": ""}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False, headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"})

    if response == 400:
        main.send_msg("**Google told me to fuck off.**")
    else:
        sauce = BeautifulSoup(response.text)
        main.send_msg(str(sauce.a['href']))

def help():
    main.send_msg("```Uploads Image to google and sends link to look up```")