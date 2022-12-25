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
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("snooper743@gmail.com")
reg_password = driver.find_element_by_id("reg_password")
reg_password.send_keys("Rexxar09051945")
register_btn = driver.find_element_by_css_selector(".register p > input.woocommerce-Button")
register_btn.click()
time.sleep(5)
driver.quit()