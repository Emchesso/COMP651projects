# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 20:20:04 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

sql_command = """
                SELECT name, age
                FROM horse_table
                WHERE age
                BETWEEN ? AND ?;"""

c.execute(sql_command, (8,12))
print(c.fetchall())

conn.commit()

conn.close()
