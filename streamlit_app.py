# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Example Streamlit App :cup_with_straw:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)
name_on_smoothie=st.text_input("enter name on smoothie")
st.write("name on smoothie : ",name_on_smoothie)
cnx=st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.FRUIT_OPTIONS").select('FRUIT_NAME')
#st.dataframe(data=my_dataframe, use_container_width=True)
ingredents_list = st.multiselect(
    'What are your favorite fruits',
     my_dataframe,
    max_selections =5)
if ingredents_list:
    st.write('You selected:', ingredents_list)
    st.text( ingredents_list)
    ingredient_string = ''
    for each_fruit in ingredents_list:
        ingredient_string += each_fruit + ' '
    #st.write(ingredient_string)
    my_insert_stmt = """ INSERT INTO SMOOTHIES.PUBLIC.ORDERS(INGREDIENTS,name_on_order) VALUES 
       ('""" + ingredient_string + """ ','""" + name_on_smoothie + """')"""
    st.write(my_insert_stmt)
    submit_order=st.button("submit order")
    if submit_order:
        session.sql(my_insert_stmt).collect()
        
    
