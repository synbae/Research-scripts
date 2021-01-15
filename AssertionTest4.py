# assertIn
# assertIn method verifies whether the first element is present in the second element, if
# first element is present in second element then tests passed otherwise test is failed

# assertNotIn
# assertNotIn method verifies whether the first element is not present in the second element
# or not, if first element is present then test will be failed otherwise test is passed.

# These two methods will be helpful when you want to verify presence of a value in a list,
# tuple, set, and dictionary

import unittest


class Test(unittest.TestCase):

    def testNAME1(self):
        list1 = ['python', 'jave', 'c++']

        self.assertIn('python', list1)

    def testNAME2(self):
        list2 = ['python', 'jave', 'c++']

        self.assertNotIn('javascript', list2)


if __name__ == '__main__':
    unittest.main()