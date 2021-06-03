import requests
import main

def mal(anime):
    data = requests.get("https://api.jikan.moe/v3/search/anime?q="+anime).json()['results'][0]
    print(data)
    with open("download/anime.png","wb") as f:
        f.write(requests.get(data['image_url']).content)
    anime_text = f'*{data["title"]}*\n\nScore: *{data["score"]}*\nEpisodes: *{data["episodes"]}*\nRating: *{data["rated"]}*\n\n{data["synopsis"]}'
    print(anime_text)
    main.media_with_caption("download/anime.png",anime_text)

def help():
    main.send_msg("```shut the fuck up weeb```")