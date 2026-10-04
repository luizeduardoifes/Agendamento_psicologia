import streamlit as st

def usuario_logado():
    booleano =  bool(st.session_state.get("usuario_id"))
    id_usuario = st.session_state.get("usuario_id")

    return booleano, id_usuario