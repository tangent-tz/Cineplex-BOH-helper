
def getMovieNames(movies,movie_name,moviename):
    for index, movie in enumerate(movies):
        movie_name.append(movie.find(class_='h3 theatre-movie-title margin-vertical-xs').text)

    for i in range(len(movie_name)):
        moviename.append(movie_name[i])
    return moviename