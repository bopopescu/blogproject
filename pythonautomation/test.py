from selenium import webdriver
import time
driver = webdriver.Chrome('/home/ganapathi/Desktop/Downloads/chromedriver')
driver.get("http://www.facebook.com")
element = driver.find_element_by_id("passwd-id")
time.sleep(5)
driver.close()
