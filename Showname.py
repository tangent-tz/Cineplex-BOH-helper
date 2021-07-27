from Showtype import showTypes
from MovieNames import *
from MovieTimes import *
from filter import filterjunk, filtertime
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pathlib

if __name__ == "__main__":
     movienametime=[]
     movie_name=[]
     moviename=[]
     PATH = "C:\Program Files (x86)\chromedriver.exe"
     options = Options()
     options.headless = True
     driver = webdriver.Chrome(PATH, options=options)
     driver.get("https://www.cineplex.com/Theatre/cineplex-cinemas-marine-gateway-and-vip")
     html=driver.page_source
     soup=BeautifulSoup(html, 'lxml')
     movies=soup.find_all(class_='movie-showtimes-row row ng-scope')
     moviename=getMovieNames(movies,movie_name,moviename)
     movienametime=getMovieTimes(soup)
     showtypes=showTypes(soup)
     size=getCount(soup)
    # url_seating=movie_meta_datas(soup)

     # print("\n")
     # for i in range(len(movie_name)):
     #      print(moviename[i])
     #      for j in range(size[i]):
     #           print(showtypes[j].upper())
     #           print(movienametime[j])
     #           print("\n")
     #      print("\n")
     driver.quit()
