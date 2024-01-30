import requests

class Message:

    def __init__(self, url=None, apikey=None):
        self.url = url
        self.apikey = apikey
    
    def post_message(self, post_data):
        url = '{0}/Profile/support'.format(self.url)
        req = requests.post(url, headers={"X-API-KEY": self.apikey, "Content-Type": "application/json"}, data= post_data)
        return req