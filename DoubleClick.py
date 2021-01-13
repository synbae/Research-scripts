from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")

driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()

element = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button")

action = ActionChains(driver)

action.double_click(element).perform()

time.sleep(3)
driver.close()