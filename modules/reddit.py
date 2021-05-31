# import main,
import requests, os,time

def reddit(input):
    # print(input)
    # args = input.split(" ")
    # print(args)
    # if input == "":
        # main.send_msg("```no subreddit requested!```")
    # else:
        page = requests.get(f'https://www.reddit.com/r/{input}/new/.json').json()
        if 'error' in page.keys():
            print('retry?')
            # main.time.sleep(1)
            time.sleep(1)
            reddit(input)
        else:
            imageurl = page['data']['children'][0]['data']['url_overridden_by_dest']
            print(imageurl)
            print(os.path.basename(imageurl))
            imagetitle = page['data']['children'][0]['data']['title']
            postlonk = 'www.reddit.com' + page['data']['children'][0]['data']['permalink']
            print(imageurl, imagetitle, postlonk)
            pic = open('download/'+os.path.basename(imageurl), 'x')
            pic.write(requests.get(imageurl, allow_redirects=True).content)
            # main.send_media('download/'+os.path.basename(imageurl))

# def help():
#     main.send_msg("```Sends Posts from reddit, yay! -_-```")