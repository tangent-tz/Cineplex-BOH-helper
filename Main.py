from Parsers import *
from Showtype import showTypes
from MovieNames import *
from MovieTimes import *
from MovieTicketSales import movieTicketSales
from filter import filterjunk, filtertime
from Utilities import *
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

#Features implmeneted so far
#    Success fully retreives the name of all the movie running in the threatre, Check Function getMovieNames()
#    Recovers all the type of threates (DBOX/ULTRAAVX/VIP/REGULAR/ETC) running in the threatres
#    Recovers all the movie running time from the threates
#    Recovers all the ticket sales so far for the movies

if __name__ == "__main__":
     movie_time=[]
     movie_name=[]
     moviename=[]
     PATH = "C:\Program Files (x86)\chromedriver.exe"
     options = Options()
     options.add_argument('--no-sandbox')
     options.add_argument("--start-maximized")
     options.add_argument("--window-size=1920x1080")
     options.add_argument('--disable-extensions')
     options.add_argument("--disable-gpu")
     options.add_argument("--disable-dev-shm-usage")
     options.add_argument("--proxy-bypass-list=*")
     options.add_argument('--ignore-certificate-errors')
     
     driver = webdriver.Chrome(PATH, options=options)
     
     driver.execute_cdp_cmd("Page.setBypassCSP", {"enabled": True})
     driver.get("https://www.cineplex.com/Theatre/cineplex-cinemas-marine-gateway-and-vip")
     html=driver.page_source
     soup=BeautifulSoup(html, 'lxml')
     moviename=getMovieNames(soup,movie_name,moviename)
     movie_time=getMovieTimes(soup)
     showtypes=showTypes(soup)
     url_seating=movie_ticket_link_parser(soup)
     movie_time_refined=[]
     movie_time_refined=movie_time_refiner(movie_time)
     size=getCount(movie_time_refined)
     ticket_sales_status=TicketSalesOnline(soup)
     seats=movieTicketSales(url_seating, options)
     show_type_per_movie=numberOfShowTypesPerMovie(soup)
     movie_per_show_type=getCount(movie_time_refined)
     
     temp=movieSalesStatus(ticket_sales_status, seats)
     
     print(movie_per_show_type)
     x=0
     A=[]
     B=[]
     for temped in enumerate(movie_per_show_type):
          for i in range(temped[1]):
               #rint(temp[x])
               A.append(temp[x])
               x+=1
          B.append(A)
          A=[]
          #print("next show")

     printer(movie_name,show_type_per_movie,showtypes,movie_time_refined, temp, B)

     driver.quit()