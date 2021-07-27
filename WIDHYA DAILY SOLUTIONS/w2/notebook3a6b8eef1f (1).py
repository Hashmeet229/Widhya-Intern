#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 5GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv("../input/rcb-vs-kkr/deliveries.csv")
df.head()
df.info()
import os
print(os.listdir("../input"))


# In[2]:


a= df[['bowling_team','batting_team','noball_runs']]
b=a[(a['bowling_team']=='Royal Challengers Bangalore') & (a['batting_team'] == 'Kolkata Knight Riders') ]
b


# In[3]:


c= df[['bowling_team','batting_team','noball_runs']]
d=c[(c['bowling_team']=='Kolkata Knight Riders') & (c['batting_team'] == 'Royal Challengers Bangalore') ]
d


# In[4]:


e = pd.concat([b,d], axis=0)
e


# In[5]:


f=e.groupby('bowling_team').agg({'noball_runs':'sum'})
f


# In[ ]:


#total_noballs=14+9=23 AND total matches b/w these two are 24..
total_noballs=23
total_macthes_vs_kkr=24
noball_per_match=total_noballs/total_macthes_vs_kkr
noball_per_match


# In[6]:


df1=pd.read_csv("../input/rcb-vs-kkr/matches.csv")
df1.info()


# In[7]:


df2=df1[['team1','team2','winner','result','toss_winner','toss_decision']]
df2.head()


# In[8]:


df3 = df2[(df2['team1']=='Royal Challengers Bangalore') & (df2['team2'] == 'Kolkata Knight Riders')]
df3


# In[9]:


df4 = df2[(df2['team1']=='Kolkata Knight Riders') & (df2['team2'] == 'Royal Challengers Bangalore')]

df4 


# In[10]:


df5 = pd.concat([df3,df4], axis=0)
df5


# In[11]:


df5['winner'].value_counts()


# In[12]:


df5['toss_decision'].value_counts()


# In[13]:


matches_played=pd.concat([df1['team1'],df1['team2']])
matches_played=matches_played.value_counts().reset_index()
matches_played.columns=['Team','Total Matches']
matches_played['wins']=df1['winner'].value_counts().reset_index()['winner']

matches_played.set_index('Team',inplace=True)
matches_played.reset_index().head(8)


# In[14]:


win_percentage = round(matches_played['wins']/matches_played['Total Matches'],3)*100
win_percentage.head(8)


# In[15]:


df6= df[['bowling_team','batsman','batsman_runs','match_id']]
df6.head()

df7=df6[(df6['bowling_team']=='Royal Challengers Bangalore') & (df6['batsman'] == 'KD Karthik')]
df7['match_id'].value_counts()


# In[16]:


df8=df7.groupby('batsman').agg({'batsman_runs':'sum'})
df8.div(20)


# In[17]:



df11=df6[(df6['bowling_team']=='Kolkata Knight Riders') & (df6['batsman'] == 'V Kohli')]
df11


# In[18]:


df12=df11.groupby('batsman').agg({'batsman_runs':'sum'})
df11['match_id'].value_counts()
df12.div(24)


# In[24]:


df13= df[['batsman','batsman_runs','match_id','bowling_team']]
df13.head()

df14=df13[(df13['batsman'] == 'V Kohli') & (df13['batsman_runs'] == 4) & (df13['bowling_team'] == 'Kolkata Knight Riders')]
df14


# In[26]:


no_of_matches=df14['match_id'].value_counts()
no_of_matches


# In[29]:


#from above data summing all the values in match_id.Since each match_id represents no. of fours in that match.So after summing up ..
total_fours=58
total_macthes_vs_kkr=24
four_per_match=total_fours/total_macthes_vs_kkr
four_per_match

