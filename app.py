import streamlit as st

db_user = st.secrets["database"]["user"]
db_password = st.secrets["database"]["password"]


st.write('# Teste')
print(db_user, db_password)
st.write('# Teste 2')