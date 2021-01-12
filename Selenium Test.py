from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

cdriver = webdriver.Chrome(executable_path='./Drivers/chromedriver/chromedriver')
# fdriver = webdriver.Firefox(executable_path='./Drivers/geckodriver/geckodriver')

cdriver.get('https://medium.com/')
# fdriver.get('https://github.com/')

# cdriver.get('https://github.com/')
# print(cdriver.title)
# print(cdriver.current_url)

# cdriver.back()
cdriver.find_element_by_xpath("//*[@id='top-nav-sign-in-cta-desktop']/div/h4/span/a").click()
cdriver.find_element_by_id("email-susi-button-text").click()
# ele = cdriver.find_element_by_xpath("//*[@id='susi-modal-background']/div/div/div[3]/div/div[1]/div/div/div[2]/div/h4/input")
# ele = cdriver.find_element_by_class_name("vi")
ele = cdriver.find_element_by_css_selector("input")
ele.send_keys('synbae.rks@gmail.com')
cdriver.fin
# cdriver.find_element_by_xpath("//*[@id='susi-modal-background']/div/div/div[3]/div/div[2]/button").click()
time.sleep(5)

print(cdriver.title)
print(cdriver.current_url)
# print(fdriver.title)

cdriver.close()
# fdriver.close()