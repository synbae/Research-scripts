from selenium import webdriver

driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")

driver.get("file:///home/synbae/PycharmProjects/Research%20scripts/Files/DocChiDat.html")

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
col = len(driver.find_elements_by_xpath("/html/body/table/thead/tr/th"))

print(rows, col)

for a in range(1,col+1):
    elem1 = driver.find_element_by_xpath("/html/body/table/thead/tr/th["+str(a)+"]").text
    print(elem1,end=' ')

for r in range(1,rows+1):
    for c in range(1,col+1):
        elem = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(elem,end=' ')
    print()


driver.close()