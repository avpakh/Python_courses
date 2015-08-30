# -*- coding: cp1251 -*-
import unittest
import infosys



class TestsysInfo(unittest.TestCase):

    def setUP(self):
        pass
    
    def tearDown(self):
        reload(infosys)

    def test_init(self):
        info = infosys.sysInfo()
                     

if __name__ == '__main__':
    suite = []
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestsysInfo))
    test_suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=2).run(test_suite)




    
    
