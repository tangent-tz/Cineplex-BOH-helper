from filter import *


def getMovieTimes(movies):
    movie_sub = []
    movie_time = movies.find_all(class_="showtime-grid col-xs-12")
    for index, movie in enumerate(movie_time):
        movie_sub.append(movie.text.replace('\n', ''))
        movie_sub[index] = filterJunkTime(movie_sub[index])
    return movie_sub


def getMoviePerScreenType(movie_time_refined):
    movie_count = []
    for index in range(len(movie_time_refined)):
        movie_count.append(len(movie_time_refined[index]))
    return movie_count


def getScreenTypesPerMovie(movies):
    movie_count = []
    screen_type_wrapper = movies.find_all(class_="col-xs-12 col-sm-8 theatre-showtime-selection-wrapper")
    for index, movie in enumerate(screen_type_wrapper):
        movie_count.append(len(movie.find_all(class_="showtime-grid col-xs-12")))
    return movie_count
