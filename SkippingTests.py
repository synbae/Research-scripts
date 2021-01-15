import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search test")

    @unittest.skip("Skipping because incomplete")
    def test_advancedSearch(self):
        print("This is Advanced Search method")

    @unittest.skipIf(1==1,'Because one equals one, dummy')
    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge test")

    def test_loginByGmail(self):
        print("This is login by Gmail")

    def test_loginByTwitter(self):
        print("This is login by Twitter")


if __name__ == '__main__':
    unittest.main()