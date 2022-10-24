# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:58:34 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""
from typing import List

def add_increment(ls: List[int]) -> List[int]:
    return [x+increment for x in ls]

increment = 5
ls = [1,2,3,4,5,6]
print(add_increment(ls))
