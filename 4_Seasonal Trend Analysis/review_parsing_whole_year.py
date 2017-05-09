# -*- coding: utf-8 -*-
"""
Created on Sat May  6 14:13:59 2017

@author: Mohammad
"""


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
    return reviewDateTime.timetuple().tm_yday
    
    

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
         #if index == 90:
          #  break
         #print(reviewedD =ay)
         
print(index)  
businessID = remove_duplicates(businessID)      


index = 0
w, h = 735, 150000;
Matrix = [[0 for x in range(w)] for y in range(h)]         

for id in businessID:    
    for info in parseInfo:
        if (id == info[0]):
            for i in range(366):
                if(info[1] == i):
                    Matrix[index][i] = Matrix[index][i]+1
                    Matrix[index][i+1]=Matrix[index][i+1]+info[2]


    
    index = index +1

    
    
    

def getTotalReviewCount(index):
    totalReviewcnt = 0
    for i in range (0,730):
       if(i%2== 0):
           totalReviewcnt = totalReviewcnt + Matrix[index][i]
    return totalReviewcnt;    
    
def getTotalScore(index):
    totalScore = 0
    for i in range (0,730):
       if(i%2 != 0):
           totalScore = totalScore + Matrix[index][i]
    return totalScore;
    
    
def getDailyBasisScore(index):
    
    totCnt = getTotalReviewCount(index)
    totScore = getTotalScore(index)
    #print(totCnt)
    #print(totScore)
    dailyScores = []    
    for i in range (0,730,2):
           score = (Matrix[index][i]/totCnt) * (Matrix[index][i+1]/totScore)
           dailyScores.append(score)
    return dailyScores;
    
    
    
target = open('feature_signal.txt', 'w')
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