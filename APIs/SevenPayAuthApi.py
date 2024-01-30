import requests
from time import sleep

class AuthApi:
    def __init__(self, url=None):
        self.url = url
        pass

    def post_login(self, post_data):
        url = '{0}/api/Account/login'.format(self.url)
        req = requests.post(url, headers={"Content-Type": "application/json"}, data= post_data)
        return req
    
    def post_login_confirmation(self, post_data):
        url = '{0}/api/Account/login-confirmation'.format(self.url)
        req = requests.post(url, headers={"Content-Type": "application/json"}, data= post_data)
        return req
    
    def refresh_token(self, post_data):
        url = '{0}/api/Account/refresh-token'.format(self.url)
        req = requests.post(url, headers={"Content-Type": "application/json"}, data= post_data)
        return req
    
    def resend_login_conf(self, reqestId):
        url = '{0}/api/Account/resend-login-confirmation?requestId={1}'.format(self.url, reqestId)
        sleep(30)
        req = requests.post(url, headers={"Content-Type": "application/json"})
        return req
    
    def logout(self):
        url = '{0}/api/Account/logout'.format(self.url)
        req = requests.post(url, headers={"Content-Type": "application/json"})
        return req
    
    def installment_get(self, token):
        url = '{0}/api/Installment/get'.format(self.url)
        req = requests.post(url, headers= {"Content-Type": "application/json", "Authorization": "Bearer {0}".format(token)})
        return req