# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:35:04 2017

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

raw_data= read_data('location_data.csv')

#X, labels_true = make_blobs(n_samples=750, centers=data, cluster_std=0.4,
    #                        random_state=0)

#X = StandardScaler().fit_transform(X)
db = DBSCAN(eps= .024, min_samples=80).fit(raw_data)
labels =db.labels_ 
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print(n_clusters_)
print(len(labels))


#for lb in labels:
 #  print(lb)
 
 

target = open('labels.txt', 'w')
indx = 0
for id in labels:
    val_to_str = "%d " % id
    target.write(val_to_str)
    target.write("\n")
   # print(id)
    #print(getDailyBasisScore(indx))
    #print("-----------------------------------------------------")    
    #indx = indx + 1
target.close()


data= read_data('location_score.csv')

w, h = 7, 9;
clus_score_matrix = [[0.0 for x in range(w)] for y in range(h)]

cnt_items_clus_0 = 0
cnt_items_clus_1 = 0
cnt_items_clus_2 = 0
cnt_items_clus_3 = 0
cnt_items_clus_4 = 0
cnt_items_clus_5 = 0
cnt_items_clus_6 = 0
cnt_items_clus_7 = 0
cnt_items_clus_8 = 0
cnt_items_clus_9 = 0
def add_vector( v1,v2):
    for i in range (0,7):
        v1[i] = float(v2[i]) +v1[i]
    return v1
                      
def set_cluster_base_score():
    index = 0
    
    global cnt_items_clus_0 
    global cnt_items_clus_1 
    global cnt_items_clus_2 
    global cnt_items_clus_3 
    global cnt_items_clus_4
    global cnt_items_clus_5 
    global cnt_items_clus_6 
    global cnt_items_clus_7 
    global cnt_items_clus_8
    global cnt_items_clus_9
    for i in labels:
        if i == 0:
            tmpSum = add_vector(clus_score_matrix[0], data[index])
            clus_score_matrix[0]= tmpSum
            cnt_items_clus_0 = cnt_items_clus_0 + 1
            #print(tmpSum)
        elif i == 1:
            tmpSum = add_vector(clus_score_matrix[1], data[index])
            clus_score_matrix[1] = tmpSum
            cnt_items_clus_1 = cnt_items_clus_1 + 1
            #print(tmpSum)
        elif i == 2:
            tmpSum = add_vector(clus_score_matrix[2], data[index])
            clus_score_matrix[2] = tmpSum
            cnt_items_clus_2 = cnt_items_clus_2 + 1
            #print(tmpSum)            
        elif i == 3:
            tmpSum = add_vector(clus_score_matrix[3], data[index])
            clus_score_matrix[3] = tmpSum
            cnt_items_clus_3 = cnt_items_clus_3 + 1
            #print(tmpSum)
        elif i == 4:
            tmpSum = add_vector(clus_score_matrix[4], data[index])
            clus_score_matrix[4] = tmpSum
            cnt_items_clus_4 = cnt_items_clus_4 + 1
            #print(tmpSum)
        elif i == 5:
            tmpSum = add_vector(clus_score_matrix[5], data[index])
            clus_score_matrix[5] = tmpSum
            cnt_items_clus_5 = cnt_items_clus_5 + 1
            #print(tmpSum)
        elif i == 6:
            tmpSum = add_vector(clus_score_matrix[6], data[index])
            clus_score_matrix[6] = tmpSum
            cnt_items_clus_6 =cnt_items_clus_6 + 1
        
        elif i == 7:
            tmpSum = add_vector(clus_score_matrix[7], data[index])
            clus_score_matrix[7] = tmpSum
            cnt_items_clus_7 =cnt_items_clus_7 + 1
       
        else:
            tmpSum = add_vector(clus_score_matrix[8], data[index])
            clus_score_matrix[8] = tmpSum
            cnt_items_clus_8 =cnt_items_clus_8 + 1
       # else:
        #    cnt_items_clus_9 =cnt_items_clus_9 + 1
            #print(tmpSum)
        index = index + 1
    return
                      
set_cluster_base_score()

#print(clus_score_matrix)

    
    
#plot_cluster(data,7)    



print(cnt_items_clus_0)
print(cnt_items_clus_1)
print(cnt_items_clus_2)
print(cnt_items_clus_3)
print(cnt_items_clus_4)
print(cnt_items_clus_5)
print(cnt_items_clus_6)
print(cnt_items_clus_7)
print(cnt_items_clus_8)
#print(cnt_items_clus_9)



 
target = open('clusters_point_dbscan.txt', 'w')
indx = 0
for i in range(0,9):
    for j in range( 0,7):
        val = 0
        if(i == 0):
            val = clus_score_matrix[i][j]/cnt_items_clus_0

        elif(i == 1):
            val = clus_score_matrix[i][j]/cnt_items_clus_1

        elif(i == 2):
            val = clus_score_matrix[i][j]/cnt_items_clus_2
        
        elif(i == 3):
            val = clus_score_matrix[i][j]/cnt_items_clus_3

        elif(i == 4):
            val = clus_score_matrix[i][j]/cnt_items_clus_4

        elif(i == 5):
            val = clus_score_matrix[i][j]/cnt_items_clus_5
        
        else:
            val = clus_score_matrix[i][j]/cnt_items_clus_6

        val_to_str = "%.9f " % val
        target.write(val_to_str)
    target.write("\n")    
    indx = indx + 1
target.close()