# assertGreater
# assertGreater verifies whether first value is greater than second value

# assertGreaterEqual
# assertGreaterEqual verifies whether first value is greater or equal to second element

# assertLess
# assertLess verifies whether first parameter is lesser than second parameter

# assertLessEqual
# assertLessEqual verifies whether first parameter is lesser or equal to second parameter

import unittest


class Test(unittest.TestCase):

    def testName1(self):
        var1 = 20
        var2 = 10

        self.assertGreater(var1, var2)

    def testName2(self):
        var1 = 10
        var2 = 10

        self.assertGreaterEqual(var1, var2)

    def testName3(self):
        var1 = 10
        var2 = 20

        self.assertLess(var1, var2)

    def testName4(self):
        var1 = 10
        var2 = 10

        self.assertLessEqual(var1, var2)


if __name__ == '__main__':
    unittest.main()