import json
import csv
import urllib2

api_key = 'AIzaSyCrFWiPfGcb5IsyS-wpAMk6eaNdMaC8pXs'
url =  'https://www.googleapis.com/youtube/v3/videos?part=id,statistics&id='

with open('test.json') as f:    
    data = json.load(f)
    l = []

    for item in data['items']:
    	l.append([item['id']['videoId'], item['snippet']['title'], item['snippet']['description']])
    
    with open('videoStats.csv', 'wb') as c:
        writer = csv.writer(c)
        writer.writerow(['Id', 'Title', 'Description', 'LikeCount', 'DislikeCount', 'ViewCount', 'FavoriteCount', 'CommentCount'])

        for vid in l:
            stats = json.load(urllib2.urlopen(url + vid[0] + '&key=' + api_key))
            s = stats['items'][0]['statistics']
            writer.writerow([vid[0], vid[1].encode('utf8'), vid[2].encode('utf8'), s['likeCount'], s['dislikeCount'], s['viewCount'], s['favoriteCount'], s['commentCount']])