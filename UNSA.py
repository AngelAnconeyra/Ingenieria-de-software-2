
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.unsa.edu.pe/")
#time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="wr-megamenu-menu-14"]/li[8]/a').click()
web_element = driver.find_element(By.NAME,'search')
web_element.send_keys("Ciencia de la computación" + Keys.ENTER)
time.sleep(5)

driver.get("http://fips.unsa.edu.pe/cienciadelacomputacion")
time.sleep(5)

