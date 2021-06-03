import requests,os,main
from .getsticker import getsticker

def rbg(args):
    try:
        uri = main.replied_media()
        bytes = main.get_file_content_chrome(uri)
        f = open("sticker/remove.png","wb")
        f.write(bytes)
        f.close()
        name = "sticker/replied.png"
    except:
        name = "sticker/" + getsticker("x") 
    print(name)

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(name, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': os.environ['REM_BG_API']},
    )
    if response.status_code == requests.codes.ok:
        with open('sticker/no-bg.png', 'wb') as out:
            out.write(response.content)
        main.send_media('sticker/no-bg.png')
    else:
        main.send_msg("Error:", response.status_code, response.text)