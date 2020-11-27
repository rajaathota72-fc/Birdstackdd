import pandas as pd
df = pd.read_csv("salesorder.csv")
#print(df)
df_1 = df[["RPA BOT","Type","Platform","RPA Tool","Link"]]
#print(df_1)
df_2 = df[["RPA BOT","ROI","Cost Reduction","Visibility","Accuracy","Productivity"]]
#print(df_2)
import streamlit as st
st.title("News Feed Summary Test - Admin Panel")
st.image("rpaf.jpg",width=700)
st.sidebar.title("Fill the details")
st.sidebar.image("Picture 1.png",width = 300)
st.write("This is a test Client Panel used for unit testing - to check how information is provided to client based on requirements ")
radio = st.sidebar.radio("Select your Role",("Developer","Decision Maker"),key=None)
st.sidebar.success("Select task to automate")
dropdown = st.sidebar.selectbox("Drop down to select",("Sales invoice Processing","other"))
if radio == "Developer" and dropdown=="Sales invoice Processing":
    if st.sidebar.button("Submit"):
        st.success("Hello Developer, here is your RPA report")
        st.dataframe(df_1)
        st.button("Download now")
if radio == "Decision Maker" and dropdown=="Sales invoice Processing":
    if st.sidebar.button("Submit"):
        st.success("Hello Decison Maker, here is your RPA report")
        st.dataframe(df_2)
        st.button("Download now")
if dropdown == "other":
    if st.sidebar.button("Submit"):
        st.success("Hello This part is in development phase Thanks for visiting")
       
