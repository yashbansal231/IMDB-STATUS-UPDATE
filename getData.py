import requests
import json
from bs4 import BeautifulSoup
import logging
import datetime as dt
import time
import os
import pandas as pd

def gather_HTML(url):
    response = requests.get(url)
    html = response.content
    return BeautifulSoup(html, 'html.parser')
def update_database_ID():
    titles_url = "https://www.imdb.com/chart/tvmeter"
    top_rated = "https://www.imdb.com/chart/toptv/"
    name = []
    ids = []
    urls = [titles_url,top_rated]
    for x in urls:
        soup = gather_HTML(x)
        data = soup.find_all('td', attrs={'class':'titleColumn'})

        for x in data:
            name.append(str(x.a.text).lower())
            ids.append(str(x.a.get('href')).split('/')[2])

    data = pd.DataFrame({
        "Name" : name,
        "Id" : ids
    })
    data.to_csv("moreids.csv")
def getContentInf(name):
    now_year = dt.datetime.now().year
    url = "https://www.imdb.com/title/"+name+"/"
    raw = gather_HTML(url)
    div = raw.find('div', attrs={'class':'seasons-and-year-nav'})
    div_req = div.find_all('div')
    year = []
    for x in div.find_all('a'):
        try:
            year.append(int(x.text))
        except:
            continue
    year.sort(reverse=True)
    if(year[0]<now_year):
        return("The show has finished streaming all its episodes.")
    elif(year[0]==now_year):
        url = url + "episodes?year="+str(year[0])
        return("Next episode airs on "+ str(getDate(url)))
    else:
        return("The next season begins in " + str(year[0]))
def getDate(url):
    data = gather_HTML(url)
    date = data.find_all('div',attrs={'class':'airdate'})
    return date[-1].text.strip()
'''
series = ["tt1632701"]
for x in series:
    msg = getContentInf(x)
    print(msg)
'''