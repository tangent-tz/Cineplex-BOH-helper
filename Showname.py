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
movienametime=getMovieTimes(movies,movie_name, movienametime)


for i in range(len(movie_name)):
     print(moviename[i])
     print(movienametime[i],"\n")

          


driver.quit()
