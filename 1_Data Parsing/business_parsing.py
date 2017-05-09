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

# Open a JSON file from the dataset and read data line-by-line iteratively
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
               if tmp[i] == 'Restaurants' or tmp[i] == 'Food':
                   #s print("Test")
                   restaurant_IDS.append(data['business_id'])
                   
                  
                    
                   
                   


#for index in restaurant_IDS:
 #   print(index)
         