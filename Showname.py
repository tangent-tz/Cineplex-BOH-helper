from filter import filterjunk
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
for index, movie in enumerate(movies):
     movie_name.append(movie.find(class_='h3 theatre-movie-title margin-vertical-xs').text)
for i in range(len(movie_name)):
     moviename.append(movie_name[i])
for index2, movie2 in enumerate(movies):
     movie_time= movie2.find(class_="col-xs-12 movie-showtimes-section").text.replace('\n','')
     if 'https://mediafiles.cineplex.com/img/showtime_experience/vip19plus.png' in movie_time:
          times=movie_time.find(id='l_1145_s_69214_c_0000000001').text
     movie_time=movie_time.replace(' ','')
     movie_time=movie_time.replace('0pm','0pm|')
     movie_time=movie_time.replace('5pm','5pm|')
     movie_time=movie_time.replace('0am','0am|')
     movie_time=movie_time.replace('5am','5am|')
     movienametime.append(filterjunk(movie_time,movie_name))

for i in range(len(movie_name)):
     print(moviename[i])
     print(movienametime[i],"\n")

          


driver.quit()
