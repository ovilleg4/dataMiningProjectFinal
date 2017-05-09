# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:22:44 2017

@author: Mohammad
"""
# Import Psycopg Postgres adapter for Python
#import psycopg2

# Import Python's default JSON encoder and decoder
import json
import datetime
from business_parsing import restaurant_IDS 

# Initialize an empty list for temporarily holding a JSON object
#print(restaurant_IDS)
data = []

def getDay( reviewDate):
    tmpDate = reviewDate.split('-', 2) 
    yr = int(tmpDate[0])
    mm = int(tmpDate[1])
    dd = int(tmpDate[2])
    reviewDateTime = datetime.datetime(yr, mm, dd, 0, 0, 0, 0)
    return reviewDateTime.weekday();


def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output
    
    
#print(getDay("2016-08-01"))

unique_resturant_ID = remove_duplicates(restaurant_IDS)
parseInfo = []
businessID = []
# Open a JSON file from the dataset and read data line-by-line iteratively
index  = 0
with open('yelp_academic_dataset_review.json', encoding='utf8') as fileobject:
	for line in fileobject:
         data = json.loads(line)
         
        # print(data['business_id'])
         #print(data['review_id'])
         #print(data['date'])
        # print(data['stars'])
        # print(data)
         for resid in unique_resturant_ID:
             if resid == data['business_id']:
                 tmpList = []
                 reviewedDay = getDay(data['date'])
                 businessID.append(data['business_id'])
                 tmpList.append(data['business_id'])
                 tmpList.append(reviewedDay)
                 tmpList.append(data['stars'])
                 parseInfo.append(tmpList)
                 index = index + 1
         if index == 9000:
            break
         #print(reviewedD =ay)
         
  
businessID = remove_duplicates(businessID)         
#print(len(businessID))

monday = 0
tuesday = 1
wednesday = 2
thursday = 3
friday = 4
satday = 5
sunday = 6


#inf0[0] == businessID
#inf0[1] == day
#inf0[2] == star

dayWiseReviewStatus = []

index = 0
w, h = 15, 150000;
Matrix = [[0 for x in range(w)] for y in range(h)]         

for id in businessID:
    satReviewCnt = 0
    sunReviewCnt = 0
    monReviewCnt =0
    tuesReviewCnt =0
    wedReviewCnt =0
    trReviewCnt =0
    friReviewCnt =0

    satTotScore =0
    sunTotScore = 0
    monTotScore = 0
    tuesTotScore = 0
    wedTotScore = 0
    trTotScore =0
    friTotScore = 0
    
    for info in parseInfo:
        if (id == info[0]):
            if(info[1] == monday):
                monReviewCnt = monReviewCnt+1
                monTotScore =monTotScore+info[2]

            elif(info[1] == tuesday):
                tuesReviewCnt = tuesReviewCnt+1
                tuesTotScore =tuesTotScore+info[2]

            elif(info[1] == wednesday):
                wedReviewCnt = wedReviewCnt+1
                wedTotScore =wedTotScore+info[2]

            elif(info[1] == thursday):
                trReviewCnt = trReviewCnt+1
                trTotScore =trTotScore+info[2]
        
            elif(info[1] == friday):
                friReviewCnt = friReviewCnt+1
                friTotScore =friTotScore+info[2]
        
            elif(info[1] == satday):
                satReviewCnt = satReviewCnt+1
                satTotScore =satTotScore+info[2]
            
            else:
                sunReviewCnt = sunReviewCnt+1
                sunTotScore =sunTotScore+info[2]
    
    Matrix[index][0] = monReviewCnt
    Matrix[index][1] = monTotScore   
    Matrix[index][2] = tuesReviewCnt
    Matrix[index][3] = tuesTotScore
    Matrix[index][4] = wedReviewCnt
    Matrix[index][5] = wedTotScore
    Matrix[index][6] = trReviewCnt
    Matrix[index][7] = trTotScore   
    Matrix[index][8] = friReviewCnt
    Matrix[index][9] = friTotScore
    Matrix[index][10] = satReviewCnt
    Matrix[index][11] = satTotScore 
    Matrix[index][12] = sunReviewCnt
    Matrix[index][13] = sunTotScore
    
    index = index +1
    
    
    
          
#print(Matrix)


def getTotalReviewCount(index):
    totalReviewcnt = 0
    for i in range (0,14):
       if(i%2== 0):
           totalReviewcnt = totalReviewcnt + Matrix[index][i]
    return totalReviewcnt;
    
    

def getTotalScore(index):
    totalScore = 0
    for i in range (0,14):
       if(i%2 != 0):
           totalScore = totalScore + Matrix[index][i]
    return totalScore;
    
    
def getDailyBasisScore(index):
    
    totCnt = getTotalReviewCount(index)
    totScore = getTotalScore(index)
    #print(totCnt)
    #print(totScore)
    dailyScores = []    
    for i in range (0,14,2):
           score = (Matrix[index][i]/totCnt) * (Matrix[index][i+1]/totScore)
           dailyScores.append(score)
    return dailyScores;
    
    
    
target = open('output.txt', 'w')
indx = 0
for id in businessID:
    score = getDailyBasisScore(indx)
    for val in score :
        val_to_str = "%.9f " % val
        target.write(val_to_str)
    target.write("\n")
    print(id)
    #print(getDailyBasisScore(indx))
    print("-----------------------------------------------------")    
    indx = indx + 1
target.close()