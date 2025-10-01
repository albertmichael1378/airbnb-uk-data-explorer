#!/usr/bin/env python
# coding: utf-8

# In[2]:

import csv
import components
from components import hostid_search,location_search,ptp_search,review_search,opening_file
def app(path_file,csv_file,a):
    try:
        exit_outer_loop=False
        while True:
            if exit_outer_loop:
                break

            host_id=input("enter host id")
            if host_id.lower()=="back":
                exit_outer_loop=True
                break
            while True:
                if host_id.lower()=="back":
                    
                    break
                if host_id:
                    if host_id!='next' and host_id!='Next':
                        host_id=hostid_search(host_id,csv_file)
                        if host_id:
                            break
                    else:
                        break       
                else:
                    host_id=input("Your input is empty, please enter a valid host id or enter next or enter back to open data visualization")
            #input("enter location")
            if exit_outer_loop:
                break
            while True:
                
                host_location=input("enter host location, ente back for Data visualization")
                if host_location:
                    if host_location!='back' and host_location!='Back':
                        location_search(host_location,csv_file)
                        break
                    else:
                        exit_outer_loop=True
                        break
                else:
                    print("Host location cannot be empty. Please try again.")
            
            if exit_outer_loop:
                break
            #input("enter property type")
            ptp_type=input("enter type of property to search for room type, accommodates, bathrooms_text,bedrooms, beds or enter back to data visualization part")
            while True:
                
                if ptp_type.lower()=='back':
                    exit_outer_loop=True
                    break
                elif ptp_type.lower()==next:
                    break
                elif ptp_type:
                    ptp_type=ptp_search(csv_file,ptp_type)
                    
                    if ptp_type:
                        break
                    else:
                        ptp_type=input("enter type of property to search for room type, accommodates, bathrooms_text,bedrooms, beds or enter back to data visualization part")
                        
            if exit_outer_loop:
                break
          
            #input("enter a location to see review details")
            while True:
                
                R=input("enter the location to search for review details there or enter 'back' to got to data visualization session: ")
                if R:
                    if R.lower()=='back':
                        exit_outer_loop=True
                        break
                    else:
                        review_search(csv_file,R)
                else:
                    print(f"Your input is empty, enter correct details")
                    
            if exit_outer_loop==True:
                break
    except Exception as e:
        print(f"{e}enter correct details")
