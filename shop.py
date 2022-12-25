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
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
login_name = driver.find_element_by_id("username")
login_name.send_keys("snooper743@gmail.com")
login_password = driver.find_element_by_id("password")
login_password.send_keys("Rexxar09051945")
login_btn = driver.find_element_by_css_selector("#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button")
login_btn.click()
shop_btn = driver.find_element_by_link_text("Shop")
shop_btn.click()
html_book = driver.find_element_by_class_name("post-181")
html_book.click()
book_title = driver.find_element_by_css_selector(".entry-summary > h1")
book_title_txt = book_title.text
if book_title_txt == "HTML5 Forms":
    print("Название совпадает")
else:
    print("Название НЕ совпадает")
driver.quit()