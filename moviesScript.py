# Scraping movies from IMDB
# Written by Erik Stinnett

import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Scraping title, runtime, rating, metascore, votes, gross
movieTitle = []
runTime = []
genre = []
relDate = []
userRating = []
metaScore = []

def scrapeMovieData():

    movie_data = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})

    for i in movie_data:
        name = i.h3.a.text
        # Title
        movieTitle.append(name) 

        date = i.h3.find('span', class_ = 'lister-item-year text-muted unbold').text.replace('(','').replace(')','')
        # Release Date
        relDate.append(date)

        time = i.p.find('span', class_ = 'runtime').text.replace('min','')
        # Runtime
        runTime.append(time)

        rating = i.find('div', class_ = 'inline-block ratings-imdb-rating').text.strip()
        # user rating
        userRating.append(rating)

        meta = i.find('span', class_ = 'metascore').text.strip() if i.find('span', class_ = 'metascore') else 'N/A'
        # Metascore
        metaScore.append(meta)

        movieGenre = i.find('span', class_ = 'genre').text.strip()
        genre.append(movieGenre)

def writeMoviesToDatabase():
    conn = sqlite3.connect('testDBProject.db')
    c = conn.cursor()

    c.execute('''DROP TABLE IF EXISTS film''')
    c.execute('''CREATE TABLE film(Title TEXT, Date TEXT, Runtime INT, UserRating INT, MetaScore INT, Genre text)''')
    for i in range(90):
        c.execute('''INSERT INTO film VALUES(?,?,?,?,?,?)''', (movieTitle[i], relDate[i], runTime[i], userRating[i], metaScore[i], genre[i]))
        conn.commit()
