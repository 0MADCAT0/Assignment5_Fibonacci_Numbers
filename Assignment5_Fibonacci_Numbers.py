# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:04:08 2020

@author: MADCAT
"""


def fibonacci(num):
    ara = [1]
    i = num
    y=1
    x=0
    c=0
    while i > 0 and c != num:
        c=x+y
        ara.append(c)
        x, y = y, c
        i -=1
        
    return  print(ara) 

num = 55
fibonacci(num)