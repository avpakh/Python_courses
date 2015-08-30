# -*- coding: utf-8 -*-
import logging
LOG = logging.getLogger(__name__)


class FlatManagementError(Exception):
    pass

import os
import subprocess
import re
import commands

"""
Class of flat description
"""

class MyApp(object):
    def __init__(self,square,price,room_n,wallmat,consdate,sun_side):
        self.square = square 
        self.price = price
        self.room_n = room_n
        self.wallmat = wallmat
        self.consdate = consdate
        self.sun_side  = sun_side
    def __eq__(self, other):
        return  self.price/self.square == other.price/other.square
    def __lt__(self, other):
        return  self.price/self.square < other.price/other.square
    def __gt__(self, other):
        return  self.price/self.square >= other.price/other.square
    #def __setattr__(self, room_n, value):
    #    if self.room_n == value:
    #        self.room_n = value
    #def __setattr__(self, price, value):
    #   if self.price > 0:
    #   self.price = value

class Cond(object):
    def __init__(self):
        self.flats = []

    def add_flat(self,fl):
        self.flats.append(fl)
        pass
    """
    Sort by sq m  from higher prices to lower 
    """    
    def sorting (self):
       flat_list=sorted(self.flats, reverse=True)
       return flat_list
            
     



r = Cond()

app1 = MyApp(30,50000,1,'brick',1980,0)
app2 = MyApp(40,60000,1,'brick',1990,0)
app3 = MyApp(60,70000,2,'wood',1960,0)
app4 = MyApp(55,70000,2,'panel',1960,0)
app5 = MyApp(70,70000,3,'panel',1960,0)

r.add_flat(app1)
r.add_flat(app2)
r.add_flat(app3)
r.add_flat(app4)
r.add_flat(app5)


tt = r.sorting()

for ii in tt:
    print ii.price , ii.square , ii.price/ii.square , ii.wallmat

   
