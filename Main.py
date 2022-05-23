import itertools
import json

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from MovieInfoScrapperFuncs import MovieTicketSales
import config
from MovieInfoScrapperFuncs.Guestnumber import *
from MovieInfoScrapperFuncs.MovieNames import *
from MovieInfoScrapperFuncs.MovieTimes import *
from MovieInfoScrapperFuncs.Parsers import *
from MovieInfoScrapperFuncs.Showtype import getSreeningTypes
from MovieInfoScrapperFuncs.Utilities import *
from MovieInfoScrapperFuncs.filter import *

"""Features implmeneted so far
    Success fully retreives the name of all the movie running in the threatre, Check Function getMovieNames()
    Recovers all the type of threates (DBOX/ULTRAAVX/VIP/REGULAR/ETC) running in the threatres
    Recovers all the movie running time from the threates
    Recovers all the ticket sales so far for the movies"""


def setup_web_driver():
    driver = webdriver.Chrome(config.DEFAULT_PATHS["DEFAULT_WEBDRIVER"], options=config.DEFAULT_WEBDRIVER_OPTION)
    driver.execute_cdp_cmd("Page.setBypassCSP", {"enabled": True})
    return driver


def get_page_source_code(driver):
    driver.get(config.DEFAULT_PATHS["DEFAULT_CINEPLEX_WEBPAGE"])
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    return soup


def prep_movie_name(movie_name, page_soup):
    size_inner = getScreenTypesPerMovie(page_soup)
    size_outer = len(movie_name)
    movies = []
    for outer_iter in range(size_outer):
        for inner_iter in range(size_inner[outer_iter]):
            movies.append(movie_name[outer_iter])
    return movies


def generateRDPSURLSET(movie_name, movie_time, showtypes):
    URLvars = [movie_name[0:1], movie_time[0:1]]
    climatetilesURLCombinations1 = list(itertools.product(*URLvars))
    # climatetilesURLCombinations = climatetilesURLCombinations1

    for i in range(len(climatetilesURLCombinations1)):
        print(i, " : ", climatetilesURLCombinations1[i])
    # return climatetilesURLCombinations


if __name__ == "__main__":
    driver = setup_web_driver()
    page_soup = get_page_source_code(driver)
    movie_time = pretty_MovieTime(getMovieTimes(page_soup))
    movie_name = prep_movie_name(getMovieNames(page_soup), page_soup)
    showtypes = getSreeningTypes(page_soup)
    # url_seating = getMovieTicketUrl(page_soup)
    # print(url_seating)
    # ticket_sales_status = getTicketSales(page_soup)
    #
    ticket_sold = MovieTicketSales.getTicketSoldStatus(getMovieTicketUrl(page_soup), ticketsold=True)
    total_seats = MovieTicketSales.getTicketSoldStatus(getMovieTicketUrl(page_soup), totalseat=True)
    generateRDPSURLSET(movie_name, movie_time, showtypes)
    # print(movie_name)
    print(movie_time)
    # print(showtypes)
    # print(len(ticket_sold))
    # print(len(total_seats))
    # show_type_per_movie = getScreenTypesPerMovie(soup)
    # movie_per_show_type = getMoviePerScreenType(movie_time_refined)
    # #
    # temp = movieSalesStatus(ticket_sales_status, ticket_sold)
    # guest_list = guestnumber(movie_per_show_type, temp)
    # #
    # json_string = printer(moviename, show_type_per_movie, showtypes, movie_time_refined, guest_list)
    # with open('MovieData.json', 'w') as fp:
    #     json.dump(json_string, fp)
    # with open('MovieData.json', 'r') as fp:
    #     data = json.load(fp)
    # driver.quit()
