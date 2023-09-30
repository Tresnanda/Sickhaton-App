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
df2023['year'] = 2023

menu_option = st.sidebar.radio("Choose Language:", ["English", "Indonesian"])
if menu_option == "English":
    with st.sidebar:
        selected = option_menu("SDG Score Insights", ['Country Insights', 'Indonesian Insight', 'SDG Score Prediction'], icons=['bar-chart-fill', 'bar-chart-fill', 'bar-chart-fill'], default_index=1)
        selected

    if selected == 'Country Insights':
        st.markdown(f"<h1 style='text-align:center;'>Analysis of Sustainable Development Goals in 2023 Countries</h1>",unsafe_allow_html=True)

        st.divider()
        st.header("10 countries with the highest average scores on SDGs aspects in 2023")
    

        #st.dataframe(df2023)
        #df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']] = pd.to_numeric(df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']], errors='coerce').fillna(0).astype(int)
    
        sns.set(font_scale=0.75)
        plot_top10 = sns.barplot(data=df2023.sort_values(by="overall_score", ascending=False).head(10), x="country", y="overall_score")
        plt.xticks(rotation=45)
        st.pyplot(plot_top10.get_figure())
        st.write ("✅Based on this diagram, Finland is ranked first with the highest average score of all aspects of the SDGs based on 2023 data.")
        st.write("✅The top 10 countries in the ranking belong to the Continental Europe region with an average score above 80%, indicating that the region has made efforts to pursue the 17 SDGs goals by 2030.")
        plt.close()
        st.divider()

        st.header("10 countries with the lowest average scores on SDGs by 2023")
    

        #st.dataframe(df2023)
        #df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']] = pd.to_numeric(df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']], errors='coerce').fillna(0).astype(int)
    
        sns.set(font_scale=0.50)
        plot_top10 = sns.barplot(data=df2023.sort_values(by="overall_score", ascending=False).head(10), x="country", y="overall_score")
        plt.xticks(rotation=45)
        st.pyplot(plot_top10.get_figure())
        st.write ("✅Based on the diagram, South Sudan occupies the first position with the lowest average score of all aspects of the SDGs based on 2023 data.")
        st.write("✅The 10 countries in the ranking are classified into 8 countries that belong to the African continent including South Sudan, Central African Republic, Chad, Somalia, Niger, Sudan, Congo, and Liberia. The remaining 2 countries, Yemen Rep and Afghanistan, belong to the Asian continent. The two continental regions have a score below 50, so efforts must be made to improve the score of achieving the 17 Aspects of SDGs in the following year.")
        plt.close()
        st.divider()

        st.header("Distribution of Number of Countries by Region Category")
        #region_counts = df2023.groupby('region')['country'].count().reset_index()
        region_counts = df2023['region'].value_counts().reset_index()
        region_counts.columns = ['region', 'country']
        plt.figure(figsize=(10, 6))
        sns.barplot(data=region_counts, x='region', y='country', palette='viridis')
        plt.xlabel("Region")
        plt.ylabel("Number of Countries")
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf()) 
        plt.close()
        st.write("✅Based on the bar chart above, Sub-Saharan Africa is the region category with the largest distribution of countries in the SDGs growth report data in 2023.")
        st.write("✅Meanwhile, the Oceania region is the region category with the least number of countries in the 2023 SDGs growth report data.")
        st.write("✅The E.Europe & C.Asia Region and LAC Region are the two regions with the same number of countries based on the SDGs growth report data in 2023.")
        st.divider()
        st.header("Ratio of Average Value of All Aspects of SDGs in Each Region")
        plt.figure(figsize=(10, 6))

        sns.set(font_scale=1)
        region_score = df2023.groupby('region')['overall_score'].mean().reset_index()
        bar_region = sns.barplot(data=region_score.sort_values(by='overall_score', ascending=False), x="region", y="overall_score")
        bar_region.set(xlabel="Region", ylabel="Skor Rata-Rata")
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf())
        plt.close()
        st.write("✅Countries that are members of the Organization for Economic Co-operation and Development (OECD) show much higher average achievement in achieving the SDGs compared to other regions around the world. On the other hand, the Sub-Saharan Africa region, with the lowest average SDG score, is the focus of attention in working towards achieving the sustainable development goals. For example, Finland, which stands out as the country with the highest SDG score, is one of the leading members of this OECD group.")
        st.write("✅Although Sub-Saharan Africa has the largest number of countries, the average Sustainable Development Index (SDG) score in this region is the lowest. On the other hand, the OECD Region with the second highest number of countries recorded the highest average SDG score. This reflects the strong commitment of OECD countries in achieving the SDG goals.")
        st.divider()

        goal_means = df2023[[f"goal_{i}_score" for i in range(1, 18)]].mean()
        goal_means = goal_means.sort_values(ascending=False)
        st.header("Average goal scores of countries")
        plt.figure(figsize=(12, 6))
        bar_rata = sns.barplot(x=goal_means.values, y=goal_means.index, palette="viridis")
        bar_rata.set(xlabel="Mean Score", ylabel="Goals")
        st.pyplot(plt.gcf())
        high_scoring_goals = goal_means[goal_means >= goal_means.mean()]
        low_scoring_goals = goal_means[goal_means < goal_means.mean()]
        st.write("✅Overall, most countries have done well in achieving SDG goals such as Goal 13 (Climate Action), Goal 12 (Responsible Consumption and Production), and Goal 4 (Quality Education), with average scores in the top ranks.")
        st.write("✅However, there are significant challenges in achieving Goal 14 (Life Below Water), Goal 9 (Industry, Innovation, and Infrastructure), Goal 10 (Reduced Inequalities), and Goal 2 (Zero Hunger), which still record low average scores. This suggests that further expansion of efforts and focus on key aspects of sustainable development that still require serious attention and concerted action.")
        st.divider()

        feature_map2 = {
            'Average score': 'overall_score',
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
        st.header("SDG Score Progress from 2000 - 2022")
        pilihan = st.selectbox('Select Score Type', list(feature_map2.keys()), key='select-type', index=0)
        kolom_pilihan = feature_map2[pilihan]
        rata_pil = df2000.groupby('year')[kolom_pilihan].mean().reset_index()
        plt.figure(figsize=(10, 6))
        plt.plot(rata_pil['year'], rata_pil[kolom_pilihan], marker='o', linestyle='-', color='b')
        plt.xlabel("Year")
        plt.ylabel("Overall Score")
        plt.xticks(rotation=45)
        plt.title("Average SDG Score from Year to Year")
        plt.grid(True)
        #plt.ylim(30, 90)
        st.pyplot(plt.gcf())
        plt.close()
        if feature_map2[pilihan] == 'overall_score':
            st.write("✅Based on the graph of the average score of all aspects of the SDGs in the period 2000 to 2022, it shows that there is a consistent upward growth every year, illustrating the increasing efforts made by countries in pursuing the 2030 SDG targets.")
            st.write("✅There is a similar pattern in all aspects of the SDGs, where efforts made starting in 2020 tend to decrease compared to previous years. This is reflected in the score graph which tends to flatten since 2020.")
    
        elif feature_map2[pilihan] == 'goal_1_score':
            st.write("✅In the SDG Goal Aspect (No Poverty), there was no significant increase from 2000 to 2010, but there was a very sharp increase from 2010 to 2019 which indicated a decrease in poverty, then there was a decrease in scores in the 2019-2020 period due to the co-19 pandemic which caused an increase in poverty, but in the 2019-2022 period there was a recovery in poverty levels marked by an increase in scores.") 
        elif feature_map2[pilihan] == 'goal_2_score':
            st.write("✅In the Zero Hunger Goal Aspect, there is inconsistency in the development of scores in some periods of the year, thus requiring expanded efforts to increase the stability of scores in achieving this SDG goal in the following year.")
        elif feature_map2[pilihan] == 'goal_3_score':
            st.write("✅The Good Health and Well Being graph shows a steady increase from 2000 to 2019, but there was a slight decrease in scores in the 2019-2022 period due to the Covid-19 Pandemic which affected the level of human health so that it had an impact on reducing the quality of Healthy and Prosperous Life.")
        elif feature_map2[pilihan] == 'goal_4_score':
            st.write("✅The Quality Education graph has increased consistently in the 2000-2020 period, but there was a slight decrease in the quality of education in the 2020-2022 period, indicating that there needs to be an improvement in the quality of education in the following year.")
        elif feature_map2[pilihan] == 'goal_5_score':
            st.write("✅The Gender Quality aspect shows a steady upward graph from the period 2000-2022 reflecting continued progress in achieving gender equality.")
        elif feature_map2[pilihan] == 'goal_6_score':
            st.write("✅The Clean Water and Sanitation aspect shows a consistent increase in score growth from 2000 to 2020, but there is a slight decrease in score from 2020-2022 so that maintenance and continuous monitoring efforts are needed in maintaining access to clean water and good sanitation to increase the score again the following year.")
        elif feature_map2[pilihan] == 'goal_7_score':
            st.write("✅The Affordable and Clean Energy aspect saw a consistent increase in scores from 2000 to 2020, reflecting positive steps in the development of clean and affordable energy sources. However, the slight decline in the period 2020-2022 indicates the need to monitor and adapt to the changing dynamics in the global energy sector, which may affect the accessibility and sustainability of clean energy sources in the following years.")
        elif feature_map2[pilihan] == 'goal_8_score':
            st.write("✅The Decent Work and Economic Growth graph shows an unstable development of scores over several periods, with fluctuations between increases and decreases. This may reflect the complex challenges faced in achieving inclusive economic growth and creating decent work.")
        elif feature_map2[pilihan] == 'goal_9_score':
            st.write("✅The Industry, Innovation and Infrastructure graph shows a consistent upward increase in scores over the period 2000-2022, reflecting successful efforts to develop the industry, innovation and infrastructure sectors, which have a positive impact on economic growth and sustainable development.")
        elif feature_map2[pilihan] == 'goal_10_score':
            st.write("✅The graph of the Reduced Inequalities Aspect experienced a slight decrease in score in the 2003-2004 period and then tended to increase in score during the 2004-2020 period, and again experienced a slight decrease in score, so it needs to be improved again in the following year.")
        elif feature_map2[pilihan] == 'goal_11_score':
            st.write("✅The Sustainable Cities and Communities graph shows instability in the development of scores from 2000 to 2022, with fluctuations that include both increases and decreases in scores that require action to stabilize and improve scores in the following year.")
        elif feature_map2[pilihan] == 'goal_12_score':
            st.write("✅The Responsible Consumption and Production aspect illustrates the instability of score development characterized by increases and decreases with inconsistent differences and timeframes, so efforts need to be made to stabilize score growth in the following year.")
        elif feature_map2[pilihan] == 'goal_13_score':
            st.write("✅The Climate Action aspect experienced fluctuations in scores from 2000 to 2022, with volatile increases and decreases, reflecting the complex challenges of achieving consistent climate action goals.")
        elif feature_map2[pilihan] == 'goal_14_score':
            st.write("✅The Life Below Water aspect tends to see an increase in scores, with only one decrease recorded.")
        elif feature_map2[pilihan] == 'goal_15_score':
            st.write("✅The Life on Land aspect shows a graph that tends to increase from 2001-2017, and there were only two decreases in the score.")
        elif feature_map2[pilihan] == 'goal_16_score':
            st.write("✅The Peace, Justice, and Strong Institutions graph illustrates that the score has dropped four times in different years.")
        elif feature_map2[pilihan] == 'goal_17_score':
            st.write("✅The graph from Partnership for the Goals depicts a slowly growing graph, but there were two drops in scores at different distances and timescales.")
            
        st.divider()
        kolom = ["overall_score"] + [f"goal_{i}_score" for i in range(1, 18)]
        data_korelasi = df2023[kolom]
        matrix_corr = data_korelasi.corr()
        matrix_corr = matrix_corr.drop("overall_score", axis=0)
        matrix_corr = matrix_corr.drop("overall_score", axis=1)
        st.header("SDGs Aspect Score Correlation Heatmap")
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
        st.write("✅Through the heatmap analysis, it was found that there are unique correlations, both positive and negative, between some of the SDG scores. The following is the correlation of the SDG scores.")
        if high_correlation_pairs:
            st.subheader("Highly correlated pairs (|correlation score|>0.7):")
            for pair in high_correlation_pairs:
                st.write(f"{pair[0]} with {pair[1]}: {pair[2]:.2f}")
        else:
            st.subheader("There are no pairs with high correlation")
        
        st.divider()

        st.subheader("SDGs Score Comparison between Two Countries")
        # Menambahkan pilihan tahun untuk data tahun 2023 dan 2000-2022
        tahun_option = st.selectbox("Select SDG score data period", ["2023", "2000-2022"])
        tahun = None
        #scores = indonesia_data['overall_score']

        # Memilih dataset berdasarkan tahun yang dipilih
        if tahun_option == "2023":
            tahun = "2023"
            df = df2023
        else:
            tahun = st.selectbox("Select Year (2000-2022):", df2000['year'].unique())
            df = df2000[df2000['year'] == tahun]
            
        negara1 = st.selectbox("Select Country First:", df['country'].unique())
        negara2 = st.selectbox("Select Second Country:", df['country'].unique())

        scores = st.selectbox("Select SDG Aspect:", list(feature_map2.keys()), key='select-type2', index=0)
        selected_column = feature_map2[scores]

        skor_negara1 = df[(df['country'] == negara1)]
        skor_negara2 = df[(df['country'] == negara2)]

        if not skor_negara1.empty and not skor_negara2.empty:
            skor1 = skor_negara1[selected_column].values[0]
            skor2 = skor_negara2[selected_column].values[0]

            # Menampilkan hasil perbandingan skor
            st.write(f"Score {selected_column} in {tahun} for {negara1}: {skor1}")
            st.write(f"Score {selected_column} in {tahun} for {negara2}: {skor2}")

            # Membuat plot perbandingan skor
            plt.figure(figsize=(6, 6))
            bar_width = 0.35
            r1 = [1]
            r2 = [2]
            plt.bar(r1, [skor1], color='b', width=bar_width, edgecolor='grey', label=negara1)
            plt.bar(r2, [skor2], color='orange', width=bar_width, edgecolor='grey', label=negara2)
            plt.xlabel('Country', fontweight='bold')
            plt.ylabel(f'Score {selected_column}', fontweight='bold')
            plt.xticks([r + bar_width / 2 for r in r1 + r2], [negara1, negara2])
            plt.title(f'Score Comparison {selected_column} between {negara1}, {negara2} ({tahun})')
            plt.legend()
            plt.show()
            st.pyplot(plt.gcf())
        else:
            st.write(f"There is no data for {negara1} or {negara2} in {tahun}.")

    elif selected == 'Indonesian Insight':
        st.markdown(f"<h1 style='text-align:center;'>Analysis of Indonesia's Sustainable Development Goals 2023</h1>",unsafe_allow_html=True)
        st.divider()
        st.header("Indonesia's SDG Score Statistics")
        indonesia = df2023[df2023['country'] == 'Indonesia']
        selected_columns = ["overall_score"] + [f"goal_{i}_score" for i in range(1, 18)]
        plt.figure(figsize=(12, 6))
        bar_chart = sns.barplot(data=indonesia[selected_columns], palette="viridis")
        bar_chart.set(xlabel="Goals", ylabel="Score")
        plt.title("Indonesia's score in 2023")
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf())

        st.write("If sorted based on the largest SDG aspect score it would be as follows.")
        indonesia_kolumsort = [f'goal_{i}_score' for i in range(1,18)]
        skor = indonesia[indonesia_kolumsort].mean().sort_values(ascending=False)
        plt.figure(figsize=(12, 6))
        bar_chart = sns.barplot(x=skor.index, y=skor.values)
        bar_chart.set(xlabel="Goals", ylabel="Score")
        plt.title("If sorted by the largest SDG aspect score, it would be as follows.")
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf())
        plt.close()
        st.write("✅Indonesia achieved the highest SDG scores in the Climate Action, Quality Education, and Responsible Consumption and Production sectors. However, the analysis also reveals that Indonesia needs to emphasize further efforts on sectors such as Partnership for the Goals, Life on Land, and Industry Innovation and Infrastructure, in order to achieve more holistic and inclusive sustainable development goals.")
        st.divider()

        st.header("Indonesia's SDG score progress")
        indonesia_data = df2000[df2000['country'] == 'Indonesia']
        years = indonesia_data['year']

        #scores = indonesia_data['overall_score']
        feature_map2 = {
            'Average scores': 'overall_score',
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

        scores = st.selectbox('Select Score Type', list(feature_map2.keys()), key='select-type2', index=0)
        selected_column = feature_map2[scores]
        indonesia_data[selected_column] = indonesia_data[selected_column].astype(float)
        #indonesia_data[scores] = indonesia_data[scores].astype(float)
        plt.figure(figsize=(10, 6))
        plt.plot(years, indonesia_data[selected_column], marker='o', linestyle='-', color='b')
        plt.xlabel("Year")
        plt.ylabel("Overall Score")
        plt.xticks(rotation=45)
        plt.title("Indonesia's Average Score SDG from Year to Year")
        plt.grid(True)
        plt.ylim(0, 100)
        st.pyplot(plt.gcf())
        plt.close()
        if feature_map2[scores] == 'overall_score':
            st.write("✅Through a linechart analysis of Indonesia's SDG scores from year to year, it can be concluded that on average, Indonesia's SDG scores experienced limited progress until 2012. After 2012, there was a more significant increase in scores.")
            st.write("✅Overall, many SDG goals in Indonesia still require further efforts from the government, as seen from the graphs that tend to be flat in each aspect of SDG and the overall score is still below 80 in 2022, it needs to be a serious concern for the Indonesian government, especially in improving 13 aspects of SDGS which are still below the score of 80 such as the zero hunger aspect, Good Health and Well Being, Gender Equality, Clean Water and Sanitation, Affordable and clean energy, Decent Work and Economic Growth, Industry Innovation and Infrastructure, Reduced Inequalities, Sustainable Cities and Communities, Life Below Water, Life on Land, Peace Justice and Strong institutions, and Partnership for the Goals.")
        if feature_map2[scores] == 'goal_1_score':
            st.write("✅In terms of No Poverty, there was rapid progress starting in 2010. Initially the No Poverty score was below 60 in 2010, but in 2011 the score increased consistently to over 80.")
        if feature_map2[scores] == 'goal_2_score':
            st.write("✅The Zero Hunger aspect has inconsistent score development and the score will still be below 80 in 2022. Therefore, concrete actions are needed to reduce the problem of hunger and malnutrition so as to increase the No Hungry score in the following year.")
        if feature_map2[scores] ==  'goal_3_score':
            st.write("✅The Good Health and Well Being aspect saw an increase in the score from below 60 in 2000 to above 60 in 2022, with a record of the decline and increase that occurred during the 2000-2022 period. Seeing that the score is still below 80, the government must make strategic efforts to improve the health and welfare of the community so as to increase the value of the SDG Good Health and Well Being.") 
        if feature_map2[scores] == 'goal_4_score':
            st.write("✅The Quality Education aspect represents a good score of above 80 in 2022. However, the increase obtained from 2000 to 2022 is not too significant. This is because in 2000 the score reached above 80, then there was a decline and increase, until finally it stabilized for 6 years starting from 2016 to 2022.")
        if feature_map2[scores] == 'goal_5_score':
            st.write("✅The Gender Equality aspect shows an increase in score from 2000, which was still below 60, to above 60 in the 2016-2022 period. This shows that Indonesia is still not perfect in overcoming problems related to gender equality.")
        if feature_map2[scores] == 'goal_6_score':
            st.write("✅The graph related to the clean water and sanitation aspect shows a steady growth increasing from 2000 to 2022 with a score above 60 and close to 80. The Indonesian government must pay attention and improve the quality of clean water and sanitation to all corners of Indonesia to improve the SDG score in the following years.")
        if feature_map2[scores] == 'goal_7_score':
            st.write("✅Based on the graphical data, it can be observed that Indonesia has experienced significant improvement in the aspect of Clean and Affordable Energy since 2000. The score was initially below 40, but has consistently risen to reach the 60 and above range. This increase reflects Indonesia's seriousness in prioritizing clean and affordable energy for its people. The government is expected to continue to be active in addressing issues related to clean and affordable energy through sustainable measures.")
        if feature_map2[scores] == 'goal_8_score' :
            st.write("✅The graph above informs that the Decent Work and Economic Growth aspect experienced stable development in the 2000-2007 period, then experienced a slow increase in the 2007-2022 period with a score close to 80. This reflects Indonesia's commitment to creating an economic environment that supports sustainable growth and decent work for its population.")
        if feature_map2[scores] == 'goal_9_score' :
            st.write("✅The graph illustrates the increase in scores in Industry, Innovation and Infrastructure, which initially stabilized in the 2000-2009 period below 20, but saw a rapid surge approaching 60 in the 2010-2022 period. This growth reflects Indonesia's serious efforts to develop the industry, innovation and infrastructure sectors, which have a positive impact on the economy and society.")
        if feature_map2[scores] == 'goal_10_score' :
            st.write("✅The score in the Reduced Inequalities aspect experienced a significant decline, especially in 2010-2011, which resulted in a drop from around 90 to around 60. This signals the need for immediate improvement in efforts to reduce inequalities in society.")
        if feature_map2[scores] == 'goal_11_score' :
            st.write("✅The graph above shows that the sustainable cities and communities aspect has experienced growth from below 60 in 2000, but has increased to a score close to 80. This reflects the serious efforts of the government and society in creating a sustainable urban environment and healthy communities.")
        if feature_map2[scores] == 'goal_12_score' :
            st.write("✅The Responsible Consumption and Production aspect represents a stable score above 80 from 2000-2022. This achievement reflects Indonesia's seriousness in facing global challenges related to sustainable consumption and production.")
        if feature_map2[scores] == 'goal_13_score' :
            st.write("✅The Climate Action spec shows a stable score from 2000-2000 with a score above 80. This achievement reflects Indonesia's strong commitment in facing climate change and mitigating its impacts.")
        if feature_map2[scores] == 'goal_14_score' :
            st.write('✅The graph shows that the Life Below Water aspect has consistently increased from a score below 60 in 2000 to above 60 in 2022. This reflects the consistent improvement of Life Below Water from a score below 60 in 2000 to above 60 in 2022. As a maritime country, this reflects the commitment of the Indonesian government and society to protect marine life, biota diversity and underwater ecosystems.')
        if feature_map2[scores] == 'goal_15_score' :
            st.write("✅Looking at the graph, the Life on Land aspect requires further attention from the Indonesian government. From 2000 to 2022, there has been little change and the score is low at around 40. Therefore, greater efforts are needed to maintain and restore the terrestrial ecosystem.")
        if feature_map2[scores] == 'goal_16_score' :
            st.write('✅Based on the graph, it can be seen that the score was stable at around 60 in the 2000-2007 period, which was then followed by fluctuations in increase and decrease in the 2008-2022 period, but the final score remained at around 60. This phenomenon illustrates that Indonesia still needs to improve peace, justice and realize strong institutions.') 
        if feature_map2[scores] == 'goal_17_score' :
            st.write('✅Based on the graph, the aspect of Partnership for the Goals did not experience a significant increase, marked by a score that was still below 60 during the 2000-2022 period. This shows that Indonesia must make strategic efforts in facing challenges to build strong partnerships to achieve sustainable development goals.')

    elif selected == 'SDG Score Prediction':
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
        st.markdown(f"<h1 style='text-align:center;'>Predicted SDG Scores in 2030</h1>",unsafe_allow_html=True)
        st.divider()
        negara = st.selectbox('Select Country', list(country_mapping.keys()), key='select-type3', index=0)
        selected_negara = country_mapping[negara]
        predict_input = [[selected_negara, 2030]]

        predict = model.predict(predict_input)
        st.write(f"The SDGS score for {negara} in 2030 is {predict[0]}")

elif menu_option == "Indonesian":
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
        plot_top10 = sns.barplot(data=df2023.sort_values(by="overall_score", ascending=False).head(10), x="country", y="overall_score")
        plt.xticks(rotation=45)
        st.pyplot(plot_top10.get_figure())
        st.write ("✅Berdasarkan diagram tersebut, Negara Finlandia menduduki peringkat pertama dengan perolehan rata-rata nilai tertinggi dari seluruh aspek SDGs berdasarkan data tahun 2023.")
        st.write("✅10 Negara dalam peringkat teratas termasuk kategori wilayah Benua Eropa dengan nilai rata-rata di atas 80% sehingga menunjukan bahwa kawasan tersebut telah melakukan upaya dalam mengejar 17 tujuan SDGs di tahun 2030.")
        plt.close()
        st.divider()

        st.header("10 Negara dengan nilai rata-rata terendah aspek SDGs di tahun 2023")
    

        #st.dataframe(df2023)
        #df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']] = pd.to_numeric(df2023[['overall_score', 'goal_1_score', 'goal_2_score', 'goal_3_score', 'goal_4_score', 'goal_5_score', 'goal_6_score', 'goal_7_score', 'goal_8_score', 'goal_9_score', 'goal_10_score','goal_11_score', 'goal_12_score', 'goal_13_score', 'goal_14_score', 'goal_15_score', 'goal_16_score', 'goal_17_score']], errors='coerce').fillna(0).astype(int)
    
        sns.set(font_scale=0.50)
        plot_top10 = sns.barplot(data=df2023.sort_values(by="overall_score", ascending=True).head(10), x="country", y="overall_score")
        plt.xticks(rotation=45)
        st.pyplot(plot_top10.get_figure())
        st.write ("✅Berdasarkan diagram tersebut, Negara South Sudan menempati posisi pertama dengan perolehan rata-rata nilai terendah dari seluruh aspek SDGs berdasarkan data tahun 2023.")
        st.write("✅10 Negara pada peringkat tersebut diklasifikasikan menjadi 8 negara yang termasuk kawasan benua Afrika meliputi South Sudan, Central African Republic, Chad, Somalia, Niger, Sudan, Congo, dan Liberia. Sisa 2 Negara yakni Yemen Rep dan Afganistan termasuk kawasan benua Asia. Dua kawasan benua tersebut memiliki skor di bawah 50, sehingga wajib dilakukan upaya dalam meningkatkan skor pencapaian 17 Aspek SDGs di tahun berikutnya.")
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
        st.header("Perkembangan Skor SDG dari Tahun 2000 - 2022")
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
        if feature_map2[pilihan] == 'overall_score':
            st.write("✅Berdasarkan grafik skor rata-rata dari seluruh aspek SDG pada periode tahun 2000 sampai 2022 menunjukan bahwa terjadi pertumbuhan yang terus naik dengan konsisten di setiap tahunnya sehingga menggambarkan peningkatan usaha yang dilakukan oleh negara-negara dalam mengejar target SDGs 2030.")
            st.write("✅Terlihat pola serupa pada semua aspek SDG, yaitu usaha yang dilakukan mulai tahun 2020 cenderung berkurang dibandingkan dengan tahun-tahun sebelumnya. Ini tercermin dalam grafik skor yang cenderung mendatar sejak tahun 2020.")
        elif feature_map2[pilihan] == 'goal_1_score':
            st.write("✅Pada Aspek Tujuan SDG (No Poverty) tidak mengalami peningkatan yang signifikan pada tahun 2000 sampai 2010, namun terjadi peningkatan yang sangat tajam dari tahun 2010 sampai 2019 yang mengindikasikan penurunan angka kemiskinan, kemudian terjadi penurunan skor pada periode 2019-2020 akibat pandemi covid-19 sehingga menyebabkan meningkatnya angka kemiskinan, akan tetapi pada periode 2019-2022 terjadi pemulihan tingkat kemiskinan yang ditandai oleh meningkatnya skor.") 
        elif feature_map2[pilihan] == 'goal_2_score':
            st.write("✅Pada Aspek Tujuan Zero Hunger, terjadi ketidakkonsistenan perkembangan skor pada beberapa periode tahun, sehingga memerlukan perluasan upaya yang untuk meningkatkan stabilitas skor dalam pencapaian tujuan SDG ini pada tahun berikutnya.")
        elif feature_map2[pilihan] == 'goal_3_score':
            st.write("✅Grafik Good Health and Well Being menunjukan peningkatan yang stabil dari tahun 2000 sampai tahun 2019, namun terjadi sedikit penurunan skor pada periode 2019-2022 hal itu disebabkan oleh Pandemi Covid-19 yang memengaruhi tingkat kesehatan manusia sehingga berdampak pada penurunan kualitas Kehidupan Sehat dan Sejahtera.")
        elif feature_map2[pilihan] == 'goal_4_score':
            st.write("✅Grafik Quality Education mengalami kenaikan secara konsisten pada periode 2000-2020, namun terjadi sedikit penurunan kualitas pendidikan pada periode 2020-2022 hal itu menunjukan perlu ada perbaikan kualitas pendidikan pada tahun berikutnya.")
        elif feature_map2[pilihan] == 'goal_5_score':
            st.write("✅Aspek Gender Quality menunjukan grafik yang stabil naik dari periode tahun 2000-2022 mencerminkan kemajuan yang berkelanjutan dalam upaya mencapai kesetaraan gender.")
        elif feature_map2[pilihan] == 'goal_6_score':
            st.write("✅Aspek Clean Water and Sanitation menunjukan pertumbuhan skor yang meningkat konsisten dari tahun 2000 sampai tahun 2020, namun terjadi sedikit penurunan skor dari tahun 2020-2022 sehingga perlu upaya pemeliharaan dan pemantauan berkelanjutan dalam menjaga akses air bersih dan sanitasi yang baik untuk meningkatkan kembali skor pada tahun berikutnya.")
        elif feature_map2[pilihan] == 'goal_7_score':
            st.write("✅Aspek Affordable and Clean Energy mengalami peningkatan skor yang konsisten dari tahun 2000 hingga 2020, mencerminkan langkah-langkah positif dalam pengembangan sumber energi yang bersih dan terjangkau. Namun, terjadinya sedikit penurunan pada periode 2020-2022 menunjukkan perlunya pemantauan dan adaptasi terhadap dinamika perubahan dalam sektor energi global, yang dapat memengaruhi aksesibilitas dan keberlanjutan sumber energi bersih di tahun berikutnya.")
        elif feature_map2[pilihan] == 'goal_8_score':
            st.write("✅Grafik Decent Work and Economic Growth menunjukkan perkembangan skor yang tidak stabil dari beberapa periode, dengan fluktuasi antara peningkatan dan penurunan. Hal ini mungkin mencerminkan tantangan kompleks yang dihadapi dalam mencapai pertumbuhan ekonomi yang inklusif dan menciptakan lapangan kerja yang layak.")
        elif feature_map2[pilihan] == 'goal_9_score':
            st.write("✅Grafik Industry, Innovation and Infrastructure menunjukan peningkatan skor yang cenderung naik dan konsisten pada periode tahun 2000-2022, Hal ini mencerminkan upaya yang berhasil dalam mengembangkan sektor industri, inovasi, dan infrastruktur, yang memiliki dampak positif pada pertumbuhan ekonomi dan perkembangan berkelanjutan.")
        elif feature_map2[pilihan] == 'goal_10_score':
            st.write("✅Grafik Aspek Reduced Inequalities mengalami sedikit penurunan skor pada periode 2003-2004 dan kemudian cenderung mengalami kenaikan skor saat periode 2004-2020, dan kembali mengalami penurunan skor dalam jumlah sedikit, sehingga perlu diimprove kembali pada tahun berikutnya.")
        elif feature_map2[pilihan] == 'goal_11_score':
            st.write("✅Grafik Sustainable Cities and Communities menunjukkan ketidakstabilan perkembangan skor dari tahun 2000 hingga 2022, dengan adanya fluktuasi yang mencakup peningkatan dan penurunan skor sehingga perlu tindakan untuk menstabilkan dan meningkatkan skor di tahun berikutnya.")
        elif feature_map2[pilihan] == 'goal_12_score':
            st.write("✅Aspek Responsible Consumption and Production menggambarkan ketidakstabilan perkembangan skor yang ditandai dengan peningkatan dan penurunan dengan selisih dan jangka waktu yang tidak konsisten, sehingga perlu dilakukan upaya yang dapat menstabilkan pertumbuhan skor di tahun berikutnya.")
        elif feature_map2[pilihan] == 'goal_13_score':
            st.write("✅Aspek Climate Action mengalami fluktuasi skor dari tahun 2000 hingga 2022, dengan peningkatan dan penurunan yang tidak stabil, mencerminkan tantangan yang kompleks dalam mencapai tujuan aksi iklim yang konsisten.")
        elif feature_map2[pilihan] == 'goal_14_score':
            st.write("✅Aspek Life Below Water cenderung mengalami peningkatan skor, dengan hanya satu penurunan skor yang tercatat.")
        elif feature_map2[pilihan] == 'goal_15_score':
            st.write("✅Aspek Life on Land menunjukan grafik yang cenderung meningkat dari tahun 2001-2017, dan hanya terjadi dua kali penurunan skor.")
        elif feature_map2[pilihan] == 'goal_16_score':
            st.write("✅Grafik Peace, Justice, and Strong Institutions menggambarkan adanya penurunan skor sebanyak empat kali pada periode tahun yang berbeda.")
        elif feature_map2[pilihan] == 'goal_17_score':
            st.write("✅Grafik dari Partnership for The Goals menggambarkan pertumbuhan grafik yang naik secara perlahan, namun terjadi penurunan skor sebanyak dua kali pada jarak dan rentang waktu yang berbeda.")
            

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
            st.subheader("Pasangan dengan korelasi tinggi (|skor korelasi|>0.7):")
            for pair in high_correlation_pairs:
                st.write(f"{pair[0]} dengan {pair[1]}: {pair[2]:.2f}")
        else:
            st.subheader("Tidak ada pasangan dengan korelasi tinggi")
        
        st.divider()
        
        st.subheader("Perbandingan Skor SDGs antara Dua Negara")
        # Menambahkan pilihan tahun untuk data tahun 2023 dan 2000-2022
        tahun_option = st.selectbox("Pilih periode data SDG", ["2023", "2000-2022"])
        tahun = None

        # Memilih dataset berdasarkan tahun yang dipilih
        if tahun_option == "2023":
            tahun = "2023"
            df = df2023
        else:
            tahun = st.selectbox("Pilih Tahun (2000-2022):", df2000['year'].unique())
            df = df2000[df2000['year'] == tahun]
        negara1 = st.selectbox("Pilih Negara Pertama:", df['country'].unique())
        negara2 = st.selectbox("Pilih Negara Kedua:", df['country'].unique())
        scores = st.selectbox("Pilih Aspek SDG:", list(feature_map2.keys()), key='select-type2', index=0)
        selected_column = feature_map2[scores]

        skor_negara1 = df[(df['country'] == negara1)]
        skor_negara2 = df[(df['country'] == negara2)]

        if not skor_negara1.empty and not skor_negara2.empty:
            skor1 = skor_negara1[selected_column].values[0]
            skor2 = skor_negara2[selected_column].values[0]

            # Menampilkan hasil perbandingan skor
            st.write(f"Skor {selected_column} pada tahun {tahun} untuk {negara1}: {skor1}")
            st.write(f"Skor {selected_column} pada tahun {tahun} untuk {negara2}: {skor2}")

            # Membuat plot perbandingan skor
            plt.figure(figsize=(6, 6))
            bar_width = 0.35
            r1 = [1]
            r2 = [2]
            plt.bar(r1, [skor1], color='b', width=bar_width, edgecolor='grey', label=negara1)
            plt.bar(r2, [skor2], color='orange', width=bar_width, edgecolor='grey', label=negara2)
            plt.xlabel('Negara', fontweight='bold')
            plt.ylabel(f'Skor {selected_column}', fontweight='bold')
            plt.xticks([r + bar_width / 2 for r in r1 + r2], [negara1, negara2])
            plt.title(f'Perbandingan Skor {selected_column} antara {negara1}, {negara2} ({tahun})')
            plt.legend()
            plt.show()
            st.pyplot(plt.gcf())
        else:
            st.write(f"Tidak ada data untuk {negara1} atau {negara2} pada tahun {tahun}.")

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
        if feature_map2[scores] == 'overall_score':
            st.write("✅Melalui analisis linechart mengenai skor SDG Indonesia dari tahun ke tahun, dapat disimpulkan bahwa secara rata-rata, nilai SDG di Indonesia mengalami perkembangan yang terbatas hingga tahun 2012. Setelah tahun 2012, terlihat peningkatan skor yang lebih signifikan.")
            st.write("✅Secara keseluruhan, banyak tujuan SDG di Indonesia yang masih memerlukan usaha lebih lanjut dari pemerintah, terlihat dari grafik yang cenderung datar pada setiap aspek SDG dan skor secara keseluruhan masih berada di bawah 80 pada tahun 2022, hal itu perlu menjadi perhatian serius bagi pemerintah Indonesia terutama dalam meningkatkan 13 aspek SDGS yang masih berada di bawah skor 80 seperti aspek zero hunger, aspek Good Health and Well Being, aspek Gender Equality, aspek Clean Water and Sanitation, aspek Affordable and clean energy, aspek Decent Work and Economic Grwoth, aspek Industry Innovation and Infrastructure, aspek Reduced Inequalities, aspek Sustainable Cities and Communities, aspek Life Below Water, aspek Life on Land, aspek Peace Justice and Strong institutions, dan aspek Partnership for the Goals.")
        if feature_map2[scores] == 'goal_1_score':
            st.write("✅Dalam aspek No Poverty, terdapat perkembangan pesat mulai tahun 2010. Awalnya skor No Poverty berada di bawah 60 tepat di tahun 2010, namun pada tahun 2011 skornya terus meningkat secara konsisten hingga melebihi angka 80.")
        if feature_map2[scores] == 'goal_2_score':
            st.write("✅Aspek Zero Hunger terjadi perkembangan skor yang tidak konsisten dan skornya masih berada di bawah 80 di tahun 2022. Sehingga perlu tindakan nyata untuk mengurangi masalah kelaparan dan gizi buruk sehingga dapat meningkatkan skor No Hungry di tahun berikutnya.")
        if feature_map2[scores] ==  'goal_3_score':
            st.write("✅Aspek Good Health and Well Being terjadi peningkatan skor yang awalnya di bawah 60 pada tahun 2000, meningkat menjadi di atas angka 60 tepat di tahun 2022, dengan rekaman penurunan dan peningkatan yang terjadi selama periode 2000-2022. Melihat skor masih di bawah angka 80, pemerintah harus melakukan upaya strategis untuk meningkatkan kesehatan dan kesejahteraan masyrakat sehingga meningkatkan nilai SDG Good Health and Well Being.") 
        if feature_map2[scores] == 'goal_4_score':
            st.write("✅Aspek Quality Education menggambarkan skor yang bagus yakni di atas 80 pada tahun 2022. Namun, peningkatan yang diperoleh dari tahun 2000 sampai dengan tahun 2022 tidak terlalu signifikan peningkatan skornya. Hal itu dikarenakan pada tahun 2000 skornya sudah mencapai di atas angka 80, kemudian terjadi penurunan dan peningkatan, sampai akhirnya stabil selama 6 tahun mulai dari tahun 2016 sampai dengan 2022.")
        if feature_map2[scores] == 'goal_5_score':
            st.write("✅Aspek Gender Equality menunjukan peningkatan skor dari tahun 2000 yang masih di bawah angka 60 menjadi di atas 60 pada periode tahun 2016-2022. Hal itu menunjukan Indonesia masih belum sempurna dalam mengatasi masalah-masalah yang terkait kesetaraan Gender.")
        if feature_map2[scores] == 'goal_6_score':
            st.write("✅Grafik terkait aspek clean water and sanitation menunjukan pertumbuhan yang stabil meningkat dari tahun 2000 sampai 2022 dengan skor di atas 60 dan mendekati angka 80. Pemerintah Indonesia harus memperhatikan dan meningkatkan kualitas air bersih dan sanitasi ke seluruh pelosok Indonesia untuk meningkatkan skor SDG di tahun berikutnya.")
        if feature_map2[scores] == 'goal_7_score':
            st.write("✅Berdasarkan data grafik, dapat diamati bahwa Indonesia telah mengalami peningkatan yang signifikan dalam aspek Energi Bersih dan Terjangkau sejak tahun 2000. Skor awalnya berada di bawah 40, namun secara konsisten naik hingga mencapai rentang angka 60 ke atas. Peningkatan ini mencerminkan keseriusan Indonesia dalam memprioritaskan energi yang bersih dan terjangkau bagi masyarakatnya. emerintah diharapkan terus aktif dalam mengatasi masalah-masalah terkait energi bersih dan terjangkau melalui langkah-langkah yang berkelanjutan.")
        if feature_map2[scores] == 'goal_8_score' :
            st.write('✅Grafik di atas menginformasikan bahwa aspek Decent Work and Economic Growth mengalami perkembangan yang stabil pada periode tahun 2000-2007, kemudian mengalami peningkatan secara perlahan pada periode tahun 2007-2022 dengan skor mendekati angka 80. Hal itu mencerminkan komitmen Indonesia untuk menciptakan lingkungan ekonomi yang mendukung pertumbuhan yang berkesinambungan dan pekerjaan yang layak bagi penduduknya.')
        if feature_map2[scores] == 'goal_9_score' :
            st.write('✅Grafik tersebut menggambarkan peningkatan skor di bidang Industry, Innovation and Infrastructure yang awalnya stabil pada periode 2000-2009 di bawah angka 20, namun terjadi lonjakan pesat mendekati angka 60 pada periode 2010-2022. Pertumbuhan ini mencerminkan upaya serius Indonesia dalam mengembangkan sektor industri, inovasi, dan infrastruktur, yang memiliki dampak positif terhadap ekonomi dan masyarakat. ')
        if feature_map2[scores] == 'goal_10_score' :
            st.write("✅Skor dalam aspek Reduced Inequalities mengalami penurunan yang signifikan, terutama pada tahun 2010-2011, yang mengakibatkan penurunan dari sekitar 90 menjadi sekitar 60. Ini menandakan perlunya perbaikan segera dalam upaya mengurangi kesenjangan dalam masyarakat.")
        if feature_map2[scores] == 'goal_11_score' :
            st.write('✅Grafik di atas menunjukan aspek sustainable cities and communities mengalami pertumbuhan yang awalnya di bawah angka 60 pada tahun 2000, namun terjadi peningkatan skor hingga mendekati angka 80. Hal ini mencerminkan upaya serius pemerintah dan masyarakat dalam menciptakan lingkungan kota yang berkelanjutan dan komunitas yang sehat.')
        if feature_map2[scores] == 'goal_12_score' :
            st.write('✅Aspek Responsible Consumption and Production menggambarkan skor yang stabil di atas angka 80 dari tahun 2000-2022. Pencapaian ini mencerminkan kesungguhan Indonesia dalam menghadapi tantangan global terkait konsumsi dan produksi yang berkelanjutan.')
        if feature_map2[scores] == 'goal_13_score' :
            st.write('✅Aspek Climate Action menunjukan kestabilan skor dari tahun 2000-2000 dengan skor di atas 80. Pencapaian ini mencerminkan komitmen kuat Indonesia dalam menghadapi perubahan iklim dan memitigasi dampaknya.')
        if feature_map2[scores] == 'goal_14_score' :
            st.write('✅Grafik menunjukan aspek Life Below Water mengalami peningkatan yang konsisten dari skor di bawah 60 pada tahun 2000 menjadi di atas 60 pada tahun 2022. Hal ini mencerminkan Grafik menunjukan aspek Life Below Water mengalami peningkatan yang konsisten dari skor di bawah 60 pada tahun 2000 menjadi di atas 60 pada tahun 2022. Sebagai negara maritim, hal ini mencerminkan komitmen pemerintah dan masyarakat Indonesia dalam melindungi kehidupan laut, keanekaragaman biota, dan ekosistem bawah air.')
        if feature_map2[scores] == 'goal_15_score' :
            st.write("✅Melihat grafik tersebut, aspek Life on Land memerlukan perhatian lebih lanjut dari pemerintah Indonesia. Dalam rentang tahun 2000 hingga 2022, terjadi sedikit perubahan dan skor yang rendah yakni sekitar 40. Oleh karena itu, perlu upaya lebih besar untuk menjaga dan memulihkan ekosistem daratan.")
        if feature_map2[scores] == 'goal_16_score' :
            st.write('✅Berdasarkan grafik, terlihat adanya kestabilan skor di kisaran 60 pada periode 2000-2007, yang kemudian diikuti oleh fluktuasi peningkatan dan penurunan pada periode 2008-2022, namun skor akhirnya tetap bertahan di kisaran angka 60. Fenomena ini memberikan gambaran bahwa Indonesia masih perlu meningkatkan perdamaian, keadilan dan mewujudkan kelembagaan yang tangguh.') 
        if feature_map2[scores] == 'goal_17_score' :
            st.write('✅Berdasarkan grafik, aspek Partneship for the Goals tidak mengalami peningkatan yang signifikan dengan ditandai skor yang masih di bawah 60 selama periode 2000-2022. Hal ini menunjukan Indonesia harus melakukan upaya strategis dalam menghadapi tantangan untuk membangun kemitraan yang kuat untuk mencapai tujuan pembangunan berkelanjutan.')
       

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
    <p style='font-size:14px;'>Made with ❤️ by SIC HACKATHON Team.<br>
    Source of dataset: <a href='https://www.kaggle.com/datasets/sazidthe1/sustainable-development-report' target='_blank'>Sustainable Development Report Dataset</a></p>
    """,
    unsafe_allow_html=True
)
