#!/usr/bin/env python
# coding: utf-8

# # Data Sructures

# In[1]:


#List -can have duplicate
L=[1,2,'name',8.4,2]
#tuple-can have duplicate
T=(1,2,'name',8.4,2)
#Set- remove duplicates also saes the element in any order
S={1,2,'name',8.4,2}
#Dictonary
D={"a":1,3:2,"val":'name',67:8.4,"xyz":2}


# In[3]:


print("Type of L is:" ,type(L))
print("Type of T is:" ,type(T))
print("Type of S is:" ,type(S))
print("Type of D is:" ,type(D))


# In[5]:


print(L)
print(T)
print(S)
print(D)


# In[7]:


print(L[1])
print(T[2])
print(3 in S)
print(D[67])
print(D['xyz'])


# In[8]:


L[1:3] #same as string start from index 1 and end at 3


# In[9]:


L[::-1]


# In[10]:


L[:4:2]


# In[11]:


L=L+["How","are","you"]


# In[12]:


L


# In[13]:


L.append(6.98)


# In[14]:


L


# In[21]:


L.append(T)


# In[22]:


L


# In[40]:


T2=('a','b',100)
T=T+T2   #was run twice so appened 2 times

T3=(767676,'tfcggh')
T+=T3


# In[45]:


T


# In[44]:


T[12]


# In[27]:


S.add(200)


# In[28]:


S


# In[30]:


S.update({600,1000,"echo"})


# In[31]:


S


# In[32]:


S.update({600,1000,"echo"}) #will not insert duplicate


# In[48]:


S.remove(600)
print(S)


# In[35]:


D['Newkey']="NewValue"


# In[36]:


D


# In[37]:


D2={'y':"YY",'z':89909}


# In[39]:


D=D+D2


# In[46]:


del D[3]


# In[47]:


D


# In[49]:


D2={'A':L,'B':T,'C':S,'D':D}


# In[50]:


D2.items()


# In[52]:


D2['A']


# In[53]:


D2['A'][3]


# In[57]:


D2['A'][10]


# In[58]:


D2['A'][10][2]


# In[59]:


L5=[L,T,D,23,'hundred']


# In[60]:


type(L5[2])


# In[61]:


L4=[x**2 for x in range(10)]


# In[62]:


L4


# In[63]:


S4={x**2 for x in range(2,20,3)}


# In[64]:


S4


# # Pandas

# In[65]:


import pandas as pd


# In[67]:


data=pd.Series([0.25,0.76,0.67,1.0],index=['a','b','c','d']) # we can create our own index in pandas by deault from 0,1,2...


# In[68]:


data.values


# In[69]:


type(data)


# In[70]:


type(data.values)


# In[71]:


data.index


# In[72]:


print(pd.__version__)


# In[73]:


data['a']


# In[74]:


data['a','b'] # can access only 1 obj at a time


# In[75]:


data['a':'c'] #here the last index is also included unlike arrays


# In[76]:


grd_dict={'A':4,'-A':3.5,'B':3,'-B':2.5,'C':2} #1st define dict and then pass t series
grades=pd.Series(grd_dict)


# In[78]:


grades


# In[103]:


mrk_dict={'A':90,'A1':85,'B':80,'1B':75,'C1':70} #1st define dict and then pass t series
marks=pd.Series(mrk_dict)
mrk_dict1={'A':90,'-A':85,'B':80,'-B':75,'C':70} #1st define dict and then pass t series
marks1=pd.Series(mrk_dict1)


# In[96]:


marks


# In[97]:


marks[0:2] #explicit index will not include last value


# In[98]:


D=pd.DataFrame({'Marks':marks,'Grades':grades})


# In[99]:


D #NaN= Not a number


# In[106]:


D.T


# In[104]:


D1=pd.DataFrame({'Marks':marks1,'Grades':grades})


# In[105]:


D1


# In[107]:


D1.T


# In[108]:


D1.values


# In[110]:


D1.values[2,0]


# In[111]:


D1.values[3,1]


# In[112]:


D.columns


# In[116]:


D1['ScaledMarks']=100*(D1['Marks']/90) #add new column in the data


# In[117]:


D1


# In[118]:


del D1['ScaledMarks']


# In[119]:


D1


# In[124]:


G=D1[D1['Marks']>80]


# In[125]:


G


# In[130]:


T=pd.DataFrame([{'a':1,'b':2},{'b':-3,'c':9}])


# In[131]:


T


# In[133]:


T.fillna(0)


# In[135]:


get_ipython().run_line_magic('pinfo', 'T.dropna')


# In[136]:


T.dropna


# In[137]:


T


# In[143]:


data1=pd.Series(['a1','b1','c1'],index=[1,3,5])


# In[144]:


data1


# In[145]:


data1[1]


# In[146]:


data1[1:3]


# In[147]:


data1.loc[1:3]


# In[148]:


data1.iloc[1:3]


# In[149]:


D1.iloc[2,:]


# In[150]:


D1


# In[151]:


D1.loc[2,:] ## error bcoz it is not haing explicit index as 2


# In[152]:


from sklearn.impute import SimpleImputer


# In[178]:


df=pd.read_csv('E:\covid_19.csv')


# In[179]:


df.head()


# In[155]:


df.head(10)


# In[181]:


df.drop(['Lat','Long'],axis=1,inplace=True) #Axis is do it in column 
# inplace will stort the return in df if not written then will retuen in default variable '_' or some other variable give in df it self


# In[182]:


df.head(10) #Lat and Long deleted


# In[183]:


df.rename(columns={'Province/State':'Province','Country/Region':'Country'},inplace=True)


# In[184]:


df.head()


# In[185]:


df['Date']=pd.to_datetime(df['Date']) # it was in panda format so no changes seen


# In[186]:


df.head()


# In[187]:


df.describe()


# In[164]:


df.info()


# In[189]:


df.fillna('NA') #will fill NAN with NUll


# In[175]:


#imputer=SimpleImputer(strategy='constant')
#df2=pd.DataFrame(imputer.fit_transform(df),column=df.column)


# In[190]:


df.head()


# In[192]:


df2=df.groupby('Country')[['Confirmed','Deaths','Recovered']].sum().reset_index()


# In[193]:


df2


# In[198]:


df3=df.groupby(['Country','Date'])[['Confirmed','Deaths','Recovered']].sum().reset_index()


# In[199]:


df3


# In[200]:


df4=df3[df3['Confirmed']>100]


# In[201]:


df4


# # Matpotlib

# In[204]:


import matplotlib.pyplot as plt
#from matplot import pyplot as plt
import numpy as np


# In[206]:


x=np.linspace(0,10,1000)
y=np.sin(x)
plt.plot(x,y)


# In[209]:


plt.scatter(x[::10],y[::10],color='yellow')


# In[210]:


plt.plot(x,y,color='red')
plt.plot(x,np.cos(x),color='g')# or green


# In[211]:


plt.plot(x,x,+0,'b')#Blue


# In[212]:


plt.plot(x,x,+1,'--c')#dashed cyan


# In[215]:


plt.plot(x,x,+2,'-.k')#dashed black


# In[216]:


plt.plot(x,x,+3,':r')#dotted red


# In[217]:


## Practice back on file
countries = df3['Country'].unique()
len(countries)


# In[218]:


countries


# In[219]:


for idx in range(0,len(countries)):    
    C = df3[df3['Country']==countries[idx]].reset_index()        
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
    plt.title(countries[idx])
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of cases')
    plt.legend() 
    plt.show()    


# In[221]:


df4 = df3.groupby(['Date'])[['Confirmed','Deaths','Recovered']].sum().reset_index()


# In[222]:


C = df4
plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
plt.title('World')
plt.xlabel('Days since the first suspect')
plt.ylabel('Number of cases')
plt.legend()
plt.show()


# In[ ]:




