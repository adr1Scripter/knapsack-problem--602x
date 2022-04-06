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
        
    def ratio(self):
        if item.weight==0:
            item.weight=0.01
        return self.value/self.weight

#constraint
weight_limit=14
item_ratio=""

dirt = Loot(4,0)
computer = Loot(10,30)
fork = Loot(5,1)
pSet = Loot(0,-10)
phone = Loot(3, 20)
noodles = Loot(1, 4)
'''
3 approaches to compare to what degree they make meaningful choices
'''

#Provides the ratio value/weight for passed obj
def runRatio(item):
    return round(item.ratio(), 2)
#heavier items for last places of the ordering, lighter first
def runWeight(item):
    return -(item.weight)
#More expensive items come first
def runValue(item):
    return item.value

for item in len(items):
'''
To be finished
'''
    
