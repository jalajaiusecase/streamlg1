


import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np





# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
from streamlit_option_menu import option_menu
hide_st_style= """
            <style>
            #MainMenu{visibility:hidden;}
            footer{visibility:hidden;}
            header{visibility:hidden;}
            </style>
            """
st.markdown(hide_st_style,unsafe_allow_html=True)



#selectect = option_menu(menu_title=None, options=["Graph","Code"], icons=["pencil-fill","bar-chart-fill"], orientation="horizontal")
   



# ---- READ EXCEL ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="graph.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )

    return df

df = get_data_from_excel()

# ---- SIDEBAR ----


st.sidebar.header("Please Filter Here:")
Libs = st.sidebar.selectbox(
    "Select the Library:",
    options=df["libs"].unique()
     )

Graphname = st.sidebar.selectbox(
    "Select the Graph Chart:",
    options=df["graphname"].unique()        
)


df_selection = df.query(
    "libs== @Libs & graphname ==@Graphname"
)

# ---- MAINPAGE ----


for ind in range(len(df_selection)):
       
    if df_selection.iloc[ind]['present'] =="Yes":
        selectect = option_menu(menu_title=df_selection.iloc[ind]['graphname']+ '-' + str(ind+1), options=["Graph","Code"], icons=["pencil-fill","bar-chart-fill"], orientation="horizontal")   
        if selectect=="Graph":
            code=df_selection.iloc[ind]['cdr']
            exec(code)

        if selectect=="Code":
            code=df_selection.iloc[ind]['code']
            st.code(code, language='python')
    #if df_selection.iloc[ind]['present'] =="No":
        #st.write("There is no Graph")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
