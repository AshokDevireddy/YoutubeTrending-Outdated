import os
import json
import requests

API_TOKEN = os.environ['DEVELOPER_KEY'];
API_URL_BASE = 'https://www.googleapis.com/youtube/v3/'

response = requests.get(API_URL_BASE + "/channels")
print(response)

def get_channel_resources(channel_name)
{
    PARAMS = []
}