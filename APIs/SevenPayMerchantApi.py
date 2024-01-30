import requests

class Merchant:
    def __init__(self, url=None, apikey=None):
        self.url = url
        self.apikey = apikey

    def get_invoice(self, id):
        url = '{0}/api/Invoice/{1}'.format(self.url, id)
        req = requests.get(url, headers={'X-API-KEY': self.apikey})
        return req
    
    def create_invoice(self, api_key,post):
        url = '{0}/api/Invoice'.format(self.url)
        req = requests.post(url, headers={"X-API-KEY": api_key, "Content-Type": "application/json"}, data=post)
        return req