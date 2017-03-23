import json
import urllib2

api_key = 'AIzaSyCrFWiPfGcb5IsyS-wpAMk6eaNdMaC8pXs'
queryURL =  'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&order=date&publishedAfter=2008-08-04T00:00:00Z&type=video&key=AIzaSyCrFWiPfGcb5IsyS-wpAMk6eaNdMaC8pXs'

with open('test.json', 'wb') as j:
    results = json.load(urllib2.urlopen(queryURL))
    tok = results['nextPageToken']

    while True:
        temp = json.load(urllib2.urlopen(queryURL + '&pageToken=' + tok))
        results['items'].extend(temp['items'])

        if 'nextPageToken' not in temp:
            break

        tok = temp['nextPageToken']

    json.dump(results, j)