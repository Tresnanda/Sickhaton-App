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
    st.markdown(f"<h1 style='text-align:center;'>Analisis Sustainable Development Goals pada Negara-Negara Tahun 2023</h1>",unsafe_allow_html=True)

    st.divider()
    st.header("10 Negara dengan nilai rata-rata tertinggi aspek SDGs di tahun 2023")
    

    #st.dataframe(df2023)
    #df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']] = pd.to_numeric(df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']], errors='coerce').fillna(0).astype(int)
    
    sns.set(font_scale=0.75)
    plot_top10 = sns.barplot(data=df2023.sort_values(by="overall_score", ascending=False).head(10), x="country", y="overall_score", width=0.5)
    plt.xticks(rotation=45)
    st.pyplot(plot_top10.get_figure())
    st.write ("✅Berdasarkan diagram tersebut, Negara Finlandia menduduki peringkat pertama dengan perolehan rata-rata nilai tertinggi dari seluruh aspek SDGs berdasarkan data tahun 2023.")
    st.write("✅10 Negara dalam peringkat teratas termasuk kategori wilayah Benua Eropa dengan nilai rata-rata di atas 80% sehingga menunjukan bahwa kawasan tersebut telah melakukan upaya dalam mengejar 17 tujuan SDGs di tahun 2030.")
    plt.close()
    st.divider()

    st.header("10 Negara dengan nilai rata-rata terendah aspek SDGs di tahun 2023")
    

    #st.dataframe(df2023)
    #df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']] = pd.to_numeric(df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']], errors='coerce').fillna(0).astype(int)
    
    sns.set(font_scale=0.65)
    plot_top10 = sns.barplot(data=df2023.sort_values(by="overall_score", ascending=True).head(10), x="country", y="overall_score", width=0.5)
    plt.xticks(rotation=45)
    st.pyplot(plot_top10.get_figure())
    st.write ("✅Berdasarkan diagram tersebut, Negara Finlandia menduduki peringkat pertama dengan perolehan rata-rata nilai tertinggi dari seluruh aspek SDGs berdasarkan data tahun 2023.")
    st.write("✅10 Negara dalam peringkat teratas termasuk kategori wilayah Benua Eropa dengan nilai rata-rata di atas 80% sehingga menunjukan bahwa kawasan tersebut telah melakukan upaya dalam mengejar 17 tujuan SDGs di tahun 2030.")
    plt.close()
    st.divider()

    st.header("Distribusi Jumlah Negara Berdasarkan Kategori Region")
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
    st.write("✅Berdasarkan diagram batang di atas, Sub-Saharan Africa menjadi kategori region dengan persebaran negara terbanyak dalam data laporan pertumbuhan SDGs tahun 2023.")
    st.write("✅Sedangkan region Oceania menjadi kategori region dengan persebaran negara paling sedikit dalam data laporan pertumbuhan SDGs tahun 2023.")
    st.write("✅Region E.Europe & C.Asia dan Region LAC menjadi dua region dengan persamaan jumlah persebaran negara berdasarkan data laporan pertumbuhan SDGs tahun 2023.")
    st.divider()
    st.header("Rasio Rata-Rata Nilai Seluruh Aspek SDG dalam Setiap Region")
    plt.figure(figsize=(10, 6))

    sns.set(font_scale=1)
    region_score = df2023.groupby('region')['overall_score'].mean().reset_index()
    bar_region = sns.barplot(data=region_score.sort_values(by='overall_score', ascending=False), x="region", y="overall_score")
    bar_region.set(xlabel="Region", ylabel="Skor Rata-Rata")
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())
    plt.close()
    st.write("✅Negara-negara yang tergabung dalam Organisasi Kerja Sama dan Pembangunan Ekonomi (OECD) menunjukkan pencapaian rata-rata yang jauh lebih tinggi dalam mencapai SDGs dibandingkan dengan wilayah-wilayah lain di seluruh dunia. Di sisi lain, wilayah Sub-Saharan Africa, dengan rata-rata skor SDG yang paling rendah, sehingga menjadi fokus perhatian dalam upaya menuju pencapaian tujuan-tujuan pembangunan berkelanjutan. Sebagai contoh, Finlandia, yang menonjol sebagai negara dengan skor SDG tertinggi, merupakan salah satu anggota terkemuka dalam kelompok OECD ini.")
    st.write("✅Meskipun Sub-Saharan Africa memiliki jumlah negara terbanyak, rata-rata skor Indeks Pembangunan Berkelanjutan (SDG) di wilayah ini adalah paling rendah. Di sisi lain, Region OECD dengan jumlah negara peringkat kedua terbanyak berhasil mencatat rata-rata skor SDG tertinggi. Hal ini mencerminkan komitmen yang kuat dari negara-negara OECD dalam mencapai tujuan SDG.")
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
    st.write("✅Secara keseluruhan, sebagian besar negara telah menunjukkan pencapaian yang baik dalam mencapai tujuan SDG seperti Goal 13 (Climate Action), Goal 12 (Responsible Consumption and Production), dan Goal 4 (Quality Education), dengan rata-rata skor di peringkat teratas.")
    st.write("✅Namun, terdapat tantangan yang signifikan dalam pencapaian Goal 14 (Life Below Water), Goal 9 (Industry, Innovation, and Infrastructure), Goal 10 (Reduced Inequalities), dan Goal 2 (Zero Hunger), yang masih mencatat skor rata-rata yang rendah. Hal ini menunjukan bahwa perluasan upaya dan fokus lebih lanjut pada aspek-aspek kunci pembangunan berkelanjutan yang masih memerlukan perhatian serius dan tindakan bersama.")
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
    st.header("Perkembangan Skor SDG dari Tahun 2022 - 2022")
    pilihan = st.selectbox('Pilih Jenis Skor', list(feature_map2.keys()), key='select-type', index=0)
    kolom_pilihan = feature_map2[pilihan]
    rata_pil = df2000.groupby('year')[kolom_pilihan].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.plot(rata_pil['year'], rata_pil[kolom_pilihan], marker='o', linestyle='-', color='b')
    plt.xlabel("Year")
    plt.ylabel("Overall Score")
    plt.xticks(rotation=45)
    plt.title("Rata-Rata Skor SDG dari Tahun ke Tahun")
    plt.grid(True)
    #plt.ylim(30, 90)
    st.pyplot(plt.gcf())
    plt.close()
    st.write("✅Berdasarkan grafik skor rata-rata dari seluruh aspek SDG pada periode tahun 2000 sampai 2022 menunjukan bahwa terjadi pertumbuhan yang terus naik dengan konsisten di setiap tahunnya sehingga menggambarkan peningkatan usaha yang dilakukan oleh negara-negara dalam mengejar target SDGs 2030.")
    st.write("✅Pada Aspek Tujuan SDG (No Poverty) tidak mengalami peningkatan yang signifikan pada tahun 2000 sampai 2010, namun terjadi peningkatan yang sangat tajam dari tahun 2010 sampai 2019 yang mengindikasikan penurunan angka kemiskinan, kemudian terjadi penurunan skor pada periode 2019-2020 akibat pandemi covid-19 sehingga menyebabkan meningkatnya angka kemiskinan, akan tetapi pada periode 2019-2022 terjadi pemulihan tingkat kemiskinan yang ditandai oleh meningkatnya skor.") 
    st.write("✅Pada Aspek Tujuan Zero Hunger, terjadi ketidakkonsistenan perkembangan skor pada beberapa periode tahun, sehingga memerlukan perluasan upaya yang untuk meningkatkan stabilitas skor dalam pencapaian tujuan SDG ini pada tahun berikutnya.")
    st.write("✅Grafik Good Health and Well Being menunjukan peningkatan yang stabil dari tahun 2000 sampai tahun 2019, namun terjadi sedikit penurunan skor pada periode 2019-2022 hal itu disebabkan oleh Pandemi Covid-19 yang memengaruhi tingkat kesehatan manusia sehingga berdampak pada penurunan kualitas Kehidupan Sehat dan Sejahtera.")
    st.write("✅Grafik Quality Education mengalami kenaikan secara konsisten pada periode 2000-2020, namun terjadi sedikit penurunan kualitas pendidikan pada periode 2020-2022 hal itu menunjukan perlu ada perbaikan kualitas pendidikan pada tahun berikutnya.")
    st.write("✅Aspek Gender Quality menunjukan grafik yang stabil naik dari periode tahun 2000-2022 mencerminkan kemajuan yang berkelanjutan dalam upaya mencapai kesetaraan gender.")
    st.write("✅Aspek Clean Water and Sanitation menunjukan pertumbuhan skor yang meningkat konsisten dari tahun 2000 sampai tahun 2020, namun terjadi sedikit penurunan skor dari tahun 2020-2022 sehingga perlu upaya pemeliharaan dan pemantauan berkelanjutan dalam menjaga akses air bersih dan sanitasi yang baik untuk meningkatkan kembali skor pada tahun berikutnya.")
    st.write("✅Aspek Affordable and Clean Energy mengalami peningkatan skor yang konsisten dari tahun 2000 hingga 2020, mencerminkan langkah-langkah positif dalam pengembangan sumber energi yang bersih dan terjangkau. Namun, terjadinya sedikit penurunan pada periode 2020-2022 menunjukkan perlunya pemantauan dan adaptasi terhadap dinamika perubahan dalam sektor energi global, yang dapat memengaruhi aksesibilitas dan keberlanjutan sumber energi bersih di tahun berikutnya.")
    st.write("✅Grafik Decent Work and Economic Growth menunjukkan perkembangan skor yang tidak stabil dari beberapa periode, dengan fluktuasi antara peningkatan dan penurunan. Hal ini mungkin mencerminkan tantangan kompleks yang dihadapi dalam mencapai pertumbuhan ekonomi yang inklusif dan menciptakan lapangan kerja yang layak.")
    st.write("✅Grafik Industry, Innovation and Infrastructure menunjukan peningkatan skor yang cenderung naik dan konsisten pada periode tahun 2000-2022, Hal ini mencerminkan upaya yang berhasil dalam mengembangkan sektor industri, inovasi, dan infrastruktur, yang memiliki dampak positif pada pertumbuhan ekonomi dan perkembangan berkelanjutan.")
    st.write("✅Grafik Aspek Reduced Inequalities mengalami sedikit penurunan skor pada periode 2003-2004 dan kemudian cenderung mengalami kenaikan skor saat periode 2004-2020, dan kembali mengalami penurunan skor dalam jumlah sedikit, sehingga perlu diimprove kembali pada tahun berikutnya.")
    st.write("✅Grafik Sustainable Cities and Communities menunjukkan ketidakstabilan perkembangan skor dari tahun 2000 hingga 2022, dengan adanya fluktuasi yang mencakup peningkatan dan penurunan skor sehingga perlu tindakan untuk menstabilkan dan meningkatkan skor di tahun berikutnya.")
    st.write("✅Aspek Responsible Consumption and Production menggambarkan ketidakstabilan perkembangan skor yang ditandai dengan peningkatan dan penurunan dengan selisih dan jangka waktu yang tidak konsisten, sehingga perlu dilakukan upaya yang dapat menstabilkan pertumbuhan skor di tahun berikutnya.")
    st.write("✅Aspek Climate Action mengalami fluktuasi skor dari tahun 2000 hingga 2022, dengan peningkatan dan penurunan yang tidak stabil, mencerminkan tantangan yang kompleks dalam mencapai tujuan aksi iklim yang konsisten.")
    st.write("✅Aspek Life Below Water cenderung mengalami peningkatan skor, dengan hanya satu penurunan skor yang tercatat.")
    st.write("✅Aspek Life on Land menunjukan grafik yang cenderung meningkat dari tahun 2001-2017, dan hanya terjadi dua kali penurunan skor.")
    st.write("✅Grafik Peace, Justice, and Strong Institutions menggambarkan adanya penurunan skor sebanyak empat kali pada periode tahun yang berbeda.")
    st.write("✅Grafik dari Partnership for The Goals menggambarkan pertumbuhan grafik yang naik secara perlahan, namun terjadi penurunan skor sebanyak dua kali pada jarak dan rentang waktu yang berbeda.")
    st.write("✅Terlihat pola serupa pada semua aspek SDG, yaitu usaha yang dilakukan mulai tahun 2020 cenderung berkurang dibandingkan dengan tahun-tahun sebelumnya. Ini tercermin dalam grafik skor yang cenderung mendatar sejak tahun 2020.")
             

    st.divider()
    kolom = ["overall_score"] + [f"goal_{i}_score" for i in range(1, 18)]
    data_korelasi = df2023[kolom]
    matrix_corr = data_korelasi.corr()
    matrix_corr = matrix_corr.drop("overall_score", axis=0)
    matrix_corr = matrix_corr.drop("overall_score", axis=1)
    st.header("Heatmap Korelasi Skor Aspek SDGs")
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
    st.write("✅Melalui analisis heatmap, ditemukan fakta terkait skor-skor tujuan SDG, yaitu terdapat hubungan korelasi yang unik, baik positif maupun negatif, antara beberapa skor. Berikut adalah korelasi skor-skor SDG.")
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

    st.write("Jika diurutkan berdasarkan skor aspek SDG terbesar maka akan menjadi sebagai berikut.")
    indonesia_kolumsort = [f'goal_{i}_score' for i in range(1,18)]
    skor = indonesia[indonesia_kolumsort].mean().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    bar_chart = sns.barplot(x=skor.index, y=skor.values)
    bar_chart.set(xlabel="Goals", ylabel="Score")
    plt.title("Skor Indonesia di 2023 Terurut")
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())
    plt.close()
    st.write("✅Indonesia mencapai skor SDG tertinggi dalam sektor Climate Action, Quality Education, dan Responsible Consumption and Production. Namun, analisis ini juga mengungkapkan bahwa Indonesia perlu menekankan upaya lebih lanjut pada sektor-sektor seperti Partnership for The Goals, Life on Land, dan Industry Innovation and Infrastructure, guna mencapai tujuan pembangunan berkelanjutan yang lebih holistik dan inklusif.")
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
    st.write("✅Melalui analisis linechart mengenai skor SDG Indonesia dari tahun ke tahun, dapat disimpulkan bahwa secara rata-rata, nilai SDG di Indonesia mengalami perkembangan yang terbatas hingga tahun 2012. Setelah tahun 2012, terlihat peningkatan skor yang lebih signifikan.")
    st.write("✅Dalam aspek No Poverty, terdapat perkembangan pesat mulai tahun 2010. Sebelumnya, skor No Poverty berada di kisaran 60, namun mulai tahun 2010, skornya terus meningkat hingga melebihi angka 80.")
    st.write("✅Skor dalam aspek Reduced Inequalities mengalami penurunan yang signifikan, terutama pada tahun 2010-2011, yang mengakibatkan penurunan dari sekitar 90 menjadi sekitar 60. Ini menandakan perlunya perbaikan segera dalam upaya mengurangi ketidaksetaraan.")
    st.write("✅Selain itu, aspek Life on Land juga memerlukan perhatian lebih lanjut. Dalam rentang tahun 2000 hingga 2022, terjadi sedikit perubahan dan skor yang rendah yakni sekitar 40. Oleh karena itu, perlu upaya lebih besar untuk menjaga dan memulihkan ekosistem daratan.")
    st.write("✅Secara keseluruhan, banyak tujuan SDG di Indonesia yang masih memerlukan usaha lebih lanjut dari pemerintah, terlihat dari grafik yang cenderung datar pada setiap aspek SDG.")

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

#background
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1483401757487-2ced3fa77952?ixlib=rb-4.0.3");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

st.markdown(
    """
    ---
    <p style='font-size:14px;'>Made with ❤️ by PisangGorengRaja Team.<br>
    Source of dataset: <a href='https://www.kaggle.com/datasets/sazidthe1/sustainable-development-report' target='_blank'>Sustainable Development Report Dataset</a></p>
    """,
    unsafe_allow_html=True
)



    
