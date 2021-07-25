from filter import *


def getMovieTimes(movies,movie_name, movienametime):
    for index2, movie2 in enumerate(movies):
        movie_time= movie2.find(class_="col-xs-12 movie-showtimes-section").text.replace('\n','')
        if 'https://mediafiles.cineplex.com/img/showtime_experience/vip19plus.png' in movie_time:
            times=movie_time.find(id='l_1145_s_69214_c_0000000001').text
        movie_time=filtertime(movie_time)
        movienametime.append(filterjunk(movie_time,movie_name))
    return movienametime