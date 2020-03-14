# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:28:46 2020

@author: AMD
"""

def fibo_position(n):
  t1 = 0
  t2 = 1
  while(n-2 != 0):
      t3 = t1 + t2
      t1 = t2
      t2 = t3
  print (t3)
   
fibo_position(4)
