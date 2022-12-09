# Scraping actor/actress data from IMDB
# Written by Erik Stinnett
''' Scraped from IMDb's top 1000: same source as moviesScript.py'''
import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

fname = []
lname = []
acts_in = []

def scrapeActorData_actors2():
    actor_data = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})

    for i in actor_data:
        # Gets the movie title for each actor
        title = i.h3.a.text
        acts_in.append(title) 
        # Find actor
        actorName = i.find('p', class_='').next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.text
        if actorName == '|':
            actorName = i.find('p', class_='').next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.text

        # some actors did not have a last name. Hence try/except
        try:
            fullName = actorName.split(' ', 1)
            first, last = fullName[0], fullName[1]
            fname.append(first)  # All first names
            lname.append(last)
        except:
            fname.append(first)
            lname.append(None)

def writeActorsToDatabase_actors2():
    conn = sqlite3.connect('testDBProject.db')
    c = conn.cursor()

    c.execute('''DROP TABLE IF EXISTS actors''')
    c.execute('''CREATE TABLE actors(Fname TEXT, Lname TEXT, Acts_In TEXT)''')

    for i in range(90):
        c.execute('''INSERT INTO actors VALUES(?,?,?)''', (fname[i], lname[i], acts_in[i]))
        conn.commit()