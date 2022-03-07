import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import MovieTicketSales
import config
from Guestnumber import *
from MovieNames import *
from MovieTimes import *
from Parsers import *
from Showtype import getShowTypes
from Utilities import *

"""Features implmeneted so far
    Success fully retreives the name of all the movie running in the threatre, Check Function getMovieNames()
    Recovers all the type of threates (DBOX/ULTRAAVX/VIP/REGULAR/ETC) running in the threatres
    Recovers all the movie running time from the threates
    Recovers all the ticket sales so far for the movies"""

if __name__ == "__main__":
    movie_time = []
    movie_name = []
    moviename = []
    movie_time_refined = []
    driver = webdriver.Chrome(config.DEFAULT_PATHS["DEFAULT_WEBDRIVER"], options=config.DEFAULT_WEBDRIVER_OPTION)
    driver.execute_cdp_cmd("Page.setBypassCSP", {"enabled": True})

    # Getting page source code
    driver.get(config.DEFAULT_PATHS["DEFAULT_CINEPLEX_WEBPAGE"])
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    # Gets Movie Names
    moviename = getMovieNames(soup, movie_name, moviename)

    # Gets Movie Schedule
    movie_time = getMovieTimes(soup)

    # Gets Movie Screen type
    showtypes = getShowTypes(soup)

    # Gets number of seats sold
    url_seating = getMovieTicketUrl(soup)
    movie_time_refined = pretty_MovieTime(movie_time)
    ticket_sales_status = getTicketSales(soup)
    #
    # seats=getTicketSoldStatus(url_seating, options)
    seats = MovieTicketSales.getTicketSoldStatus(url_seating)
    show_type_per_movie = getScreenTypesPerMovie(soup)
    movie_per_show_type = getMoviePerScreenType(movie_time_refined)
    #
    temp = movieSalesStatus(ticket_sales_status, seats)
    Guestlist = guestnumber(movie_per_show_type, temp)
    #
    test = printer(movie_name, show_type_per_movie, showtypes, movie_time_refined, Guestlist)
    with open('MovieData.json', 'w') as fp:
        json.dump(test, fp)
    with open('MovieData.json', 'r') as fp:
        data = json.load(fp)
    driver.quit()
    print(data["0"])
