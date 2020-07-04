import unittest
import json
import os
from datetime import datetime
import ea_genetic

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUp(self):
        pass

    def test_8queens(self):
        result = ea_genetic.main()
        print (result)
       # self.assertTrue(os.path.isfile("8queens.output"))
        self.assertIsNone(result)
      #  response = ea_genetic.solve_8queens()
        #self.assertTrue(os.path.isfile("8queens.output")
        
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()