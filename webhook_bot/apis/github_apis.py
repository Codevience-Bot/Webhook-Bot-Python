import os
import requests
import json

class GithubApis(object):
    HEADERS = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': os.environ.get("github_token"),
        'Content-Type': 'application/json'
    }

    def __init__(self, url, payload):
        self.__headers = GithubApis.HEADERS
        self.__payload = payload
        self.__url = url

    def call(self):
        r = requests.post(self.__url,
                          data=json.dumps(self.__payload),
                          headers=self.__headers)
        print(r)
