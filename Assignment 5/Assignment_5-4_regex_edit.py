# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 12:56:48 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import re

dollarsFirst = re.compile(r'\$([0-9]+(\.[0-9]{2})?)([a-zA-Z\s]+)([0-9]{1,2})')
membersFirst = re.compile(r'(^\D*)([0-9]{1,2})([a-zA-Z\s]*)\$?([0-9]+\.([0-9]{0,2}))([^\$\d]*$)')


with open('contribs.txt', 'r') as f:
    contents = f.readlines()

    memberContrib = {}
    lineCount = 0

    for line in contents:
        lineCount += 1
        if dollarsFirst.search(line) is not None:
            memberContrib[dollarsFirst.search(line).group(4)] = float(dollarsFirst.search(line).group(1))
        elif membersFirst.search(line) is not None:
            memberContrib[membersFirst.search(line).group(2)] = float(membersFirst.search(line).group(4))
        else:
            print(f'Line {lineCount} is ill formed: {line.strip()}')

total = 0.0
contributions = list(memberContrib.values())
members = list(memberContrib.keys())
max_contribution = max(contributions)
max_member = members[contributions.index(max_contribution)]

print("member | Contribution")
print("-"*22)
for k, v in memberContrib.items():
    total += v
    print(f'   {k:2}  | ${v:.2f}')

print(f"Contributions total ${total}")
print(f"Member {max_member} contributed the most, ${max_contribution}.")
