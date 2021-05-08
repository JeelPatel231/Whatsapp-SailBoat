import main,os
import youtube_dl

ydl_opts = {
    'format': 'bestvideo[height<=144]+bestaudio/best',
    'outtmpl': "YTDL/ytdlaudio.%(ext)s",
        'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp3',
    }],
}
def ripaud(context):
    if context == "":
        main.send_msg("No Download Link found")
    else:
        try:
            os.remove("YTDL/ytdlaudio.mp3")
        except:
            pass
        main.send_msg("starting download!")
        list = [str(context)]
        print(list)
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(list)
            main.send_msg("download finished, sending audio..")
            main.send_media("YTDL/ytdlaudio.mp3")
        except youtube_dl.utils.DownloadError as e:
            main.send_msg(str(e))

def help():
    main.send_msg("""```
RipVid Usage :
.ripaud youtubelink

downloads songs and shares in the active chat.
    ```""")