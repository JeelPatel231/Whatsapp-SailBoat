import main,os
import downloader

def dl(link):
    main.send_msg("starting download!")
    downloader.Download(link,"download/"+os.path.basename(link)).download()
    main.send_msg("download finished!")


def help():
    main.send_msg(
"""
```Downloads stuff locally from links/magnets/torrentfile```
""")