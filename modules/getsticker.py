import main

def getsticker(lol):
    uri = main.stickers()[0]
    bytes = main.get_file_content_chrome(uri)
    if main.stickers()[1] == False:
        f = open("sticker/sticker.png","wb")
        f.write(bytes)
        f.close()
        ext = "sticker.png"
    else:
        f = open("sticker/sticker.gif","wb")
        f.write(bytes)
        f.close()
        ext = "sticker.gif"
    if lol == "":
      main.send_media(f'sticker/{ext}')
    else:
      return ext

def help():
    main.send_msg("""
```Get sticker in PNG and GIF format```
""")