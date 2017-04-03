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

# FINALLY something that gets results

api_key = 'AIzaSyCrFWiPfGcb5IsyS-wpAMk6eaNdMaC8pXs'
standard_channel = 'UC4a-Gbdw7vOaccHmFo40b9g'
medicine_channel = 'UCJayvjGvKEblkA3KYK1BQQw'
sat_channel = 'UCb6Pzsn8oIFv1N8eGem570'
adm_channel = 'UCFS0Ox4LDKIx6lJED9r51Cw'

# https://www.googleapis.com/youtube/v3/search?channelId=UC4a-Gbdw7vOaccHmFo40b9g&pageToken=%22%22&order=videoCount&type=playlist&part=snippet&key=AIzaSyCrFWiPfGcb5IsyS-wpAMk6eaNdMaC8pXs&maxResults=5

parameters = {'part': 'snippet',
              'maxResults': '50',
              'channelId': adm_channel,
              'pageToken': '',
              'order': 'videoCount',
              'type': 'playlist',
              'key': api_key}

"""
parameters = {'part': 'snippet',
              'maxResults': '50',
              'order': 'date',
              #'publishedAfter': '2008-08-04T00:00:00Z',
              #'publishedBefore': '2008-11-04T00:00:00Z',
              #'publishedAfter': '2017-01-01T00:00:00Z',
              #'publishedBefore': '2017-01-08T00:00:00Z',
              'q': 'Khan_Academy',
              'type': 'channel',
              'key': api_key}
"""



url =  "https://www.googleapis.com/youtube/v3/search"

l = []

while True:
  # construct the url
  url3 = url
  symbol = '?'
  for k in parameters:
      if parameters[k] != '':
          url3 = url3+symbol+k+'='+parameters[k]
          symbol = '&'


  print(url3)

  data = json.load(urllib2.urlopen(url3))

  #urlVid =  'https://www.googleapis.com/youtube/v3/videos?part=id,statistics&id='

  #pdb.set_trace()

  # Fields: playlistId, snippet-publishedAt, snippet-title, snippet-description, snippet-thumbnails-default-url

  for item in data['items']:
    #l.append([item['id']['playlistId'], item['snippet']['publishedAt'], item['snippet']['channelTitle'], item['snippet']['description'], item['snippet']['thumbnails']['default']['url']])
    l.append(item)

  if 'nextPageToken' not in data.keys():
    break

  parameters['pageToken'] = data['nextPageToken']

#pdb.set_trace()

def getPlaylistVideos(pl_id):

  # https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=PL19E79A0638C8D449&key=AIzaSyCrFWiPfGcb5IsyS-wpAMk6eaNdMaC8pXs&maxResults=50

  base_url = "https://www.googleapis.com/youtube/v3/playlistItems"

  parameters = {"part": "snippet",
                "playlistId": pl_id,
                "key": api_key,
                "maxResults": "50"}

  v_list = []

  while True:
    # construct the url
    url3 = base_url
    symbol = '?'
    for k in parameters:
        if parameters[k] != '':
            url3 = url3+symbol+k+'='+parameters[k]
            symbol = '&'


    print(url3)

    data = json.load(urllib2.urlopen(url3))

    #urlVid =  'https://www.googleapis.com/youtube/v3/videos?part=id,statistics&id='

    #pdb.set_trace()

    # Fields:

    for item in data['items']:
      #l.append([item['id']['playlistId'], item['snippet']['publishedAt'], item['snippet']['channelTitle'], item['snippet']['description'], item['snippet']['thumbnails']['default']['url']])
      v_list.append(item)

    if 'nextPageToken' not in data.keys():
      break

    parameters['pageToken'] = data['nextPageToken']

  return v_list

for playlist in l:
  pl_id = playlist["id"]["playlistId"]

  playlist["videos"] = getPlaylistVideos(pl_id)

#with open('khanStandardPlaylists.json', 'w') as kp:
#with open('khanMedicinePlaylists.json', 'w') as kp:
with open('khanCollegeAdmissionsPlaylists.json', 'w') as kp:
  json.dump(l, kp)










