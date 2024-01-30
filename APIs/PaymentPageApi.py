import requests

class PaymentPageApi:
    def __init__(self, url = None):
        self.url = url
        pass

    def get_invoice(self, refId):
        url = '{0}/api/account/invoice/{1}'.format(self.url, refId)
        req = requests.get(url, headers={"Content-Type": "application/json"})
        return req
    

    def log_PayPage(self, post_data):
        url = '{0}/api/account/login'.format(self.url)
        req = requests.post(url, headers={"Content-Type": "application/json"}, data= post_data)
        return req
    
    def confirm_PayPage(self, post_data):
        url = '{0}/api/account/login-confirmation'.format(self.url)
        req = requests.post(url, headers={"Content-Type": "application/json"}, data= post_data)
        return req
    
    def resend_PayPage(self, post_data):
        url = '{0}/api/account/resend-login-confirmation-code'.format(self.url)
        req = requests.post(url, headers={"Content-Type": "application/json"}, data= post_data)
        return req
    
    def msisdn_PayPage(self, refId):
        url = '{0}/api/account/msisdn/{1}'.format(self.url, refId)
        req = requests.put(url, headers={"Content-Type": "application/json"})
        return req
    
    def signout_PayPage(self):
        url = '{0}/api/account/signout'.format(self.url)
        req = requests.get(url, headers={"Content-Type": "application/json"})
        return req
    
class CallbackApi:
    def __init__(self, url= None):
        self.url = url

    def sms_callback(self, post_data):
        url = '{0}/api/Callback/sms-callback-streamtelecom'.format(self.url)
        req = requests.post(url, headers={"Content-Type": "application/json"}, data= post_data)
        return req
    
    def get_esia_success(self):
        url = '{0}/api/Callback/esia-callback-success'
        req = requests.get(url, headers={"Content-Type": "application/json"})
        return req
    
    def get_esia_error(self):
        url = '{0}/api/Callback/esia-callback-error'.format(self.url)
        req = requests.get(url, headers={"Content-Type": "application/json"})
        return req
    

class InstallmentApiPayPage:
    def __init__(self, url):
        self.url = url

    def installment_profiles(self, invoiceId):
        url = '{0}/api/installment/profiles?invoiceId={1}'.format(self.url, invoiceId)
        req = requests.get(url, headers={"Content-Type": "application/json"})
        return req
    
    def installment_profiles_put(self, invoiceId):
        url = '{0}/api/installment/profiles?invoiceId={1}'.format(self.url, invoiceId)
        req = requests.put(url, headers={"Content-Type": "application/json"})
        return req
    
    def confirm_installment(self, invoiceId):
        url = '{0}/api/installment/confirm?invoiceId={1}'.format(self.url, invoiceId)
        req = requests.post(url, headers={"Content-Type": "application/json"})
        return req
    
    def resend_confirm_installment(self, invoiceId):
        url = '{0}/api/installment/resend-confirm?requestId={1}'.format(self.url, invoiceId)
        req = requests.post(url, headers={"Content-Type": "application/json"})
        return req
    
    def create_installmentPayPage(self, post_data):
        url = '{0}/api/installment'.format(self.url)
        req = requests.post(url, headers={"Content-Type": "application/json"}, data= post_data)
        return req
    
    def actualize_payment(self, ids):
        url = '{0}/api/installment/actualize-payment/{1}'.format(self.url, ids)
        req = requests.put(url, headers={"Content-Type": "application/json"})
        return req
    

    def get_installment_payment(self, ids):
        url = '{0}/api/installment/payment/{1}'.format(self.url, ids)
        req = requests.get(url, headers={"Content-Type": "application/json"})
        return req
    
    def card_container(self):
        url = '{0}/api/installment/card-container'.format(self.url)
        req = requests.post(url, headers={"Content-Type": "application/json"})
        return req
    

class PasportData:
    def __init__(self, url = None):
        self.url = url

    def validate_pasport(self, post_data):
        url = '{0}/api/passport-data/is-passport-data-valid'.format(self.url)
        req = requests.post(url, headers={"Content-Type": "application/json"},data= post_data)
        return req
    

class ProfileApi:
    def __init__(self, url = None):
        self.url = url

    def put_profile(self):
        url = '{0}/api/profile'
        req = requests.put(url, headers={"Content-Type": "application/json"})
        return req
    
    def get_payment_tool(self):
        url = '{0}/api/profile/payment-tools'.format(self.url)
        req = requests.get(url, headers={"Content-Type": "application/json"})
        return req
    
    def get_confidentiality(self):
        url = '{0}/api/profile/confidentiality'.format(self.url)
        req = requests.get(url, headers={"Content-Type": "application/json"})
        return req
    
    def get_contract(self):
        url = '{0}/api/profile/contract'.format(self.url)
        req = requests.get(url, headers={"Conten-Type": "application/json"})
        return req
    

class RedirectApi:
    def __init__(self, url = None):
        self.url = url
    
    def redirect_payments(self):
        url = '{0}/api/paymaster-redirect/payments/return'
        req = requests.get(url, headers={"Content-Type": "application/json"})
        return req
    
    def redirect_token(self):
        url = '{0}/api/paymaster-redirect/tokens/return'.format(self.url)
        req = requests.get(url, headers={"Content-Type": "application/json"})
        return req