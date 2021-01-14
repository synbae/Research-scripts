from selenium import webdriver
from selenium.webdriver.common.by import By
import time

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "/home/synbae/PycharmProjects/Research scripts/Files")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(executable_path="./Drivers/geckodriver/geckodriver", firefox_profile=fp)
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