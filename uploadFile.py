from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

driver.switch_to.frame("frame-one1434677811")

tar = driver.find_element(By.ID, "RESULT_FileUpload-10")
driver.execute_script("arguments[0].scrollIntoView();", tar)

tar.send_keys("/home/synbae/PycharmProjects/Research scripts/Files/EmptyTXTFile.txt")

time.sleep(3)
driver.close()