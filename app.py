import streamlit as st

db_user = st.secrets["database"]["user"]
db_password = st.secrets["database"]["password"]


print(db_user, db_password)