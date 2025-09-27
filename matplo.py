#!/usr/bin/env python
# coding: utf-8

# In[78]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plot_frame=pd.read_csv("./Airbnb_UK_2022.csv",encoding='Latin-1',header=0)
def pie_chart_illustratiion():
    list_bed_frequency=plot_frame["bedrooms"].value_counts().tolist()
    unique_number_beds=sorted(plot_frame["bedrooms"].unique().tolist())

    print(unique_number_beds)
    number_of_beds=[1,2,3,4,5,6,7,10]
    print(list_bed_frequency)
    print(unique_number_beds)
    fig=plt.figure(figsize=(17,7))
    plt.pie(list_bed_frequency,labels=number_of_beds, autopct='%7.1f%%')
    plt.title("number of people choosed a particular number of bed fro_m total people")
    plt.legend()
    plt.show()
def Bar_chart_illustration():
    variable=plot_frame.groupby('room_type')
    m=variable.size()
    height=m.tolist()
    g=m.index.tolist()
    print(height)
    print(m)
    fig=plt.figure(figsize=(7,27))
    plt.bar(g, height, label="number of listing" )
    plt.title("number of listing for each room type")
    plt.xlabel("room_type")
    plt.ylabel("number_of_listing")
    plt.legend()
def scatter_plot_illustration():
    scatter_variable_x=plot_frame['accommodates'].tolist()
    scatter_variable_y=plot_frame['price'].tolist()
    mean_price=plot_frame.groupby('accommodates')['price'].mean()
    print(mean_price)
    y=mean_price.tolist()
    x=mean_price.index.tolist()
    fig=plt.figure()
    plt.scatter(scatter_variable_x,scatter_variable_y,marker='o',s=27)

    plt.title('accommodates_price_relationship')
    plt.ylabel('price')
    plt.xlabel('accommodates')
    plt.show()
    print("this diagram is not very clear, so we plot the relationship between number of accomodates and mean price")
    plt.scatter(x,y,marker='D',s=5)
    plt.title('accommodates_and_avearge_price_relationship')
    plt.xlabel('number_of_accommodates')
    plt.ylabel('avearge_price')
def line_graph_illustration():
    fig,(ax1,ax2,ax3,)=plt.subplots(3,1,figsize=(7,17))
    plot_frame['host_since']=pd.to_datetime(plot_frame['host_since'])
    to_2020=plot_frame.query("host_since>='1/1/2019' and host_since<='1/1/2020'")
    to_2021=plot_frame.query("host_since>='1/1/2020' and host_since<='1/1/2021'")
    to_2022=plot_frame.query("host_since>='1/1/2021' and host_since<='1/1/2022'")
    og=to_2020.groupby(to_2020.host_since.dt.month)['price'].mean()
    ogm=og.index.tolist()
    ogp=og.tolist()
    o1=to_2021.groupby(to_2021.host_since.dt.month)['price'].mean()
    og1=o1.index.tolist()
    ogp1=o1.tolist()
    o2=to_2022.groupby(to_2022.host_since.dt.month)['price'].mean()
    og2=o2.index.tolist()
    ogp2=o2.tolist()
    
    ax1.plot(ogm,ogp,color='blue')
    ax2.plot(og1,ogp1,color='yellow')
    ax3.plot(og2,ogp2,color='green')
    ax1.set (title= "Air bnb prices from 2019 to 2020",  xlabel='mean price',ylabel='months')
    ax2.set (title= "Air bnb prices from 2020 to 2021",  xlabel='mean price',ylabel='months')
    ax3.set (title= "Air bnb prices from 2021 to 2022",  xlabel='mean price',ylabel='months ')        
    plt.show
def linegraph_yr():
    fig,axs=plt.subplots(1,1,figsize=(7,7))
    plot_frame['host_since']=pd.to_datetime(plot_frame['host_since'])
    price_per=plot_frame.groupby(plot_frame.host_since.dt.year)
    year=price_per.size()
    years=year.index.tolist()
    print(price_per)
    mean_price=price_per['price'].mean().tolist()
    to_2022=plot_frame.query("host_since>='1/1/2019' and host_since<='1/1/2022'")
    # xl=to_2022['price'].mean().tolist()
    # yl=to_2022['host_since'].mean().tolist()
    axs.plot(years,mean_price,color='yellow')
    axs.set_xlabel('mean price',fontsize=17)
    axs.set_ylabel('years',fontsize=27)
    axs.set_title("Air bnb prices from 2019 to 2022", fontsize=17)
    plt.show


# In[35]:



    #group_by_bedrooms=plot_frame.groupby('bedrooms')


# In[36]:





# In[37]:





# In[76]:



# print(og1)
# print(ogp1)

# ax1.plot(ogm,ogp,color='blue')
# ax2.plot(og1,ogp1,color='yellow')
# ax3.plot(og2,ogp2,color='green')
# ax1.set (title= "Air bnb prices from 2019 to 2020",  xlabel='mean price',ylabel='months')
# ax2.set (title= "Air bnb prices from 2020 to 2021",  xlabel='mean price',ylabel='months')
# ax3.set (title= "Air bnb prices from 2021 to 2022",  xlabel='mean price',ylabel='months ')        
# plt.show


    
    


# In[ ]:


# ax1.set_xlabel('mean price',fontsize=17)
# ax1.set_ylabel('months',fontsize=14)
# ax1.set_title("Air bnb prices from 2019 to 2020", fontsize=17)

# ax2.set_xlabel('mean price',fontsize=17)
# ax2.set_ylabel('months',fontsize=14)
# ax2.set_title("Air bnb prices from 2020 to 2021", fontsize=17)

# ax3.set_xlabel('mean price',fontsize=17)
# ax3.set_ylabel('months',fontsize=17)
# ax3.set_title("Air bnb prices from 2021 to 2022", fontsize=17)


# In[ ]:





# In[ ]:




