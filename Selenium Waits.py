from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./Drivers/chromedriver/chromedriver')

driver.get('https://deelay.me/10000/medium.com')

try:
    ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div[4]/div[3]/div/div/div/div[2]/div/div[1]/div[3]/a/h4")))

finally:
    driver.quit()