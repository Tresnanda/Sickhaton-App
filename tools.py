import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def ganti_nama(df: pd.DataFrame):
    feature_map = {
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
df.