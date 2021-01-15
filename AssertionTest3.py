# assertIsNone
# assertIsNone method verifies whether give values or expression results in None or not,
# if the result is none then python unittest will pass the test case otherwise fails the
# testcase.

# assertIsNotNone
# assertIsNotNone method verifies whether give values is not None, if the value is None then
# the test case will be failed


import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def testName1(self):
        driver = None


        self.assertIsNone(driver)

    def testName2(self):
        driver = webdriver.Chrome("./Drivers/chromedriver/chromedriver")

        self.assertIsNotNone(driver)


if __name__ == '__main__':
    unittest.main()