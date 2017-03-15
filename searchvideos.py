from __future__ import division
from datetime import datetime
import requests
from lxml import html, etree
import json
from textblob import TextBlob
import urllib2

import pandas as pd

import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# FINALLY something that gets results

api_key = 'AIzaSyCrFWiPfGcb5IsyS-wpAMk6eaNdMaC8pXs'
channel = 'UCF0pVplsI8R5kcAqgtoRqoA'


parameters = {'part': 'snippet',
              'maxResults': '5',
              'order': 'date',
              'publishedAfter': '2008-08-04T00:00:00Z',
              'publishedBefore': '2008-11-04T00:00:00Z',
              'q': 'Mark_Udall',
              'type': 'video',
              'key': api_key}

url =  "https://www.googleapis.com/youtube/v3/search"

# construct the url
url3 = url
symbol = '?'
for k in parameters:
    if parameters[k] != '':
        url3 = url3+symbol+k+'='+parameters[k]
        symbol = '&'


print(url3)

data = json.load(urllib2.urlopen(url3))

l = []
urlVid =  'https://www.googleapis.com/youtube/v3/videos?part=id,statistics&id='

for item in data['items']:
  l.append([item['id']['videoId'], item['snippet']['title'], item['snippet']['description']])

with open('videoStats.csv', 'wb') as c:
  writer = csv.writer(c)
  writer.writerow(['Id', 'Title', 'Description', 'LikeCount', 'DislikeCount', 'ViewCount', 'FavoriteCount', 'CommentCount'])

  for vid in l:
    stats = json.load(urllib2.urlopen(urlVid + vid[0] + '&key=' + api_key))
    s = stats['items'][0]['statistics']
    writer.writerow([vid[0], vid[1].encode('utf8'), vid[2].encode('utf8'), s['likeCount'], s['dislikeCount'], s['viewCount'], s['favoriteCount'], s['commentCount']])

