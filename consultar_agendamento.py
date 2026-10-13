import streamlit as st
from supabase import create_client
import pandas as pd

url = "https://vipdiqtdphlgjguvfvin.supabase.co"
key = "sb_publishable_rbn7362MHq23n_sCJiJqPw_UHGmEtFh"
postgree = create_client(url,key)

st.title("Consulta de agendamento")

@st.cache_data
def carregar_dados():
    response = postgree.table("agendamento").select("*").execute()

    dados = response.data

    df = pd.DataFrame(dados)
    return df 

df_tabela = carregar_dados()

if not df_tabela.empty:
    st.dataframe(df_tabela)

else:
    st.error("Nenhum registro no momento")