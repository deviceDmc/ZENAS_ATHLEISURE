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

