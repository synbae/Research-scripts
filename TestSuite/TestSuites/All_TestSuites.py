import unittest
from TestSuite.Package1.TC_loginTest import LoginTest
from TestSuite.Package1.TC_SignupTest import SignupTest
from TestSuite.Package2.TC_PaymentTest import PaymentTest
from TestSuite.Package2.TC_PaymentReturns import PaymentReturnsTest

# Loading Tests
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating Suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])
functionalTestSuite = unittest.TestSuite([tc3, tc4])
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])

# Running Suites
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)