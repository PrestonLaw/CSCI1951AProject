from __future__ import division
from datetime import datetime
import requests
from lxml import html, etree
import json
from textblob import TextBlob
import urllib2
import csv

import pandas as pd

import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

import pdb








def videoSearch(query, start_time, end_time):

  api_key = 'AIzaSyCrFWiPfGcb5IsyS-wpAMk6eaNdMaC8pXs'
  channel = 'UCF0pVplsI8R5kcAqgtoRqoA'

  url =  "https://www.googleapis.com/youtube/v3/search"

  parameters = {'part': 'snippet',
                'maxResults': '5',
                'order': 'date',
                #'publishedAfter': '2008-08-04T00:00:00Z',
                #'publishedBefore': '2008-11-04T00:00:00Z',
                'publishedAfter': start_time,
                'publishedBefore': end_time,
                'q': query,
                'type': 'video',
                'key': api_key}

  pdb.set_trace()

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
    l.append([item['id']['videoId'], item['snippet']['title'], item['snippet']['description'], item['snippet']['publishedAt']])

  pdb.set_trace()

  with open('videoStats.csv', 'wb') as c:
    writer = csv.writer(c)
    writer.writerow(['Id', 'Title', 'Description', 'LikeCount', 'DislikeCount', 'ViewCount', 'FavoriteCount', 'CommentCount', 'PublishedAt'])

    for vid in l:
      stats = json.load(urllib2.urlopen(urlVid + vid[0] + '&key=' + api_key))
      s = stats['items'][0]['statistics']
      writer.writerow([vid[0], vid[1].encode('utf8'), vid[2].encode('utf8'), s['likeCount'], s['dislikeCount'], s['viewCount'], s['favoriteCount'], s['commentCount'], stats['items'][0]['snippet']])



if __name__ == "__main__":
  start_time = '2017-01-01T00:00:00Z'
  end_time = '2017-01-08T00:00:00Z'
  videoSearch('Khan_Academy', start_time, end_time)

  # If I want to get data across large stretches of time, that will be hard.  The best way is to make many different queries, each spanning a month or maybe season/year.

