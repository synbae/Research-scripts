from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='./Drivers/chromedriver/chromedriver')
driver.get('http://demo.guru99.com/test/newtours/')
driver.maximize_window()

# driver.save_screenshot("./Files/ScreenS.png")

driver.get_screenshot_as_file('./Files/ScreenS1.jpg')

time.sleep(3)
driver.close()