from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

cdriver = webdriver.Chrome(executable_path='./Drivers/chromedriver/chromedriver')
# fdriver = webdriver.Firefox(executable_path='./Drivers/geckodriver/geckodriver')

cdriver.get('https://medium.com/')
# fdriver.get('https://github.com/')

cdriver.get('https://github.com/')
print(cdriver.title)
print(cdriver.current_url)

cdriver.back()
cdriver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div/div/div[3]/span[1]/div/div/h4/a').click()

time.sleep(5)

print(cdriver.title)
print(cdriver.current_url)
# print(fdriver.title)

cdriver.close()
# fdriver.close()