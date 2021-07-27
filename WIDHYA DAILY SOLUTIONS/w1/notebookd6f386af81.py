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


# In[68]:


import pandas as pd
import numpy as np
df=pd.read_csv("../input/match-prediction-mi-vs-dc/deliveries.csv")
df.head()
df.info()


# In[92]:


a= df[['bowling_team','batting_team','wide_runs']]
b=a[(a['bowling_team']=='Delhi Daredevils') & (a['batting_team'] == 'Mumbai Indians') ]
b


# In[93]:


c= df[['bowling_team','batting_team','wide_runs']]
d=c[(c['bowling_team']=='Mumbai Indians') & (c['batting_team'] == 'Delhi Daredevils') ]
d


# In[94]:


e = pd.concat([b,d], axis=0)
e


# In[97]:


f=e.groupby('bowling_team').agg({'wide_runs':'sum'})
f.div(22)


# In[114]:


g= df[['bowler','player_dismissed','batting_team','match_id']]
h=g[(g['bowler']=='K Rabada') & (g['batting_team']=='Mumbai Indians')]
h


# In[115]:


h['match_id'].value_counts()


# In[ ]:


h['player_dismissed'].value_counts()


# In[71]:


df1=pd.read_csv("../input/match-prediction-mi-vs-dc/matches.csv")
df1.info()


# In[72]:


df2=df1[['team1','team2','winner','result','toss_winner','toss_decision']]
df2.head()


# In[73]:


df3 = df2[(df2['team1']=='Mumbai Indians') & (df2['team2'] == 'Delhi Daredevils')]
df3


# In[74]:


df4 = df2[(df2['team1']=='Delhi Daredevils') & (df2['team2'] == 'Mumbai Indians')]

df4 


# In[75]:


df5 = pd.concat([df3,df4], axis=0)
df5


# In[76]:


df5['winner'].value_counts()


# In[77]:


df5['toss_decision'].value_counts()


# In[78]:


matches_played=pd.concat([df1['team1'],df1['team2']])
matches_played=matches_played.value_counts().reset_index()
matches_played.columns=['Team','Total Matches']
matches_played['wins']=df1['winner'].value_counts().reset_index()['winner']

matches_played.set_index('Team',inplace=True)
matches_played.reset_index().head(8)


# In[79]:


win_percentage = round(matches_played['wins']/matches_played['Total Matches'],3)*100
win_percentage.head(8)


# In[80]:


df6= df[['bowling_team','batsman','batsman_runs']]
df6.head()

df7=df6[(df6['bowling_team']=='Delhi Daredevils') & (df6['batsman'] == 'RG Sharma') ]
df7


# In[82]:


df8=df7.groupby('batsman').agg({'batsman_runs':'sum'})
df8.div(22)


# In[ ]:





# In[ ]:




