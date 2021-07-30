from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def movieTicketSales(url_seating, options):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH, options=options)     
    driver.execute_cdp_cmd("Page.setBypassCSP", {"enabled": True})
    seats=[]
    for i in range(len(url_seating)):
        driver.get(url_seating[i])
        test=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "seatAvailabilityMessage")))
        result=driver.find_element_by_id("seatAvailabilityMessage")
        seats.append(result.text)
        driver.close()
        driver = webdriver.Chrome(PATH, options=options)
    driver.close()
    return seats
     
     