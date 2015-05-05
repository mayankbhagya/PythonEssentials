class MathOperations(object):
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b


#testcases, fixtures, testsuites, testrunners

import unittest
class MyTests(unittest.TestCase):
    def setUp(self):
        #print "Setting up"
        self.m = MathOperations()
     
    def tearDown(self):
        #print "Tearing down"
        del self.m
         
    def test_addition(self):
        #print "Addition test"
        self.assertEqual(self.m.add(10, 20), 30, "Addition")
 
    def test_subtraction(self):
        #print "Subtraction test"
        self.assertEqual(self.m.subtract(20, 10), 10, "Subtraction")


#unittest.main()


suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
unittest.TextTestRunner(verbosity=2).run(suite)

