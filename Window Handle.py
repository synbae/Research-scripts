from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./Drivers/chromedriver/chromedriver')

driver.get('http://demo.automationtesting.in/Windows.html')

driver.find_element(By.LINK_TEXT, 'click').click()

print(driver.current_window_handle)

wh = driver.window_handles

for var in wh:
    driver.switch_to.window(var)
    print(driver.title)

driver.quit()

