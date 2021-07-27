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
df=pd.read_csv("../input/rcb-vs-kxip-match/deliveries.csv")
df.head()
df.info()
import os
print(os.listdir("../input"))


# In[2]:


df1=pd.read_csv("../input/rcb-vs-kxip-match/matches.csv")
df1.info()


# In[38]:


df2=df1[['team1','team2','winner','result','toss_winner','toss_decision','season']]
df2.head()


# In[40]:


df3 = df2[(df2['team1']=='Royal Challengers Bangalore') & (df2['team2'] == 'Kings XI Punjab') ]

df3 


# In[41]:


df4 = df2[(df2['team1']=='Kings XI Punjab') & (df2['team2'] == 'Royal Challengers Bangalore')]

df4 


# In[54]:


df5 = pd.concat([df3,df4], axis=0)
df5


# In[55]:


df5['winner'].value_counts()


# In[56]:


df5 = df5[(df5['season'] > 2016)] 
df5


# In[53]:


df5['winner'].value_counts()


# In[7]:


matches_played=pd.concat([df1['team1'],df1['team2']])
matches_played=matches_played.value_counts().reset_index()
matches_played.columns=['Team','Total Matches']
matches_played['wins']=df1['winner'].value_counts().reset_index()['winner']

matches_played.set_index('Team',inplace=True)
matches_played.reset_index().head(8)


# In[8]:


win_percentage = round(matches_played['wins']/matches_played['Total Matches'],3)*100
win_percentage.head(8)


# In[9]:


i= df[['bowling_team','batting_team','player_dismissed']]
j=i[(i['bowling_team']=='Royal Challengers Bangalore') & (i['batting_team'] == 'Kings XI Punjab')]
j


# In[10]:


j=j.fillna(0)
j


# In[11]:


j['player_dismissed'] = j['player_dismissed'].apply(lambda x: 'NO WICKET'  if x== 0 else 'WICKET')
j


# In[12]:


j['player_dismissed'].value_counts()


# In[13]:


#from above total players of KXIP dismissed during RCB vs KXIP=135
total_matches_rcb_vs_kxip=24
wickets_per_match_ofkxip=135/total_matches_rcb_vs_kxip
wickets_per_match_ofkxip


# In[14]:


a= df[['bowling_team','batting_team','noball_runs']]
b=a[(a['bowling_team']=='Kings XI Punjab') & (a['batting_team'] == 'Royal Challengers Bangalore') & (a['noball_runs'] == 1)]
b


# In[15]:


c= df[['bowling_team','batting_team','noball_runs']]
d=c[(c['bowling_team']=='Royal Challengers Bangalore') & (c['batting_team'] == 'Kings XI Punjab') & (c['noball_runs'] == 1)]
d


# In[16]:


e = pd.concat([b,d], axis=0)
e


# In[17]:


f=e.groupby('bowling_team').agg({'noball_runs':'sum'})
f


# In[18]:


#total_noball_runs=15+7=22 and total_matches_rcb_vs_kxip=20...
total_matches_rcb_vs_kxip=24
total_noball_runs=22
noball_per_match=total_noball_runs/total_matches_rcb_vs_kxip

noball_per_match


# In[19]:


g= df[['batting_team','bowling_team','batsman_runs']]
g.head()

h=g[(g['batting_team'] == 'Kings XI Punjab') & (g['bowling_team'] == 'Royal Challengers Bangalore') & (g['batsman_runs'] == 6)]
h


# In[20]:


w=g[(g['batting_team'] == 'Royal Challengers Bangalore') & (g['bowling_team'] == 'Kings XI Punjab') & (g['batsman_runs'] == 6)]
w


# In[21]:


v = pd.concat([h,w], axis=0)
v


# In[22]:


v['batsman_runs'].value_counts()


# In[23]:


#from above data total_sixes=289
total_sixes=289
total_macthes_rcb_vs_kxip=24
sixes_per_match=total_sixes/total_macthes_rcb_vs_kxip
sixes_per_match


# In[29]:


x= df[['batsman','non_striker','total_runs','match_id','bowling_team']]
x.head()

y=x[(x['batsman'] == 'V Kohli') & (x['non_striker'] == 'AB de Villiers') & (x['bowling_team'] == 'Kings XI Punjab')]
y


# In[30]:


z=x[(x['batsman'] == 'AB de Villiers') & (x['non_striker'] == 'V Kohli') & (x['bowling_team'] == 'Kings XI Punjab')]
z


# In[31]:


o = pd.concat([y,z], axis=0)
o


# In[34]:


tt=o.groupby('match_id').agg({'total_runs':'sum'})
tt


# In[35]:


tt=o.groupby('batsman').agg({'total_runs':'sum'})
tt


# In[37]:


#from above data total_runs_between_kohliandABde=120
total_runs_between_kohliandABde=120
#from total_macthes_rcb_vs_kxip_with_AB_and_VK_both=5
total_macthes_rcb_vs_kxip_with_AB_and_VK_both=5
runs_between_them_per_match=total_runs_between_kohliandABde/total_macthes_rcb_vs_kxip_with_AB_and_VK_both
runs_between_them_per_match


# In[ ]:




