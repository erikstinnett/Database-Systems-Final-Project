import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://www.imdb.com/list/ls050274118/'
url2 = 'https://www.imdb.com/list/ls057000570/'
response = requests.get(url)
response2 = requests.get(url2)
soup = BeautifulSoup(response.content, 'html.parser')
soup2 = BeautifulSoup(response2.content, 'html.parser')

fName = []
lName = []
actsIn = []

actor_data = soup.findAll('div', attrs = {'class': 'lister-item mode-detail'})
actress_data = soup2.findAll('div', attrs = {'class': 'lister-item mode-detail'})

# Scraping for actor data
for i in actor_data:
    nameMen = i.h3.a.text.strip()
    movieTitle = i.find('p', class_ = 'text-muted text-small').a.text.strip()
    actsIn.append(movieTitle)
    actorName = nameMen.split(' ', 1)

    fName.append(actorName[0])  # All first names
    lName.append(actorName[1])  # All last names

# Scraping for actress data
for i in actress_data:
    nameWm = i.h3.a.text.strip()
    actressName = nameWm.split(' ', 1)
    movieTitle = i.find('p', class_ = 'text-muted text-small').a.text.strip()

    fName.append(actressName[0])  # All first names
    lName.append(actressName[1])  # All last names
    actsIn.append(movieTitle)
print(actsIn)


conn = sqlite3.connect('testDBProject.db')
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS film''')
c.execute('''DROP TABLE IF EXISTS actors''')
c.execute('''CREATE TABLE actors(Fname TEXT, Lname TEXT, Acts_In TEXT, Awards TEXT)''')

for i in range(150):
    c.execute('''INSERT INTO actors VALUES(?,?,?,?)''', (fName[i], lName[i], actsIn[i], None))
    conn.commit()

c.execute('''SELECT Fname, Lname from actors''')
results = "\n".join(str(actor) for actor in c.fetchall())   # Splits list into lines of movies
print(results)