import requests, json
from .constants import Recaptcha


from django.contrib import messages

def check_recpatcha(req) -> bool:
    clientkey = req.POST['g-recaptcha-response']
    captchaData = {
            "secret": Recaptcha.secretKey,
            "response": clientkey
        }  
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
    res = json.loads(r.text)
    verify = res['success']

    if clientkey:
       if verify:
         return True

       else:
            return 'There has been a problem in our system'
    else:
       return False 


def captchaVerificationFailedHandler(req, result):
    if result is False:
          messages.error(req, "Please check the recaptcha verification box.")
          
    else: 
        messages.error(req, "There has been a problem in our system. We are working on fixing this issue.")
               




