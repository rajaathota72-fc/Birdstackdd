import streamlit as st
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
dropdown = st.sidebar.selectbox("Drop down to select",("Sales invoice Processing","Tax Automation", "Mail Automation"))
if st.sidebar.checkbox("Get Analysis Report"):
    st.success("Hello Decision Maker, here is your RPA report")
    st.image("DMimages/salesorder.png", width=700)
    if st.button("Pay Now & Get Full Report"):
        link = '[Click here to Navigate](https://rzp.io/l/0ne27uKX)'
        st.markdown(link, unsafe_allow_html=True)
    if st.button("Interested in Custom Solutions"):
<<<<<<< HEAD
        link = '[Click here to Navigate](http://birdstack.tech/customsolutions.html)'
        st.markdown(link, unsafe_allow_html=True)
=======
        webbrowser.open_new_tab("http://birdstack.tech/customsolutions.html")

>>>>>>> 7f21ffe1645fd942950e293da1f0afc17459b2be
