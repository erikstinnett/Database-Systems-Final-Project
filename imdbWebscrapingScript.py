# Driver function
# Written by Erik Stinnett
from actorsScript import *
from moviesScript import *


if __name__ == "__main__":
    scrapeMovieData()
    scrapeActorData()
    writeMoviesToDatabase()
    writeActorsToDatabase()