def getSreeningTypes(soup):
    screening_types = []
    titles = soup.find_all(class_="banner-image")
    for index2, movie2 in enumerate(titles):
        screening_types.append(movie2.get("title"))
    return screening_types
