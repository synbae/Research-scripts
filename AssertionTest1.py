# Assertion is nothing but the checkpoint or you can say it as verification for the test case
# to evaluate some item on the execution.

# If we do not provide any assertion  inside a test case then there is no way to know whether
# a test case is failed or not.

# Assertion helps in report generation, based on the assertions the test execution report will
# be generated.

# There are few assertion which will accept all the values and few assertions will accept only
# numeric values.

# assertEqual
# assertEqual compare the first parameter with the second parameter, if both matches the
# unittest will continue with the remaining execution but the both the values are different
# then unit test fails the testcase.

# assertNotEqual
# assertNotEqual method compares the given two parameters, if both parameter are not same
# then unittest passes the test case but if both parameter are same then unittest fails
# the test case

import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def testNameEQ(self):
        driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")
        driver.get("https://www.google.com/")
        titleWebPage = driver.title

        self.assertEqual("Google", titleWebPage, "webpage title is not same")

    def testNameNEQ(self):
        driver = webdriver.Chrome(executable_path="./Drivers/chromedriver/chromedriver")
        driver.get("https://www.google.com/")
        titleWebPage = driver.title

        self.assertNotEqual("Google1", titleWebPage, "webpage title is same")


if __name__ == '__main__':
    unittest.main()