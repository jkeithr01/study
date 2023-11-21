# This file needs to be run within the Anaconda base environment.
# In VSCode, select the interpreter using the lower-right status bar.

# FROM Streamlit Vending Machine Notebook:
# start the Streamlit Application
# !/opt/conda/envs/snowpark/bin/streamlit run app_vending_machine_simulator.py
# 
# This command ran my app.py file without the error:
# streamlit run app.py --server.fileWatcherType none
# 
# The error was generated because my source file was in a directory that had 
# TOO MANY SUBFOLDERS AND FILES
# See this StackOverflow Q&A:
# https://stackoverflow.com/questions/73027461/oserror-errno-28-inotify-watch-limit-reached/77106870#77106870


from operator import index
import os
import glob
import pandas as pd
import streamlit as st
import altair as alt

# print out a message using markdown
st.write("""
# Hello, world!
This is my first *Streamlit* app!
""")

# create a pandas DataFrame from the people.csv data files
path = r'/Users/kratliff/Documents/demos/data/people.csv'
all_files = glob.glob(os.path.join(path , "*/*.csv"))
# st.write(all_files)
li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
peopleDF = pd.concat(li, axis=0, ignore_index=True)
# could also try 
# df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

# show the data items
# st.write(li)
st.write("""
This is the *people.csv* data in a pandas DataFrame
""")
st.write(peopleDF)
# st.write(peopleDF.columns)
st.write("""
This is the people DataFrame written as a *table*.  
Note that the pandas DataFrame above is scrollable, and the table printout presents all the data.
""")
st.table(peopleDF)

# select and plot the amounts v. id as a bar chart
# twoColDF = peopleDF[["id","amount"]].sort_values(by='amount', ascending=False)
# This version of sort keeps the ordered index in place:
twoColDF = peopleDF[["id","amount"]].sort_values(by='amount', ascending=False, ignore_index=True)
st.write("""
This is *people.csv* with column projection selecting only *id* and *amount*, sorted by 'amount'  
""")
st.write(twoColDF)
st.write("""
These are bar charts from the two-column projection using the DataFrame index as the x-axis, 
and *amount* as the y-axis.  
""")
st.write("""
Thee first bar chart is created using the Streamlit st.bar_chart() wrapper function.  
""")
st.bar_chart(twoColDF, y='amount')
st.write("""
The second bar chart is created using the more general Streamlit Altair charting object, `altair.Chart`,  
and the charting functions `altair-chart()` and `mark_bar()`.  
""")
# NOTE: the DataFrame required the use of the reset_index() function to create a usable column for the 
# mark_bar() function.
# See https://github.com/altair-viz/altair/issues/271 for more details.
c = alt.Chart(twoColDF.reset_index()).mark_bar().encode(
      x=alt.X('index', sort=None)
    , y='amount'
)
st.altair_chart(c)
st.write("""
The Altair bar chart is created in a more compact size by default.  
This can be modified using the `use_container_width` parameter, which takes a Boolean.
""")
st.altair_chart(c 
    , use_container_width=True
)

# Place the scrollable DataFrame and the barchart side-by-side
# I think I found it. See here:
# https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/
col1, col2 = st.columns(2)
col1.write(peopleDF)
col2.altair_chart(c)
# That totally worked!  :)
# Now I want them to be the same vertical size, and closer together in the center.
