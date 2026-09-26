import streamlit as st
from repo.cliente_repo import criar_tabela_cliente

criar_tabela_cliente()

st.set_page_config(
    page_title="Agendamento",
    page_icon="📅",
    layout="centered"
)

paginas = [
    st.Page("menu.py", title="Início"),
    st.Page("cadastro.py", title="Cadastro")
]

pagina = st.navigation(
    paginas,
    position="hidden"
)

pagina.run()