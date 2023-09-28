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

st.header("Perbandingan Rata-Rata Nilai SDG Setiap Region")
plt.figure(figsize=(10, 6))

sns.set(font_scale=1)
region_score = df2023.groupby('region')['overall_score'].mean().reset_index()
bar_region = sns.barplot(data=region_score.sort_values(by='overall_score', ascending=False), x="region", y="overall_score")
bar_region.set(xlabel="Region", ylabel="Skor Rata-Rata")
plt.xticks(rotation=45)
st.pyplot(plt.gcf())
plt.close()
st.write("Negara-negara yang termasuk dalam OECD(Economic Co-operation and Development) memiliki rata-rata skor SDG lebih besar dibandingkan dengan region lainnya, sedangkan region Sub-Saharan Africa memiliki rata-rata skor paling rendah. Finland yang merupakan negara dengan skor SDG tertinggi termasuk dalam OECD")
st.divider()

goal_means = df2023[[f"goal_{i}_score" for i in range(1, 18)]].mean()
goal_means = goal_means.sort_values(ascending=False)
st.header("Rata-rata skor goal negara-negara")
plt.figure(figsize=(12, 6))
bar_rata = sns.barplot(x=goal_means.values, y=goal_means.index, palette="viridis")
bar_rata.set(xlabel="Mean Score", ylabel="Goals")
st.pyplot(plt.gcf())
high_scoring_goals = goal_means[goal_means >= goal_means.mean()]
low_scoring_goals = goal_means[goal_means < goal_means.mean()]
st.write("Secara rata-rata, kebanyakan negara sangat bagus skornya dalam goal 13, 12 4 yaitu Climate Action, Responsible Consumption and Production, dan Quality Education. Namun skor rata-rata dari goal 14, 9, 10, 2 yaitu Life Below Water, Industry Innovation and Infrastructure, Reduced Inequalities, dan Zero Hunger masih sangat rendah")

st.divider()
kolom = ["overall_score"] + [f"goal_{i}_score" for i in range(1, 18)]
data_korelasi = df2023[kolom]
matrix_corr = data_korelasi.corr()
matrix_corr = matrix_corr.drop("overall_score", axis=0)
matrix_corr = matrix_corr.drop("overall_score", axis=1)
st.header("Heatmap Korelasi Skor")
plt.figure(figsize=(12, 10))
heatmap = sns.heatmap(matrix_corr, annot=True, cmap="coolwarm", fmt=".2f")
st.pyplot(plt.gcf())
plt.close()

threshold = 0.8
high_correlation_pairs = []
for i in range(matrix_corr.shape[0]):
    for j in range(i + 1, matrix_corr.shape[0]):
        if abs(matrix_corr.iloc[i, j]) > threshold:
            high_correlation_pairs.append((matrix_corr.index[i], matrix_corr.columns[j]))

feature_map = {
    'goal_1_score': 'No Poverty',
    'goal_2_score': 'Zero Hunger',
    'goal_3_score': 'Good Health and Well Being',
    'goal_4_score': 'Quality Education',
    'goal_5_score': 'Gender Equality',
    'goal_6_score': 'Clean Water and Sanitation',
    'goal_7_score': 'Affordable and Clean Energy',
    'goal_8_score': 'Decent Work and Economic Growth',
    'goal_9_score': 'Industry, Innovation and Infrastructure',
    'goal_10_score': 'Reduced Inequalities',
    'goal_11_score': 'Sustainable Cities and Communities',
    'goal_12_score': 'Responsible Consumption and Production',
    'goal_13_score': 'Climate Action',
    'goal_14_score': 'Life Below Water',
    'goal_15_score': 'Life on Land',
    'goal_16_score': 'Peace, Justice, and Strong Institutions',
    'goal_17_score': 'Partnership for The Goals'
}
high_correlation_pairs = [(feature_map.get(pair[0], pair[0]), feature_map.get(pair[1], pair[1]), matrix_corr.loc[pair[0], pair[1]]) for pair in high_correlation_pairs]
st.write("Dari heatmap, kita mendapat suatu fakta unik tentang skor-skor goal SDG yaitu ada beberapa skor yang memiliki korelasi baik itu secara positif maupun negatif. Skor-skor yang dimaksud adalah: ")
if high_correlation_pairs:
     st.subheader("Pasangan dengan korelasi tinggi (>|0.7|):")
     for pair in high_correlation_pairs:
          st.write(f"{pair[0]} dengan {pair[1]}: {pair[2]:.2f}")
else:
     st.subheader("Tidak ada pasangan dengan korelasi tinggi")


# korelasi_kolom = ['goal_3_score', 'goal_4_score', 'goal_6_score']
# data_korelasi = df2023[korelasi_kolom]
# st.header("Korelasi antara goal 6 dengan goal 3 dan 4")
# plt.figure(figsize=(8, 6))
# st.subheader("Korelasi nantara goal 3 dan goal 6")
# scatter_plot_1 = sns.scatterplot(data=data_korelasi, x="goal_3_score", y="goal_6_score")
# plt.title("Scatter Plot: Goal 6 vs. Goal 3 Scores")
# plt.xlabel("Goal 3 Score")
# plt.ylabel("Goal 6 Score")
# st.pyplot(plt.gcf())
# plt.close()

# plt.figure(figsize=(8, 6))
# st.subheader("Korelasi nantara goal 4 dan goal 6")
# scatter_plot_2 = sns.scatterplot(data=data_korelasi, x="goal_4_score", y="goal_6_score")
# plt.title("Scatter Plot: Goal 6 vs. Goal 4 Scores")
# plt.xlabel("Goal 4 Score")
# plt.ylabel("Goal 6 Score")
# st.pyplot(plt.gcf())
# plt.close()

st.divider()
st.header("Statistik Skor SDG Indonesia")
indonesia = df2023[df2023['country'] == 'Indonesia']
selected_columns = ["overall_score"] + [f"goal_{i}_score" for i in range(1, 18)]
plt.figure(figsize=(12, 6))
bar_chart = sns.barplot(data=indonesia[selected_columns], palette="viridis")
bar_chart.set(xlabel="Goals", ylabel="Score")
plt.title("Skor Indonesia di 2023")
plt.xticks(rotation=45)
st.pyplot(plt.gcf())

st.write("Jika diurutkan menurut skor terbesar maka akan menjadi")
indonesia_kolumsort = [f'goal_{i}_score' for i in range(1,18)]
skor = indonesia[indonesia_kolumsort].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
bar_chart = sns.barplot(x=skor.index, y=skor.values)
bar_chart.set(xlabel="Goals", ylabel="Score")
plt.title("Skor Indonesia di 2023 Terurut")
plt.xticks(rotation=45)
st.pyplot(plt.gcf())
st.write("Skor SDG tertinggi yang dimiliki oleh indonesia yaitu di bidang Climate Action, Quality Education, dan Konsumsi Produksi Bertanggung Jawab. Dari bar ini juga dapat kita liat bahwa Indonesia harus menekankan dalam bidang Partnership for The Goals, Kehidupan di Darat, dan Industri Inovasi dan Infrastruktur")
st.divider()