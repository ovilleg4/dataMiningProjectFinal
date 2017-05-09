# -*- coding: utf-8 -*-
"""
Created on Sat May  6 23:55:27 2017

@author: Mohammad
"""

import csv
def read_data(filename):
    csvf = open(filename,'rU')
    rows = csv.reader(csvf)
    data = [row for row in rows]
    csvf.close()
    return data

data= read_data('singal_cluster_day_score.csv')




target = open('weekly_score.txt', 'w')
for i in range(0,7):
    index = 0
    score = 0.0
    for j in range(0,365):
        index = index + 1
        score = score + float( data[i][j])
        if index%7 == 0 :
            val_to_str = "%.9f " % score
            target.write(val_to_str)
            score = 0.0
    target.write("\n")
   # print(id)
    #print(getDailyBasisScore(indx))
    #print("-----------------------------------------------------")    
    #indx = indx + 1
target.close()