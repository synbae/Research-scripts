from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {'download.default_directory': '/home/synbae/PycharmProjects/Research scripts/Files'})

driver = webdriver.Chrome(executable_path='./Drivers/chromedriver/chromedriver', chrome_options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element(By.ID, "textbox").send_keys("Testing Text")
driver.find_element(By.ID, "createTxt").click()
time.sleep(3)
driver.find_element(By.ID, "link-to-download").click()

driver.find_element(By.ID, "pdfbox").send_keys("Testing PDF")
driver.find_element(By.ID, "createPdf").click()
time.sleep(3)
driver.find_element(By.ID, "pdf-link-to-download").click()

time.sleep(3)
driver.close()