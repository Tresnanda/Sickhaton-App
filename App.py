import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit.connections import SQLConnection
import seaborn as sns
from streamlit_option_menu import option_menu
import pickle

#conn = st.experimental_connection('sdg_db', type="sql")
query2023 = "SELECT * FROM sdg_2023"
query2000 = "SELECT * FROM sdg_2000"


conn: SQLConnection = st.experimental_connection('sdg_db', type='sql')
df2023: pd.DataFrame = conn.query(query2023)
df2000: pd.DataFrame = conn.query(query2000)

with open('model/model_new.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
# @st.cache_resource
# def get_data_from_db(query):
#     df: pd.DataFrame = conn.query(query)
#     return df
# df2023 = get_data_from_db(query=query2023)
# df2000 = get_data_from_db(query=query2000)
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
df2023['overall_score'] = pd.to_numeric(df2023['overall_score'], errors='coerce').fillna(0).astype(float)
ubah = ['goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score', 'goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']
df2023[ubah] = df2023[ubah].apply(pd.to_numeric, errors='coerce').fillna(0).astype(float)

df2000.rename(columns = {
        'COL 1':'country_code',
        'COL 2':'country',
        'COL 3':'year',
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
df2000 = df2000[1:]
ubah = ['overall_score'] + ubah
df2000[ubah] = df2000[ubah].apply(pd.to_numeric, errors='coerce').fillna(0).astype(float)


with st.sidebar:
     selected = option_menu("Insight Skor SDG", ['Insight Negara-Negara', 'Insight Indonesia', 'Prediksi Skor SDG'], icons=['bar-chart-fill', 'bar-chart-fill', 'bar-chart-fill'], default_index=1)
     selected

if selected == 'Insight Negara-Negara':
    st.markdown(f"<h1 style='text-align:center;'>Analisis Sustainable Development Goals pada Negara-Negara 2023</h1>",unsafe_allow_html=True)

    st.divider()
    st.header("Negara dengan nilai SDG terbesar di tahun 2023")
    

    #st.dataframe(df2023)
    #df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']] = pd.to_numeric(df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']], errors='coerce').fillna(0).astype(int)
    
    sns.set(font_scale=0.75)
    plot_top10 = sns.barplot(data=df2023.sort_values(by="overall_score", ascending=False).head(10), x="country", y="overall_score", width=0.5)
    st.pyplot(plot_top10.get_figure())
    st.write("Dapat dilihat bahwa Finlandia menempati posisi pertama dalam negara dengan skor SDG rerata, diikuti oleh Swedia, Denmark, Jerman, Austria, Prancis, Norwegia, Czech, Polandia, dan Estonia")
    st.write("Dari grafik ini diketahui juga bahwa negara-negara Eropa melakukan usaha yang bagus dalam mencapai tujuan SDG")
    plt.close()
    st.divider()

    st.header("Persebaran Jumlah Negara Berdasarkan Region")
    #region_counts = df2023.groupby('region')['country'].count().reset_index()
    region_counts = df2023['region'].value_counts().reset_index()
    region_counts.columns = ['region', 'country']
    plt.figure(figsize=(10, 6))
    sns.barplot(data=region_counts, x='region', y='country', palette='viridis')
    plt.xlabel("Region")
    plt.ylabel("Jumlah Negara")
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf()) 
    plt.close()
    st.write("Region dengan negara terbanyak adalah Sub-Saharan Africa disusul dengan OECD di posisi kedua")


    st.divider()
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
    st.write("Walaupun region Sub-Saharan Africa memiliki jumlah negara paling banyak tetapi rata-rata skornya terendah, sedangkan OEDC dengan jumlah negara terbanyak kedua memiliki skor rata-rata SDG tertinggi. Hal ini berarti negara-negara yang termasuk kedalam OEDC mengeluarkan usaha yang sangat bagus dalam mencapai tujuan SDG")
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
    

    feature_map2 = {
        'Skor Rata-Rata': 'overall_score',
        'No Poverty': 'goal_1_score',
        'Zero Hunger': 'goal_2_score',
        'Good Health and Well Being': 'goal_3_score',
        'Quality Education': 'goal_4_score',
        'Gender Equality': 'goal_5_score',
        'Clean Water and Sanitation': 'goal_6_score',
        'Affordable and Clean Energy': 'goal_7_score',
        'Decent Work and Economic Growth': 'goal_8_score',
        'Industry, Innovation and Infrastructure': 'goal_9_score',
        'Reduced Inequalities': 'goal_10_score',
        'Sustainable Cities and Communities': 'goal_11_score',
        'Responsible Consumption and Production': 'goal_12_score',
        'Climate Action': 'goal_13_score',
        'Life Below Water': 'goal_14_score',
        'Life on Land': 'goal_15_score',
        'Peace, Justice, and Strong Institutions': 'goal_16_score',
        'Partnership for The Goals': 'goal_17_score'
    }
    st.header("Perkembangan Skor Seiring Tahun")
    pilihan = st.selectbox('Pilih Jenis Skor', list(feature_map2.keys()), key='select-type', index=0)
    kolom_pilihan = feature_map2[pilihan]
    rata_pil = df2000.groupby('year')[kolom_pilihan].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.plot(rata_pil['year'], rata_pil[kolom_pilihan], marker='o', linestyle='-', color='b')
    plt.xlabel("Year")
    plt.ylabel("Overall Score")
    plt.xticks(rotation=45)
    plt.title("Rata-Rata Skor Tahun ke Tahun")
    plt.grid(True)
    #plt.ylim(30, 90)
    st.pyplot(plt.gcf())
    plt.close()
    st.write("Dari linechart kita dapat mengetahui bahwa pengembangan skor SDG di hampir semua bidang memiliki tren yang sama, yaitu meningkat. Namun di beberapa goal terdapat tren yang berbeda seperti pada Climate Action yang mengalami penurunan sampai tahun 2011 lalu naik lagi")
    st.write("Lalu terdapat juga suatu kesamaan dari semua goal yaitu dari tahun 2020 ke atas usaha yang dikeluarkan untuk goal tersebut tidak sebanyak pada tahun sebelumnya. Hal ini dapat dilihat dari linechart yang cenderung mendatar dari tahun 2020 ke atas")

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

elif selected == 'Insight Indonesia':
    st.markdown(f"<h1 style='text-align:center;'>Analisis Sustainable Development Goals Indonesia 2023</h1>",unsafe_allow_html=True)
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
    plt.close()
    st.write("Skor SDG tertinggi yang dimiliki oleh indonesia yaitu di bidang Climate Action, Quality Education, dan Konsumsi Produksi Bertanggung Jawab. Dari bar ini juga dapat kita liat bahwa Indonesia harus menekankan dalam bidang Partnership for The Goals, Kehidupan di Darat, dan Industri Inovasi dan Infrastruktur")
    st.divider()


    st.header("Perkembangan skor SDG Indonesia")
    indonesia_data = df2000[df2000['country'] == 'Indonesia']
    years = indonesia_data['year']

    #scores = indonesia_data['overall_score']
    feature_map2 = {
        'Skor Rata-Rata': 'overall_score',
        'No Poverty': 'goal_1_score',
        'Zero Hunger': 'goal_2_score',
        'Good Health and Well Being': 'goal_3_score',
        'Quality Education': 'goal_4_score',
        'Gender Equality': 'goal_5_score',
        'Clean Water and Sanitation': 'goal_6_score',
        'Affordable and Clean Energy': 'goal_7_score',
        'Decent Work and Economic Growth': 'goal_8_score',
        'Industry, Innovation and Infrastructure': 'goal_9_score',
        'Reduced Inequalities': 'goal_10_score',
        'Sustainable Cities and Communities': 'goal_11_score',
        'Responsible Consumption and Production': 'goal_12_score',
        'Climate Action': 'goal_13_score',
        'Life Below Water': 'goal_14_score',
        'Life on Land': 'goal_15_score',
        'Peace, Justice, and Strong Institutions': 'goal_16_score',
        'Partnership for The Goals': 'goal_17_score'
    }

    scores = st.selectbox('Pilih Jenis Skor', list(feature_map2.keys()), key='select-type2', index=0)
    selected_column = feature_map2[scores]
    indonesia_data[selected_column] = indonesia_data[selected_column].astype(float)
    #indonesia_data[scores] = indonesia_data[scores].astype(float)
    plt.figure(figsize=(10, 6))
    plt.plot(years, indonesia_data[selected_column], marker='o', linestyle='-', color='b')
    plt.xlabel("Year")
    plt.ylabel("Overall Score")
    plt.xticks(rotation=45)
    plt.title("Rata-Rata Skor Indonesia Dari Tahun ke Tahun")
    plt.grid(True)
    plt.ylim(0, 100)
    st.pyplot(plt.gcf())
    plt.close()
    st.write("Dari linechart mengenai skor SDG Indonesia tahun ke tahun kita menemui bahwa secara rata-rata nilai SDG di Indonesia tidak begitu berkembang sampai tahun 2012 di mana terdapat trend naik. ")
    st.write("Begitu pula dengan skor No Poverty, terdapat perkembangan yang pesat dari tahun 2010. Pada tahun-tahun sebelumnya skor No Poverty berada di rentan 60, tapi darai tahun 2010 skor tersebut mulai naik sampai ke angka di atas 80")
    st.write("Skor Reduced Inequalities mengalami trend turun penurunan yang paling pesat pada tahun 2010 ke 2011. Skor Reduced Inequalities yang awalnya di rentan 90 sekarang menjadi di rentan 60, hal ini harus diperbaiki secepatnya")
    st.write("Pemerintah juga harus memerhatikan Life on Land karena dari tahun 2000 sampai 2022 terjadi sedikit sekali perubahan dan skornya yang rendah yaitu di rentan 40")
    st.write("Masih banyak goals dari SDG yang harus diberikan usaha lebih baik oleh pemerintah karena kebanyakan skor SDG Indonesia di setiap goal memiliki garis yang datar")

elif selected == 'Prediksi Skor SDG':
    country_names = ['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
       'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The',
       'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
       'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
       'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria',
       'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon',
       'Canada', 'Central African Republic', 'Chad', 'Chile', 'China',
       'Colombia', 'Comoros', 'Congo, Dem. Rep.', 'Congo, Rep.',
       'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus',
       'Czechia', 'Denmark', 'Djibouti', 'Dominican Republic',
       'East and South Asia', 'Eastern Europe and Central Asia',
       'Ecuador', 'Egypt, Arab Rep.', 'El Salvador', 'Estonia',
       'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon',
       'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece',
       'Guatemala', 'Guinea', 'Guyana', 'Haiti', 'High-income Countries',
       'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia',
       'Iran, Islamic Rep.', 'Iraq', 'Ireland', 'Israel', 'Italy',
       'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea, Rep.',
       'Kuwait', 'Kyrgyz Republic', 'Lao PDR',
       'Latin America and the Caribbean', 'Latvia', 'Lebanon', 'Lesotho',
       'Liberia', 'Lithuania', 'Lower & Lower-middle Income',
       'Lower-middle-income Countries', 'Low-income Countries',
       'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
       'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico',
       'Middle East and North Africa', 'Moldova', 'Mongolia',
       'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
       'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger',
       'Nigeria', 'North Macedonia', 'Norway', 'Oceania', 'OECD members',
       'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay',
       'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
       'Russian Federation', 'Rwanda', 'Sao Tome and Principe',
       'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore',
       'Slovak Republic', 'Slovenia', 'Small Island Developing States',
       'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka',
       'Sub-Saharan Africa', 'Sudan', 'Suriname', 'Sweden', 'Switzerland',
       'Syrian Arab Republic', 'Tajikistan', 'Tanzania', 'Thailand',
       'Togo', 'Trinidad and Tobago', 'Tunisia', 'Türkiye',
       'Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates',
       'United Kingdom', 'United States', 'Upper-middle-income Countries',
       'Uruguay', 'Uzbekistan', 'Venezuela, RB', 'Vietnam', 'World',
       'Yemen, Rep.', 'Zambia', 'Zimbabwe']
    import json
    with open('dataset/country_mapping.json', 'r') as json_file:
        country_mapping = json.load(json_file)
    st.markdown(f"<h1 style='text-align:center;'>Prediksi Skor SDG di Tahun 2030</h1>",unsafe_allow_html=True)
    st.divider()
    negara = st.selectbox('Pilih Negara', list(country_mapping.keys()), key='select-type3', index=0)
    selected_negara = country_mapping[negara]
    predict_input = [[selected_negara, 2030]]

    predict = model.predict(predict_input)
    st.write(f"Skor SDG untuk Negara {negara} di tahun 2030 adalah {predict[0]}")
    