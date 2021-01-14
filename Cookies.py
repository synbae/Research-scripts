from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")
driver.get("https://www.amazon.in/")
driver.maximize_window()

cookies = driver.get_cookies()
print("Number of Cookies created: " + str(len(cookies)))

for var in cookies:
   for var1 in var:
       print(var1, var[var1])

cookie = {'name': 'MyCookie', 'value': '1234567890'}
driver.add_cookie(cookie)

for var in driver.get_cookies():
   for var1 in var:
       print(var1, var[var1])

print("Number of new cookies: ",len(driver.get_cookies()))

driver.delete_cookie('MyCookie')

print("Number of new new cookies: ",len(driver.get_cookies()))

driver.delete_all_cookies()

print("Number of new new new cookies: ",len(driver.get_cookies()))

time.sleep(3)
driver.close()