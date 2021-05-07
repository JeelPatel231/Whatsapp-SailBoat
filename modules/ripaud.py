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
    try:
        os.remove("YTDL/ytdlaudio.mp3")
    except:
        pass
    main.send_msg("starting download!")
    list = [str(context)]
    print(list)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(list)
    main.send_msg("download finished, sending audio..")
    main.send_media("YTDL/ytdlaudio.mp3")