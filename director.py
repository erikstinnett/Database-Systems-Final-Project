# Scraping director data from IMDB
# Written by Erik Stinnett
import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

director_data = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})
fname = []
lname = []
directs = []

for i in director_data:
    # Get movie title of directed movie
    title = i.h3.a.text
    directs.append(title) 

    #Find DIRECTOR for each movie
    name = i.find('p', class_='').a.text
    try:
        fullName = name.split(' ', 1)
        first, last = fullName[0], fullName[1]
        fname.append(first)  # All first names
        # Find DIRECTOR for each movie
        #name = i.find('p', class_='').a.text
        #fname.append(name)
        lname.append(last)
    except:
        fname.append(first)
        lname.append(None)


print(lname)

conn = sqlite3.connect('testDBProject.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS directors''')
c.execute('''CREATE TABLE directors(Fname TEXT, Lname TEXT, Directs TEXT)''')

for i in range(90):
    c.execute('''INSERT INTO directors VALUES(?,?,?)''', (fname[i], lname[i], directs[i]))
    conn.commit()