# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:56:58 2020

@author: Abinash Satapathy
"""

import csv
import matplotlib.pyplot as plt
year = []
WO = []

with open("istherecorrelation.csv") as input:
    a = csv.reader(input, delimiter=';')
    next(a)
    for row in a:
        year.append(int(row[0]))
        WO.append(float(row[1].replace(",","."))*1000)

image = plt.figure()

plt.plot(year, WO, "b-", label="Number of WO students")
plt.ylabel("Number of students")
plt.xlabel("Year")
plt.title("Correlation between the students in Netherlands and beer consumption plot")

plt.savefig('plot.png', format='png', dpi=300)