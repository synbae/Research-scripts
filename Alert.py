from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")

elem = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button")

elem.click()

time.sleep(5)

elem = driver.switch_to.alert
# elem.accept()
elem.dismiss()

time.sleep(5)

driver.close()