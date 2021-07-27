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


# In[26]:


import pandas as pd
import numpy as np
df=pd.read_csv("../input/rr-vs-dc-match/deliveries.csv")
df.head()
df.info()
import os
print(os.listdir("../input"))


# In[27]:


df1=pd.read_csv("../input/rr-vs-dc-match/matches.csv")
df1.info()


# In[28]:


df2=df1[['team1','team2','winner','result','toss_winner','toss_decision']]
df2.head()


# In[29]:


df3 = df2[(df2['team1']=='Rajasthan Royals') & (df2['team2'] == 'Delhi Capitals')]

df3 


# In[30]:


df4 = df2[(df2['team1']=='Delhi Capitals') & (df2['team2'] == 'Rajasthan Royals')]

df4 


# In[31]:


df5 = pd.concat([df3,df4], axis=0)
df5


# In[32]:


df5['winner'].value_counts()


# In[33]:


matches_played=pd.concat([df1['team1'],df1['team2']])
matches_played=matches_played.value_counts().reset_index()
matches_played.columns=['Team','Total Matches']
matches_played['wins']=df1['winner'].value_counts().reset_index()['winner']

matches_played.set_index('Team',inplace=True)
matches_played.reset_index().head(8)


# In[34]:


win_percentage = round(matches_played['wins']/matches_played['Total Matches'],3)*100
win_percentage.head(8)


# In[35]:


df6= df[['bowling_team','batting_team','batsman','batsman_runs','match_id']]
df6.head()
df7=df6[(df6['bowling_team']=='Delhi Capitals') & (df6['batsman'] == 'SPD Smith')]
df7


# In[36]:


df7['match_id'].value_counts()


# In[37]:


df8=df7.groupby('batsman').agg({'batsman_runs':'sum'})
df8


# In[38]:


runs_against_dc=150
total_matches_for_smith_against_rr=5
run_per_match=runs_against_dc/total_matches_for_smith_against_rr
run_per_match


# In[39]:


a= df[['bowling_team','batting_team','wide_runs']]
b=a[(a['bowling_team']=='Delhi Capitals') & (a['batting_team'] == 'Rajasthan Royals') & (a['wide_runs'] == 1) ]
b


# In[40]:


c= df[['bowling_team','batting_team','wide_runs']]
d=c[(c['bowling_team']=='Rajasthan Royals') & (c['batting_team'] == 'Delhi Capitals') & (a['wide_runs'] == 1)]
d


# In[41]:


e = pd.concat([b,d], axis=0)
e


# In[42]:


f=e.groupby('bowling_team').agg({'wide_runs':'sum'})
f


# In[43]:


#total_wides=68+67=135 and total_matches_rr_vs_dc=20...
total_matches_rr_vs_dc=20
total_wides=135
wides_per_match=total_wides/total_matches_rr_vs_dc

wides_per_match


# In[44]:


i= df[['bowling_team','batting_team','player_dismissed']]
j=i[(i['bowling_team']=='Delhi Capitals') & (i['batting_team'] == 'Rajasthan Royals')]
j


# In[45]:


k= df[['bowling_team','batting_team','player_dismissed']]
l=k[(k['bowling_team']=='Rajasthan Royals') & (k['batting_team'] == 'Delhi Capitals')]
l


# In[72]:


m = pd.concat([j,l], axis=0)
m


# In[73]:


m=m.fillna(0)
m


# In[74]:


m['player_dismissed'] = m['player_dismissed'].apply(lambda x: 'NO WICKET'  if x== 0 else 'WICKET')
m


# In[75]:


m['player_dismissed'].value_counts()


# In[76]:


#from above total players dismissed during rr vs dc=225
wickets_per_match=225/total_matches_rr_vs_dc
wickets_per_match


# In[ ]:


k= df[['bowling_team','batting_team','player_dismissed']]
l=k[(k['bowling_team']=='Rajasthan Royals') & (k['batting_team'] == 'Delhi Capitals')]
l


# In[78]:


x= df[['bowling_team','batting_team','over','total_runs']]
y=x[(x['bowling_team']=='Rajasthan Royals') & (x['batting_team'] == 'Delhi Capitals') & (x['over'] < 7)]
y


# In[79]:


z=y.groupby('batting_team').agg({'total_runs':'sum'})
z


# In[80]:


#total_scores_of_dc_in_powerplay=953
total_scores_of_dc_in_powerplay=953
powerplayruns_per_match_dc=total_scores_of_dc_in_powerplay/total_matches_rr_vs_dc
powerplayruns_per_match_dc

