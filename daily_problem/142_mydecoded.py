import requests
from bs4 import BeautifulSoup

username = "email"
password = "password"


 
login_url = ""
url = ""

# start session
s = requests.session()

with requests.session() as s:
    # fetch the login page
    s.get(login_url)
    csrfmiddlewaretoken = s.cookies['csrftoken']
    # post to the login form
    login_info = {
    "login": username, 
    "password": password, 
    "csrfmiddlewaretoken": csrfmiddlewaretoken
    }
    r = s.post(login_url,data=login_info, headers={"Referer":"https://my.decoded.com"})
    print(r.text)

