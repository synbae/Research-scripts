# when we have only two parameter we can use assertEqual method to check whether both are same
# or not, but if we have more than two parameters, comparing values with assertEqual method
# become more difficult

# assertTrue
# assertTrue method checks whether given parameter is true or not, if value is true then test
# is passed otherwise test is failed

# assertFalse
# assertFalse method compares whether given value or expression results in false or not
# If the result or value is False then unittest passes the testcase but if the result or
# value is True then unittest fails the test case.

import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def testNAME1(self):
        driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")
        driver.get("https:/www.google.com/")
        titleWP = driver.title

        self.assertTrue(titleWP == 'Google')

    def testNAME2(self):
        driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")
        driver.get("https:/www.google.com/")
        titleWP = driver.title

        self.assertFalse(titleWP == 'Google1')


if __name__ == '__main__':
    unittest.main()