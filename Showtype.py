def getShowTypes(soup):
    showtypes = []
    titles = soup.find_all(class_="banner-image")
    for index2, movie2 in enumerate(titles):
        showtypes.append(movie2.get("title"))
    return showtypes
