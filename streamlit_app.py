# Streamlitライブラリをインポート
import streamlit as st
import pandas as pd
import pydeck as pdk
# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="人口分布可視化アプリ", layout="wide")

# タイトルを設定
st.title('人口分布可視化アプリ')

st.caption("Created by Ryota Kawamura")


uploaded_file=st.file_uploader("ファイルをアップロードしてください (CSV or Excel)", type=["csv","xlsx"])
if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df=pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df=pd.read_excel(uploaded_file)
    
    view_state=pdk.ViewState(
        latitude=df["latitude"].mean(),
        longitude=df["longitude"].mean(),
        zoom=10,
        pitch=0,
    )