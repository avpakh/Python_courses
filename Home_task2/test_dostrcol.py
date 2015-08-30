# -*- coding: cp1251 -*-
import os ,sys, fnmatch
import dostrcol
import unittest 

class Testroots(unittest.TestCase):
    def setUP(self):
        pass
    
    def tearDown(self):
        reload(dostrcol)

    def test_init(self):
        html = dostrcol.roots('"/home/alex/Sources/Projects"')
        self.assertEqual(html.path,'"/home/alex/Sources/Projects"')

             

if __name__ == '__main__':
    suite = []
    suite.append(unittest.TestLoader().loadTestsFromTestCase(Testroots))
    test_suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
