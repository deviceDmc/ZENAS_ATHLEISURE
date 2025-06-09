# Import python packages
import streamlit as st
import pandas as pd
from snowflake.snowpark.functions import col
import requests

# Write directly to the app
st.title(f" Zena's Web Catalog ")
st.write(
  """Pick a swetsuit color of style!
  """
)
cnx= st.connection("snowflake")
session = cnx.session()

#conert de snowpark dataframe to pandas dataframe so we can use de LOC funciton
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE").select(col('COLOR_OR_STYLE'), col('FILE_NAME'), col('FILE_URL'), col('PRICE'), col('SIZE_LIST'), col('UPSELL_PRODUCT_DESC'))
st.dataframe(data=my_dataframe, use_container_width=True)
#st.stop()

pd_df= my_dataframe.to_pandas()
st.dataframe(pd_df)
#st.stop()

color_selected = st.selectbox (
"Pick a swetsuit color of style!"
, my_dataframe
)
st.stop()

  for fruit_chosen in ingredients_list:
    ingredients_string += fruit_chosen + ' '
    search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
    st.write('The search value for ', fruit_chosen,' is ', search_on, '.')
    st.subheader(fruit_chosen + ' Nutrition Information')
    smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/" + search_on)
    sf_df=st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)
    st.write(ingredients_string)
    
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, NAME_ON_ORDER)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""
    
  st.write(my_insert_stmt)
  #st.stop()
  if time_to_insert:
      session.sql(my_insert_stmt).collect()
      st.success('Your Smoothie is ordered! ' + name_on_order, icon="✅")
      
