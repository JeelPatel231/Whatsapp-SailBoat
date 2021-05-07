import main,os
import youtube_dl

ydl_opts = {
    'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
    'videoformat' : "mp4",
    'outtmpl': "YTDL/ytdlvideo.%(ext)s",
        'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}
def ripvid(context):
    try:
        os.remove("YTDL/ytdlvideo.mp4")
    except:
        pass
    main.send_msg("starting download!")
    list = [str(context)]
    print(list)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(list)
    main.send_msg("download finished, sending video..")
    main.send_media("YTDL/ytdlvideo.mp4")