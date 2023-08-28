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
    layer=pdk.Layer(
        "ScatterplotLayer",
        df,
        pickable=True,
        opacity=0.6,
        stroked=True,
        Filled=True,
        radius_scale=1,
        radius_min_pixels=10,
        radius_max_pixels=100,
        line_width_min_pixels=1,
        get_position=["longitude","latitude"],
        get_radius="population",
        get_fill_color=[150,0,0],
        get_line_color=[0,0,0],
    )
    st.pydeck_chart(pdk.Deck(map_style="mapbox://styles/mapbox/light-v9",layers=[layer],initial_view_state=view_state))
else:
    st.error("ファイルをアップロードしてください。")

# Copyright
st.markdown('Thank You For Using')