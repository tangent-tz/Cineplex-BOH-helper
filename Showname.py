from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = Options()
options.headless = True
driver = webdriver.Chrome(PATH, options=options)
driver.get("https://www.cineplex.com/Theatre/cineplex-cinemas-marine-gateway-and-vip")
html=driver.page_source
soup=BeautifulSoup(html, 'lxml')
movie_names=soup.find_all(class_='h3 theatre-movie-title margin-vertical-xs')
movie_names=list(dict.fromkeys(movie_names))
for movie_name in movie_names:
     print(f"Movie Name: {movie_name.text}")
driver.quit()
