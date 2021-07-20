from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pathlib
from io import StringIO


PATH = "C:\Program Files (x86)\chromedriver.exe"
options = Options()
options.headless = True
driver = webdriver.Chrome(PATH, options=options)
driver.get("https://www.cineplex.com/Theatre/cineplex-cinemas-marine-gateway-and-vip")
html=driver.page_source
soup=BeautifulSoup(html, 'lxml')
movies=soup.find_all(class_='movie-showtimes-row row ng-scope')
for index, movie in enumerate(movies):
     movie_name = movie.find(class_='h3 theatre-movie-title margin-vertical-xs').text
     print(movie_name)
     for index2, movie2 in enumerate(movies):
          movie_time= movie2.find(class_="showtime-grid col-xs-12").text.replace('\n','')
          movie_time=movie_time.replace(' ','')
          movie_time=movie_time.replace('m','m  |  ')
          print(movie_time)


driver.quit()
