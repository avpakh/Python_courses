# -*- coding: cp1251 -*-
import os
import subprocess
import re
import commands
import unittest
import zo


class TestAviary(unittest.TestCase):

    def setUP(self):
        pass
    
    def tearDown(self):
        reload(zo)

    def test_init(self):
        aviary = zo.Aviary('Lions','Venom')

        self.assertEqual(aviary.name,'Lions')
        self.assertEqual(aviary._type,'Venom')

    def test_get_aviary_count(self):
        aviary1 = zo.Aviary ('Lions','Venom')
        aviary2 = zo.Aviary ('Tigers','Venom')
        aviary3 = zo.Aviary ('Zebras','Herbivore')
        aviary4 = zo.Aviary ('Elepants','Herbivore')
        self.assertEqual(zo.Aviary.get_aviary_count(), 4)
        

class TestVenom(unittest.TestCase):

    def setUP(self):
        pass
    
    def tearDown(self):
        reload(zo)
  
    def test_init(self):
        animal = zo.Venom('Chucha','degu','3','F')
        self.assertEqual(animal.name,'Chucha')
        self.assertEqual(animal.sex,'F')
        self.assertEqual(animal.age,'3')
        self.assertEqual(animal.spe,'degu')

    def test_get_type(self):
        animal = zo.Venom('Chucha','degu','3','F')
        result = animal.get_type()
        self.assertEqual(result,'Venom')
        


if __name__ == '__main__':
    suite = []
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestVenom))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestAviary))
    test_suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=2).run(test_suite)

    

   


