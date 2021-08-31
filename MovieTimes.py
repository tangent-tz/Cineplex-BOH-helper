from filter import *


def getMovieTimes(movies):
    moviesub=[]
    movie_time= movies.find_all(class_="showtime-grid col-xs-12")
    for index, movie in enumerate(movie_time):
        moviesub.append(movie.text.replace('\n',''))
        moviesub[index]=filtertime(moviesub[index])
    return moviesub

def getMoviePerScreenType(movie_time_refined):
    moviecount=[]
    for i in range(len(movie_time_refined)):
        moviecount.append(len(movie_time_refined[i]))
    return moviecount


def getScreenTypesPerMovie(movies):
    moviecount=[]
    test=movies.find_all(class_="col-xs-12 col-sm-8 theatre-showtime-selection-wrapper")
    for index, movie in enumerate(test):
        moviecount.append(len(movie.find_all(class_="showtime-grid col-xs-12")))
    return moviecount