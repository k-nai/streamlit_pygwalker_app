import polars as pl
import streamlit as st

import pygwalker as pyg

# ワイド表示
st.set_page_config(layout="wide")

# タイトル
st.title("Data Analysis with PyGWalker.")

# データフレームの用意
df = None

# ファイル選択
with st.sidebar:
    uploaded_files = st.file_uploader("Choose a CSV file")
    if uploaded_files is not None:
        df = pl.read_csv(uploaded_files, try_parse_dates=True)

# pygwalkerで表示
pyg.walk(df, env='Streamlit')
