from Parsers import *
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
import urllib.request
import json

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
     movies=soup.find_all(class_='movie-showtimes-row row ng-scope')
     moviename=getMovieNames(movies,movie_name,moviename)
     movie_time=getMovieTimes(soup)
     showtypes=showTypes(soup)
     size=getCount(soup)
     url_seating=movie_ticket_link_parser(soup)
 
     seats=[]
     for i in range(len(url_seating)):
          driver.get(url_seating[i])
          test=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "seatAvailabilityMessage")))
          result=driver.find_element_by_id("seatAvailabilityMessage")
          seats.append(result.text)
          driver.close()
          driver = webdriver.Chrome(PATH, options=options)
     temp=0
     movie_time_refined=[]
     movie_time_refined=movie_time_refiner(movie_time)
     for i in range(len(movie_time_refined)):
          for j in range(len(movie_time_refined[i])):
               #movie_time_refined[i][j]=movie_time_refined[i][j]+ "&& "+seats[temp]
               print(temp)
               temp=temp+1
     print("test:",len(seats))
     print("test1:",len(movie_time_refined))
     print("\n")
     for i in range(len(movie_name)):
          print(moviename[i])
          for j in range(size[i]):
               print(showtypes[j].upper())
               print(movie_time_refined[j])
               print("\n")
          print("\n")
