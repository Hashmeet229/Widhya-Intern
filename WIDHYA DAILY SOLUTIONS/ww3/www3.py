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
df=pd.read_csv("../input/csk-vs-srh/deliveries.csv")
df.head()
df.info()
import os
print(os.listdir("../input"))


# In[24]:


a= df[['bowling_team','batting_team','wide_runs']]
b=a[(a['bowling_team']=='Sunrisers Hyderabad') & (a['batting_team'] == 'Chennai Super Kings') & (a['wide_runs'] == 1) ]
b


# In[25]:


c= df[['bowling_team','batting_team','wide_runs']]
d=c[(c['bowling_team']=='Chennai Super Kings') & (c['batting_team'] == 'Sunrisers Hyderabad') & (a['wide_runs'] == 1)]
d


# In[28]:


e = pd.concat([b,d], axis=0)
e


# In[30]:


f=e.groupby('bowling_team').agg({'wide_runs':'sum'})
f


# In[17]:


#total_wides=51+34=85 and total_matches_csk_vs_srh=12...
total_matches_csk_vs_srh=12
total_wides=85
wides_per_match=total_wides/total_matches_csk_vs_srh

wides_per_match


# In[5]:


df1=pd.read_csv("../input/csk-vs-srh/matches.csv")
df1.info()


# In[6]:


df2=df1[['team1','team2','winner','result','toss_winner','toss_decision']]
df2.head()


# In[7]:


df3 = df2[(df2['team1']=='Chennai Super Kings') & (df2['team2'] == 'Sunrisers Hyderabad')]
df3


# In[8]:


df4 = df2[(df2['team1']=='Sunrisers Hyderabad') & (df2['team2'] == 'Chennai Super Kings')]

df4 


# In[9]:


df5 = pd.concat([df3,df4], axis=0)
df5


# In[10]:


df5['winner'].value_counts()


# In[11]:


matches_played=pd.concat([df1['team1'],df1['team2']])
matches_played=matches_played.value_counts().reset_index()
matches_played.columns=['Team','Total Matches']
matches_played['wins']=df1['winner'].value_counts().reset_index()['winner']

matches_played.set_index('Team',inplace=True)
matches_played.reset_index().head(8)


# In[12]:


win_percentage = round(matches_played['wins']/matches_played['Total Matches'],3)*100
win_percentage.head(8)


# In[13]:


df6= df[['bowling_team','batsman','batsman_runs','match_id']]
df6.head()
df7=df6[(df6['bowling_team']=='Chennai Super Kings') & (df6['batsman'] == 'DA Warner')]
df7


# In[14]:


df7['match_id'].value_counts()


# In[15]:


df8=df7.groupby('batsman').agg({'batsman_runs':'sum'})
df8


# In[16]:


runs_against_csk=448
total_matches_for_warner_against_csk=14
run_per_match=runs_against_csk/total_matches_for_warner_against_csk
run_per_match


# In[50]:


i= df[['bowling_team','batting_team','player_dismissed']]
j=i[(i['bowling_team']=='Sunrisers Hyderabad') & (i['batting_team'] == 'Chennai Super Kings')]
j


# In[51]:


j['player_dismissed'].value_counts()


# In[53]:


#from above total players dismissed of csk vs srh=50
wickets_per_match=50/total_matches_csk_vs_srh
wickets_per_match


# In[55]:


w= df[['bowling_team','batting_team','total_runs']]
v=w[(w['bowling_team']=='Chennai Super Kings') & (w['batting_team'] == 'Sunrisers Hyderabad')]
v


# In[57]:


y=w[(w['bowling_team']=='Sunrisers Hyderabad') & (w['batting_team'] == 'Chennai Super Kings')]
y


# In[59]:


z = pd.concat([v,y], axis=0)
z


# In[61]:


x=z.groupby('batting_team').agg({'total_runs':'sum'})
x


# In[ ]:


# from above total_runs_scored_in_cskvssrh=2116+2020=4136 and matches played between=12
total_matches_csk_vs_srh=12
total_runs_scored_in_cskvssrh=4136/total_matches_csk_vs_srh
total_runs_scored_in_cskvssrh

