from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from selenium import webdriver

# title check

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

# book counting

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
html_btn = driver.find_element_by_link_text("HTML")
html_btn.click()
book_count = driver.find_elements_by_class_name("product")
if len(book_count) == 3:
    print("В разделе 3 товара")
else:
    print(f"В разделе", len(book_count), "товара")
driver.quit()

# Sorting

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
element = driver.find_element_by_class_name("orderby")
element_check = element.get_attribute("value")
assert element_check == "menu_order"
select = Select(element)
select.select_by_value("price-desc")
element = driver.find_element_by_class_name("orderby")
element_check = element.get_attribute("value")
assert element_check == "price-desc"
driver.quit()

# Price test

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

# Cart price, subtotal, total

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("https://practice.automationtesting.in/")
shop_btn = driver.find_element_by_link_text("Shop")
shop_btn.click()
add_btn = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]')
add_btn.click()
time.sleep(1)
cartcontents = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
cartcontents_txt = cartcontents.text
assert cartcontents_txt == "1 Item"
amount = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
amount_txt = amount.text
assert amount_txt == "₹180.00"
basket = driver.find_element_by_link_text("View Basket")
basket.click()
subtotal= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount.amount"), "₹180.00"))
total = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount.amount"), "₹183.60"))
driver.quit()

# Cart work

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("https://practice.automationtesting.in/")
shop_btn = driver.find_element_by_link_text("Shop")
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
add_1_btn = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]')
add_1_btn.click()
time.sleep(1)
add_2_btn = driver.find_element_by_xpath('//*[@id="content"]/ul/li[6]/a[2]')
add_2_btn.click()
basket = driver.find_element_by_link_text("View Basket")
basket.click()
time.sleep(1)
first_remove = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-remove > a")
first_remove.click()
undo = driver.find_element_by_link_text("Undo?")
undo.click()
time.sleep(1)
quantity = driver.find_element_by_xpath("//tr[1]/td[5]/div/input")
quantity.clear()
quantity.send_keys("3")
update_basket = driver.find_element_by_css_selector(".actions > .button")
update_basket.click()
quantity_value = quantity.get_attribute("value")
assert quantity_value == "3"
time.sleep(1)
apply_coupon = driver.find_element_by_css_selector(".coupon > .button")
apply_coupon.click()
coupon_error = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error > li"), "Please enter a coupon code."))
driver.quit()

# Place order

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("https://practice.automationtesting.in/")
shop_btn = driver.find_element_by_link_text("Shop")
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
add_1_btn = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]')
add_1_btn.click()
basket = driver.find_element_by_link_text("View Basket")
basket.click()
time.sleep(1)
proceed = driver.find_element_by_css_selector(".wc-proceed-to-checkout > a")
proceed.click()
first_name = driver.find_element_by_id('billing_first_name')
first_name.send_keys('Sergey')
last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('Perminov')
email = driver.find_element_by_id('billing_email')
email.send_keys('Snooper743@gmail.com')
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('+71234567890')
address_1 = driver.find_element_by_id('billing_address_1')
address_1.send_keys('Whasington str')
city = driver.find_element_by_id('billing_city')
city.send_keys('Whasington')
postcode = driver.find_element_by_id('billing_postcode')
postcode.send_keys('32458')
country_select = driver.find_element_by_id('s2id_billing_country')
country_select.click()
search_country = driver.find_element_by_id('s2id_autogen1_search')
search_country.send_keys('Iceland')
select2 = driver.find_element_by_class_name('select2-match')
select2.click()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)
option = driver.find_element_by_id("payment_method_cheque")
option.click()
place_order = driver.find_element_by_id('place_order')
place_order.click()
thanks= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
check_payments= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))
driver.quit()