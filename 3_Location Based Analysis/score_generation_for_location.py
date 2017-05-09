# -*- coding: utf-8 -*-
"""
Created on Sat May  6 09:20:20 2017

@author: Mohammad
"""


import numpy as np
import csv
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from collections import Counter

def read_data(filename):
    csvf = open(filename,'rU')
    rows = csv.reader(csvf)
    data = [row for row in rows]
    csvf.close()
    return data

location_data= read_data('location_data_with_ids.csv')
location_score_data = read_data('score_data_location.csv')



target = open('feature_location_calculation.txt', 'w')
indx = 0
for bis_id in location_data:
    for review_bis_id in location_score_data:
        if(bis_id[0] == review_bis_id[0]):
            target.write(bis_id[1]+ " " + bis_id[2] + " ")
            for val in review_bis_id :                        
                target.write(val+ " ")
            target.write("\n")
   # print(id)
    #print(getDailyBasisScore(indx))
    #print("-----------------------------------------------------")    
                            
target.close()