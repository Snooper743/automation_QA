from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
book = driver.find_element_by_class_name("sub_column_1-0-2-0")
book.click()
reviews = driver.find_element_by_class_name("reviews_tab")
reviews.click()
stars = driver.find_element_by_class_name("star-5")
stars.click()
review_txt = driver.find_element_by_id("comment")
review_txt.send_keys("Nice book!")
author = driver.find_element_by_id("author")
author.send_keys("Snooper")
email = driver.find_element_by_id("email")
email.send_keys("snooper743@gmail.com")
submit = driver.find_element_by_id("submit")
submit.click()
time.sleep(5)
driver.quit()