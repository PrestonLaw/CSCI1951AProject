import json
import csv
import urllib2
import re
import string

api_key = 'AIzaSyCrFWiPfGcb5IsyS-wpAMk6eaNdMaC8pXs'
url =  'https://www.googleapis.com/youtube/v3/videos?part=id,statistics&id='

regex = re.compile('[%s]' % re.escape(string.punctuation))

with open('test.json', 'rb') as f:    
    data = json.load(f)
    l = []

    for item in data['items']:
    	l.append([item['id']['videoId'], item['snippet']['title'], item['snippet']['description']])
    
    with open('videoStats.csv', 'wb') as c:
        writer = csv.writer(c)
        writer.writerow(['Id', 'Title', 'Description', 'LikeCount', 'DislikeCount', 'ViewCount', 'FavoriteCount', 'CommentCount'])

        for vid in l:
            stats = json.load(urllib2.urlopen(url + vid[0] + '&key=' + api_key))

            if stats['items'] == []:
                writer.writerow([vid[0], vid[1].encode('utf8'), vid[2].encode('utf8'),0,0,0,0,0])
                continue

            s = stats['items'][0]['statistics']
            LC = 0
            DC = 0
            CC = 0

            if 'likeCount' in s:
                LC = s['likeCount']
            if 'dislikeCount' in s:
                DC = s['dislikeCount']
            if 'commentCount' in s:
                CC = s['commentCount']

            title = regex.sub('', vid[1])
            descr = regex.sub('', vid[2])

            writer.writerow([vid[0], title.encode('utf8'), descr.encode('utf8'), LC, DC, s['viewCount'], s['favoriteCount'], CC])