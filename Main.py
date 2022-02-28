import Development
from Parsers import *
from Showtype import getShowTypes
from MovieNames import *
from MovieTimes import *
from MovieTicketSales import getTicketSoldStatus
from filter import filterjunk, filtertime
from Utilities import *
from Guestnumber import *
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pathlib
import urllib.request
import json

# Features implmeneted so far
#    Success fully retreives the name of all the movie running in the threatre, Check Function getMovieNames()
#    Recovers all the type of threates (DBOX/ULTRAAVX/VIP/REGULAR/ETC) running in the threatres
#    Recovers all the movie running time from the threates
#    Recovers all the ticket sales so far for the movies

if __name__ == "__main__":
    movie_time = []
    movie_name = []
    moviename = []
    movie_time_refined = []

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    options = Options()
    # options.add_argument('--no-sandbox')
    # options.add_argument("--start-maximized")
    # options.add_argument("--window-size=1920x1080")
    options.add_argument('--disable-extensions')
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--headless")
    driver = webdriver.Chrome(PATH, options=options)
    driver.execute_cdp_cmd("Page.setBypassCSP", {"enabled": True})

    # Getting page source code
    driver.get("https://www.cineplex.com/Theatre/cineplex-cinemas-marine-gateway-and-vip")
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
    seats = Development.test(url_seating)
    show_type_per_movie = getScreenTypesPerMovie(soup)
    movie_per_show_type = getMoviePerScreenType(movie_time_refined)
    #
    temp = movieSalesStatus(ticket_sales_status, seats)
    Guestlist = guestnumber(movie_per_show_type, temp)
    #
    test = printer(movie_name, show_type_per_movie, showtypes, movie_time_refined, Guestlist)
    print(test)
    with open('MovieData.json', 'w') as fp:
         json.dump(test, fp)
    with open('MovieData.json', 'r') as fp:
         data = json.load(fp)
    driver.quit()
