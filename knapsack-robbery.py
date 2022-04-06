# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:06:30 2022

@author: Adrián
"""

#Knapsack problem / robbery

class Loot:
    def __init__(self, weight, value):
        self.weight=weight
        self.value=value


weight_limit=14
item_ratio=""

dirt = Loot(4,0)
computer = Loot(10,30)
fork = Loot(5,1)
pSet = Loot(0,-10)

#Provides the ratio value/weight for passed obj
def method1(item):
    if item.weight==0:
        return 0
    else:
        return item.value/item.weight

def method2(item):
    return -item.weight

def method3(item):
    return item.value
    