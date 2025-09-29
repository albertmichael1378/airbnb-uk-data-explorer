#!/usr/bin/env python
# coding: utf-8

# In[2]:

import csv
from components import hostid_search,location_search,ptp_search,review_search

print("path read")
def app(csv_file):
    try:
        
        print("file is opened")
        host_id=input("enter host id")
        hostid_search(host_id,csv_file)
        #input("enter location")
        location_search(csv_file)
        #input("enter property type")
        ptp_search(csv_file)
        #input("enter a location to see review details")
        review_search(csv_file)
    except:
        print("enter correct details")
        app(csv_file)
