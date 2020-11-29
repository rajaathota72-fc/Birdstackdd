import pandas as pd
import os
def storing_data(name,role,organisation):
    List = [name,role,organisation]
    df = pd.DataFrame(List)
    directory = "DM_database/"
    os.mkdir("DM_database/"+name)
    file = os.path.join(directory,name)
    save = df.to_csv(file+"/details.csv")
    return save
import streamlit as st
import webbrowser
template = """
   <div style = "background-color : blue; padding : 1px;">
   <h2 style = "color:white;text-align:center;"> Decision Maker Zone - Interaction Portal </h2>
   </div>
   """
st.markdown(template, unsafe_allow_html=True)
st.image("dm.gif")
st.sidebar.title("Fill the details")
st.sidebar.image("Picture 1.png",width = 300)
st.write(" Get your RPA report today, Open sidebar & fill the details to let us know what you are looking for!")
name = st.sidebar.text_input("Name with Salutation","Type here")
role = st.sidebar.text_input("Role / Designation","Type here")
organisation = st.sidebar.text_input("Name of your Organisation","Type here")
st.sidebar.success("Select task to automate")
<<<<<<< HEAD
dropdown = st.sidebar.selectbox("Drop down to select",("Sales invoice Processing","Tax Automation", "Mail Automation"))
if st.sidebar.checkbox("Get Analysis Report"):
    st.success("Hello Decision Maker, here is your RPA report")
    st.image("DMimages/salesorder.png", width=700)
    storing_data(name,role,organisation)
    if st.button("Pay Now & Get Full Report"):
        webbrowser.open_new_tab("https://www.streamlit.io/")
    if st.button("Interested in Custom Solutions"):
        webbrowser.open_new_tab("http://birdstack.tech/customsolutions.html")

