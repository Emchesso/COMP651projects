# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 21:51:05 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import sqlite3
import csv

conn = sqlite3.connect('test.db')
# conn = sqlite3.connect(':memory:')

c = conn.cursor()
sql_command = """
                CREATE TABLE horse_table (
                name text,
                age integer
                );"""

c.execute(sql_command)

horse_dict = {}
with open('data.txt', 'r') as f:
    horse_reader = csv.reader(f, delimiter = " ")
    for row in horse_reader:
        horse_dict.update({row[0]:int(row[2])})

sql_command2 = """
INSERT INTO horse_table (name, age)
VALUES (?, ?);"""  

for k, v in horse_dict.items():
    c.execute(sql_command2, (k,v))

conn.commit()

conn.close()
