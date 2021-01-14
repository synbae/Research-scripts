import unittest

# will be executed before executing any class or any method present in the test class
def setUpModule():
    print('setUpModule')

# will be executed after completing everything present in the python module
def tearDownModule():
    print('tearDownModule')


class AppTesting(unittest.TestCase):

    # This will execute once at the start of the class
    @classmethod
    def setUpClass(cls):
        print("BEGIN")

    # This will execute once at the start of every method
    @classmethod
    def setUp(self):
        print("This is login test")

    def test_Search(self):
        print("This is search test")

    def test_AdvancedSearch(self):
        print("This is Advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge test")

    # This will execute once at the end of every method
    @classmethod
    def tearDown(self):
        print("this is logout test")

    # This will execute once at the end of the class
    @classmethod
    def tearDownClass(cls):
        print("END ")


if __name__ == '__main__':
    unittest.main()
