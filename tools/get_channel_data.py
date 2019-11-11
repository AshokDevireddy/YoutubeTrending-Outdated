import os
import json
import requests

API_TOKEN = 'AIzaSyDfzZw-wSX8NfI2vamY38igjIkIMimv_eA'
API_URL_BASE = 'https://www.googleapis.com/youtube/v3'

def search_vids_keyword(search_keyword):
#    response = requests.get("%s/search?part=snippet&maxResults=50&q=%s&%s" (API_URL_BASE, search_keyword, API_TOKEN)
    response = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&q=a&key=AIzaSyDfzZw-wSX8NfI2vamY38igjIkIMimv_eA")
    print(json.loads(response.content))
    f = open("tools/response.json","w+")
    f.write(json.dumps(json.loads(response.content), indent = 4, separators = (", ", "= ")))
    f.close();

search_vids_keyword('a');
