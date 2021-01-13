from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.maximize_window()

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium.cli").click()

time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("CliCommand.Executable").click()

time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("classFrame")
driver.find_element_by_link_text("DEPRECATED").click()

time.sleep(3)

driver.close()