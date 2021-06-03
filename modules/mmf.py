import main
from .getsticker import getsticker
from PIL import Image, ImageDraw, ImageFont

def mmf(args):
    col,title = args.split(" ",1)
    if col == "w":
        r,g,b = 255
    elif col == "b":
        r,g,b = 0
    else:
        r,g,b = col.split(",")
    try:
        main.replied_media()
        img_src = "sticker/replied.png"
    except:
        img_src = "sticker/" + getsticker("x")
    print(img_src," ",title)
    img = Image.open(img_src, 'r')
    draw = ImageDraw.Draw(img)
    w, h = img.size

    font = ImageFont.truetype("ProductSans.ttf", int(h*0.13))
    text_w, text_h = draw.textsize(title, font)

    draw.text(((w - text_w) // 2, h - (text_h+(.20*text_h))), title, (int(r),int(g),int(b)), font=font)

    img.save(img_src)
    img.close()
    main.send_media(img_src)
    
def help():
    main.send_msg("```meme-ifies the given image.```")