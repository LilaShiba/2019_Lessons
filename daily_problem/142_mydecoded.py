import requests
from bs4 import BeautifulSoup

username = """
password = ""
csrfmiddlewaretoken= ""


 
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
    #print(r.text)
    # parse with bs4
    r = s.get(url)
    soup = BeautifulSoup(r.content, 'html5lib') 
    my_divs = soup.findAll("div", {"class": 'attendee-container'})
    #print(my_divs)
    scores = []

    score = soup.find("span", {"class": 'answer'})
    scores.append(score)
    print(scores)
        
    #section = soup.find_all(‘section’, class_=’facts-categories’)

