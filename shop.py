from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from selenium import webdriver

# # title check
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login_name = driver.find_element_by_id("username")
# login_name.send_keys("snooper743@gmail.com")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("Rexxar09051945")
# login_btn = driver.find_element_by_css_selector("#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button")
# login_btn.click()
# shop_btn = driver.find_element_by_link_text("Shop")
# shop_btn.click()
# html_book = driver.find_element_by_class_name("post-181")
# html_book.click()
# book_title = driver.find_element_by_css_selector(".entry-summary > h1")
# book_title_txt = book_title.text
# if book_title_txt == "HTML5 Forms":
#     print("Название совпадает")
# else:
#     print("Название НЕ совпадает")
# driver.quit()
#
# # book counting
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login_name = driver.find_element_by_id("username")
# login_name.send_keys("snooper743@gmail.com")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("Rexxar09051945")
# login_btn = driver.find_element_by_css_selector("#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button")
# login_btn.click()
# shop_btn = driver.find_element_by_link_text("Shop")
# shop_btn.click()
# html_btn = driver.find_element_by_link_text("HTML")
# html_btn.click()
# book_count = driver.find_elements_by_class_name("product")
# if len(book_count) == 3:
#     print("В разделе 3 товара")
# else:
#     print(f"В разделе", len(book_count), "товара")
# driver.quit()
#
# # Sorting
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login_name = driver.find_element_by_id("username")
# login_name.send_keys("snooper743@gmail.com")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("Rexxar09051945")
# login_btn = driver.find_element_by_css_selector("#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button")
# login_btn.click()
# shop_btn = driver.find_element_by_link_text("Shop")
# shop_btn.click()
# element = driver.find_element_by_class_name("orderby")
# element_check = element.get_attribute("value")
# assert element_check == "menu_order"
# select = Select(element)
# select.select_by_value("price-desc")
# element = driver.find_element_by_class_name("orderby")
# element_check = element.get_attribute("value")
# assert element_check == "price-desc"
# driver.quit()
#
# # Price test

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
book_btn = driver.find_element_by_class_name("post-169")
book_btn.click()
old_price = driver.find_element_by_css_selector("del span")
old_price_txt = old_price.text
assert old_price_txt == "₹600.00"
new_price = driver.find_element_by_css_selector("ins span")
new_price_txt = new_price.text
assert new_price_txt == "₹450.00"
image_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")) )
image_btn.click()
close_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) )
close_btn.click()
driver.quit()