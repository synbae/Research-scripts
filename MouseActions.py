from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")

driver.get('https://opensource-demo.orangehrmlive.com')

driver.maximize_window()

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

admin = driver.find_element(By.ID, "menu_admin_viewAdminModule")
UM = driver.find_element(By.ID, "menu_admin_UserManagement")
Us = driver.find_element(By.ID, "menu_admin_viewSystemUsers")

actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(UM).move_to_element(Us).click().perform()

time.sleep(3)
driver.close()

