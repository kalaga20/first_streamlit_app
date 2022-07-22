import streamlit
import pandas

streamlit.title('🥣 All New Healthy Diner App')

streamlit.header('🐔 - Breakfast Menu')
streamlit.text('🥗 - Idly')
streamlit.text('🍞 - Dosa')
streamlit.text('🥑 - Poha')
   
streamlit.header('Lunch Menu')
streamlit.text('🐔 - Chicken Biriyani')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
