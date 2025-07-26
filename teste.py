import pandas as pd
import streamlit as st

caminho_csv = r'C://docarlos//quadro_flamboyant_teste//teste_streamlit//analise.csv'
df = pd.read_csv(caminho_csv, sep=';', encoding='latin1')
st.dataframe(df)