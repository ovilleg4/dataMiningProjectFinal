# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:57:43 2017

@author: Mohammad
"""


# Import Python's default JSON encoder and decoder
import json

# Initialize an empty list for temporarily holding a JSON object
data = []

restaurant_IDS = []
business_id = []

# Open a JSON file from the dataset and read data line-by-line iteratively
already_added = set();
with open('yelp_academic_dataset_business.json', encoding='utf8') as fileobject:
	for line in fileobject:
         data = json.loads(line)
         #print(data['business_id'])
         #print(data['review_count'])
         #print(data['stars'])
         #print(data['longitude'])
         #print(data['latitude'])
         #print(data)
         tmp = []
         length = 0
         tmp = data['categories']
         if tmp is None or len(tmp) == 0:
             length = 0
         else:
             length = len(tmp)
                 
         if data['state'] == 'AZ':
             for i in range(0,length):
               if (tmp[i] == 'Restaurants' or tmp[i] == 'Food') and data['business_id'] not in already_added:
                   #s print("Test")
                    already_added.add(data['business_id']) # for duplicatate remove
                    tmpList = []
                    tmpList.append(data['business_id'])
                    tmpList.append(data['longitude'])
                    tmpList.append(data['latitude'])
                    restaurant_IDS.append(tmpList)
                    business_id.append(data['business_id'])
             #else:
                  # print("Already in List")
                    
                   
                   

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
    
#restaurant_IDS = remove_duplicates(restaurant_IDS)

#for index in restaurant_IDS:
#    print(index)
target = open('location.txt', 'w')
indx = 0
for id in restaurant_IDS:
    for val in id :
        if isinstance(val , str):
            val_to_str = val + " "
        else : 
            val_to_str = "%.9f " % val
        target.write(val_to_str)
    target.write("\n")
   # print(id)
    #print(getDailyBasisScore(indx))
    #print("-----------------------------------------------------")    
    indx = indx + 1
target.close()