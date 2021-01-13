from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

elem_rome = driver.find_element(By.ID, "box6")
elem_madrid = driver.find_element(By.ID, "box7")
elem_oslo = driver.find_element(By.ID, "box1")
elem_copenhagen = driver.find_element(By.ID, "box4")
elem_seoul = driver.find_element(By.ID, "box5")
elem_stockholm = driver.find_element(By.ID, "box2")
elem_washington = driver.find_element(By.ID, "box3")

elem_italy = driver.find_element(By.ID, "box106")
elem_spain = driver.find_element(By.ID, "box107")
elem_norway = driver.find_element(By.ID, "box101")
elem_denmark = driver.find_element(By.ID, "box104")
elem_south_korea = driver.find_element(By.ID, "box105")
elem_sweden = driver.find_element(By.ID, "box102")
elem_united_states = driver.find_element(By.ID, "box103")

action = ActionChains(driver)

action.drag_and_drop(elem_rome, elem_italy)
action.drag_and_drop(elem_madrid, elem_spain)
action.drag_and_drop(elem_oslo, elem_norway)
action.drag_and_drop(elem_copenhagen, elem_denmark)
action.drag_and_drop(elem_seoul, elem_south_korea)
action.drag_and_drop(elem_stockholm, elem_sweden)
action.drag_and_drop(elem_washington, elem_united_states).perform()

time.sleep(3)
driver.close()