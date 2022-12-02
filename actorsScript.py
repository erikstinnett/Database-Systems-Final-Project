import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://www.imdb.com/list/ls050274118/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

fName = []
lName = []
actsIn = []

actor_data = soup.findAll('div', attrs = {'class': 'lister-item mode-detail'})

count = 0
for i in actor_data:
    name = i.h3.a.text.strip()
    movieTitle = i.find('p', class_ = 'text-muted text-small').a.text.strip()
    actsIn.append(movieTitle)
    actorName = name.split(' ', 1)

    fName.append(actorName[0])  # All first names
    lName.append(actorName[1])  # All last names


conn = sqlite3.connect('testDBProject2.db')
c = conn.cursor()

c.execute('''DROP TABLE actors''')
c.execute('''CREATE TABLE actors(Fname TEXT, Lname TEXT, Acts_In TEXT, Awards TEXT)''')

for i in range(44):
    c.execute('''INSERT INTO actors VALUES(?,?,?,?)''', (fName[i], lName[i], actsIn[i], None))
    conn.commit()

c.execute('''SELECT Fname, Lname from actors''')
results = "\n".join(str(actor) for actor in c.fetchall())   # Splits list into lines of movies
print(results)