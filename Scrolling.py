from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='./Drivers/chromedriver/chromedriver')

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# scroll by Pixel
# driver.execute_script("window.scrollBy(0,1000)","")

# Scroll by element
# flag = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
# driver.execute_script("arguments[0].scrollIntoView();", flag)

# Scroll till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


time.sleep(5)
driver.close()