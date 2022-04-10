# -*- coding: utf-8 -*-
"""Task_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SU2A_lg4inZ6exwDvQ6fKv88MsjNiY7A

###### Assessment

###### I am going to provide two .csv files , you are supposed to work on them and have to provide solutions to the following problems

###### import necessary libraries
"""

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("/content/college_1.csv")

df2 = pd.read_csv("/content/college_2.csv")

df1.info()

df2.info()

df1.head(1)

df2.head(1)

"""###### merge those two csv files (after getting as dataframes, get them as a single dataframe)"""

df = pd.concat([df1,df2],ignore_index=True)

"""###### Take each csv file , split that csv file into multiple categories (example csv files are added in the repo)

###### consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv

###### if  10000<codekata score<15000   (Reached_expectations.csv)

###### if  7000<codekata score<10000   (Needs_Improvement.csv)

###### if  codekate score < 7000        (Unsatisfactory.csv)

1.   List item
2.   List item
"""

# as Exceeded expectations.csv
exceeded_expectation = df[df["CodeKata Score"]>15000]
exceeded_expectation.to_csv("exceeded expectation.csv")
exceeded_expectation

# if 10000<codekata score<15000 (Reached_expectations.csv)
Reached_expectations = df[df["CodeKata Score"].between(10000,15000)]
Reached_expectations.to_csv("Reached_expectations.csv")
Reached_expectations

# if 7000<codekata score<10000 (Needs_Improvement.csv)
Needs_Improvement = df[df["CodeKata Score"].between(7000,10000)]
Needs_Improvement.to_csv("Needs_Improvement.csv")
Needs_Improvement

# if codekate score < 7000 (Unsatisfactory.csv)
Unsatisfactory = df[df["CodeKata Score"]<7000]
Unsatisfactory.to_csv("Unsatisfactory.csv")
Unsatisfactory

"""###### Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)"""

avg1 = df["Previous Geekions"].sum()/len(df["Name"])
avg2 = df["CodeKata Score"].sum()/len(df["Name"])

plt.bar("Previous Geekions",avg1,width=0.5)
plt.bar("CodeKata Score",avg2,width=0.5)
plt.show()

"""###### No of students participated """

no_students =len(df["Name"])
print(no_students)

"""###### #Average completion of python course or my_sql or python english or computational thinking"""

average_complt = df['python']/len(df['python'])
print(average_complt)
print(df.agg({'python':'mean'}))

"""###### rising star of the week (top 3 candidate who performed well in that particular week)"""

df.nlargest(3, 'Rising')

"""###### Shining stars of the week (top 3 candidates who has highest geekions)"""

df.nlargest(3, 'Previous Geekions')

"""###### Department wise codekata performence (pie chart)"""

import plotly.express as px
fig=px.pie(df,names='Department',values='CodeKata Score',title='Department wise codekata performence')
fig.update_traces(textinfo='percent',textposition='outside')

"""###### Department wise toppers (horizantal bar graph or any visual representations of your choice)"""

CSE = df[df["Department"]=="Computer Science and Engineering"]
# CSE.to_csv("CSE.csv")
CSE
max_cse = CSE["CodeKata Score"].max()
max_cse

ECE = df[df["Department"]=="Electronics and Communication Engineering"]
ECE
max_ece = ECE["CodeKata Score"].max()
max_ece

EEE = df[df["Department"]=="Electronics and Electrical Engineering"]
EEE
max_eee = ECE["CodeKata Score"].max()
max_eee

import plotly.express as px

x2 = ["CSE","ECE","EEE"]
y2 = [max_cse,max_ece,max_eee]
fig = px.bar(x=x2, y = y2)
fig.show()