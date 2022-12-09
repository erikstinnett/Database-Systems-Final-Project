# Driver function
# Written by Erik Stinnett
from actors2 import *
from moviesScript import *


if __name__ == "__main__":
    scrapeMovieData()
    scrapeActorData_actors2()
    writeMoviesToDatabase()
    writeActorsToDatabase_actors2()