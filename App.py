import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit.connections import SQLConnection
import seaborn as sns

#conn = st.experimental_connection('sdg_db', type="sql")
query2023 = "SELECT * FROM sdg_2023"
query2000 = "SELECT * FROM sdg_2000"


conn: SQLConnection = st.experimental_connection('sdg_db', type='sql')
df2023: pd.DataFrame = conn.query(query2023)
df2000: pd.DataFrame = conn.query(query2000)


st.markdown(f"<h1 style='text-align:center;'>Analisis Sustainable Development Goals pada Negara-Negara 2023</h1>",unsafe_allow_html=True)

st.divider()
st.header("Negara dengan nilai SDG terbesar di tahun 2023")
df2023.rename(columns = {
    'COL 1':'country_code',
    'COL 2':'country',
    'COL 3':'region',
    'COL 4':'overall_score',
    'COL 5':'goal_1_score',
    'COL 6':'goal_2_score',
    'COL 7':'goal_3_score',
    'COL 8':'goal_4_score',
    'COL 9':'goal_5_score',
    'COL 10':'goal_6_score',
    'COL 11':'goal_7_score',
    'COL 12':'goal_8_score',
    'COL 13':'goal_9_score',
    'COL 14':'goal_10_score',
    'COL 15':'goal_11_score',
    'COL 16':'goal_12_score',
    'COL 17':'goal_13_score',
    'COL 18':'goal_14_score',
    'COL 19':'goal_15_score',
    'COL 20':'goal_16_score',
    'COL 21':'goal_17_score',
}, inplace=True)
df2023 = df2023[1:]

#st.dataframe(df2023)
#df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']] = pd.to_numeric(df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']], errors='coerce').fillna(0).astype(int)
df2023['overall_score'] = pd.to_numeric(df2023['overall_score'], errors='coerce').fillna(0).astype(float)

sns.set(font_scale=0.75)
plot_top10 = sns.barplot(data=df2023.sort_values(by="overall_score", ascending=False).head(10), x="country", y="overall_score", width=0.5)
st.pyplot(plot_top10.get_figure())
st.write("Dapat dilihat bahwa Finlandia menempati posisi pertama dalam negara dengan skor SDG rerata, diikuti oleh Swedia, Denmark, Jerman, Austria, Prancis, Norwegia, Czech, Polandia, dan Estonia")

st.divider()

ubah = ['goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score', 'goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']
df2023[ubah] = df2023[ubah].apply(pd.to_numeric, errors='coerce').fillna(0).astype(float)



