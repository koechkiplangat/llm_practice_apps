import streamlit as st

from app import engine

st.title ("Start a Restaurant")

Cuisine = st.sidebar.selectbox("Pick a Cuisine of your choice:", ("Kenyan", "Ethiopian", "Arabic", "Indian", "Chinese"))


if Cuisine:
    response = engine.start_a_restaurant(Cuisine)
    st.header("**Restaurant name**")  
    st.write (response['restaurant_name'])
    menu_items = response["menu_list"].split(",")
    st.header("**Menu**")
    for item in menu_items:
        st.write(item)
else:
    print ({"error_message": "cuisie not selected"})