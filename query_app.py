#!/usr/bin/env python
# coding: utf-8

# In[2]:

import csv
import components
from components import hostid_search,location_search,ptp_search,review_search,opening_file
def app(path_file,csv_file):
    try:
        while   True:
            
            host_id=input("enter host id")
            
            if host_id:
                hostid_search(host_id,csv_file)
            #input("enter location")
            host_location=input("enter host location")
            if host_location:
                location_search(host_location,csv_file)
            else:
                print(f"not a valid {host_location}")
            #input("enter property type")
            ptp_type=input("enter type of property to search for room type, accommodates, bathrooms_text,bedrooms, beds")
            if ptp_type:
                ptp_search(csv_file,ptp_type)
            #input("enter a location to see review details")
            R=input("enter the location to search for review details there: ")
            if host_location:
                review_search(csv_file,R)
    except Exception as e:
        print(f"{e}enter correct details")
