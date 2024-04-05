'''
unit testing - enhetstesting

ref:
https://realpython.com/python-testing/#testing-your-code
https://docs.python.org/3/library/unittest.html
'''

import unittest

#source: https://realpython.com/python-testing/#choosing-a-test-runner
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
    
    