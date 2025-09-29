
import csv


import csv
from tkinter import Tk, filedialog
import csv

def opening_file():
    while True:
        try:
            path_file = input("Enter the file path: ")
            csv_file = open(path_file, errors="ignore")
            print(f"csv file {csv_file} opened from { path_file} using file opener")
            return path_file,csv_file
        except FileNotFoundError:
            print("File not found — please enter a correct file path.")
        except Exception as e:
            print("Unexpected error:", str(e))

def hostid_search(host_id,csv_file):
    try:
        csv_file.seek(0)
        countable=[]
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:

            if host_id==row[0]:
                countable.append(host_id)
                print (f"{row[1]}")
                print(f" Host Description:  {row[2]},")
                print(f" Host Name:         {row[3]},")
                print(f" Host Location:     {row[5]}, ")
                print(f" host since:        {row[4]}" )
        if len(countable)==0:
            print("entered id is invalid please run again")
    #         f=input("enter continue other search")
    #         if f==continue_other_search:
    #             break
    #         else:
    except Exception as e:
        print({e})
    

def location_search(host_location,csv_file):
    print("resetting pointer and creating csv reader")
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file)
    
    countable2=[]
    for row in csv_reader:
        if host_location in {row[5]}:
            print(row)
            countable2.append(host_location)
            print(f":{row[3]},")
            print(f"     {row[13]}, {row[20]},{row[21]},{row[22]}")
    if len(countable2)==0:
           print ("entered location is not valid")
def ptp_search(csv_file,ptp_type):
    countable3=[]
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if ptp_type in row[13]:
            countable3.append(ptp_type)
            print(f" Data showing  room type, accommodates, bathrooms_text, bedrooms and  beds for {ptp_type} properties")
            print(f"{row[14:18]}  ")
    if len(countable3)==0:
            print("enter correct type of property")
def review_search(csv_file,R):
    print(f" Data showing review score rating, review score accuracy and review score cleanlines for Location {R}")
    print("review score rating  review score accuracy  review score cleanliness")
    csv_file.seek(0)
    countable4=[]
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if R in row[5]:
            countable4.append(R)
            print(f"{row[27]},                        {row[28]},                 {row[29]}")
    if len(countable4)==0:
        print("enter correct host location")            






def TKINTER_file_OPENER():
    while True:
        
          # hide the small Tk window
        path_file = filedialog.askopenfilename(
            title="Select a CSV file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )

        if not path_file:
            print("No file selected. Please try again.")
            continue  # loop back to ask again

        try:
            csv_file = open(path_file, errors="ignore")
            csv_reader = csv.reader(csv_file)
            return csv_reader, path_file, csv_file
        except Exception as e:
            print(str(e) + " — please select a correct file.")

def oldopening_file():
    while True:
        try:
            path_file = input("Enter the file path: ")
            # Open and read inside try
            csv_file = open(path_file, errors="ignore")
            csv_reader = csv.reader(csv_file)
            return csv_reader, path_file, csv_file  # return file handle too
        except Exception as e:
            print(f"{str(e)} — please enter a correct file path.") #str(e)-jupyter notebook can crash when it try to show exception, without str