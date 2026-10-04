import streamlit as st

def pegar_id_usuario_logado():
    return st.session_state["usuario_id"]