# Parametres: movies=(page HTML source), movie_name=(List data variable), moviename= (List data variable)
def getMovieNames(soup, movie_name, moviename):
    movies = soup.find_all(class_='movie-showtimes-row row ng-scope')
    for index, movie in enumerate(movies):
        movie_name.append(movie.find(class_='h3 theatre-movie-title margin-vertical-xs').text)

    for i in range(len(movie_name)):
        moviename.append(movie_name[i])
    return moviename
