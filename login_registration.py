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
time.sleep(5)
some_element= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout"), "Logout"))
driver.quit()