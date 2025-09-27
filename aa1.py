# coding: utf-8



import csv
print("path read")
def app(path_file):
    try:
        
        
        host_id=input("enter host id")
        hostid_search(path_file, host_id)
        
        #input("enter location")
        location_search()
        #input("enter property type")
        ptp_search()
        #input("enter a location to see review details")
        review_search()
    except:
        print("enter correct details")
        
def hostid_search(path_file,host_id):
    print("id search is started)")
    try:
        with open(path_file,errors="ignore") as csv_file:
            print("id search is started)")
            csv_reader=csv.reader(csv_file)
            print("file is working")
            countable=[]
            for row in csv_reader:
                print(host_id)
                if host_id==row[0]:
                    print(host_id)
                    countable.append(host_id)
                    print (f"{row[1]}")
                    print(f" Host Description:  {row[2]},")
                    print(f" Host Name:         {row[3]},")
                    print(f" Host Location:     {row[5]}, ")
                    print(f" host since:        {row[4]}" )
            if len(countable)==0:
                print("entered id is invalid please run again")
                f=input("enter continue other search")
                if f==continue_other_search:
                    print("start again")
    except:
        print("enter correct file path")

def location_search():
    with open("./Airbnb_UK_2022.csv",errors="ignore") as csv_file:
        csv_reader=csv.reader(csv_file)
        host_location=input("enter host location")
        countable2=[]
        for row in csv_reader:
            if host_location in row[5]:
                countable2.append(host_location)
                print(f":{row[3]},")
                print(f"     {row[13]}, {row[20]},{row[21]},{row[22]}")
        if len(countable2)==0:
               print ("entered location is not valid")
def ptp_search():
    with open("./Airbnb_UK_2022.csv",errors="ignore") as csv_file:
        csv_reader=csv.reader(csv_file)
        j=input("enter type of property to search for room type, accommodates, bathrooms_text,bedrooms, beds")
        countable3=[]
        for row in csv_reader:
            if j in row[13]:
                countable3.append(j)
                print(f"{row[14:18]}  ")
        if len(countable3)==0:
                print("enter correct type of property")
def review_search():
    with open("./Airbnb_UK_2022.csv",errors="ignore") as csv_file:
        csv_reader=csv.reader(csv_file)
        host_location=input("enter the location to search for review details there: ")
        print("review score rating  review score accuracy  review score cleanliness")
        countable4=[]
        for row in csv_reader:
            if host_location in row[5]:
                countable4.append(host_location)
                print(f"{row[27]},                        {row[28]},                 {row[29]}")
        if len(countable4)==0:
            print("enter correct host location")            


# In[ ]:




