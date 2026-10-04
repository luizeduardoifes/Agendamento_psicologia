import streamlit as st
from repo.agenda_repo import criar_tabela_agendamento
from repo.cliente_repo import criar_tabela_cliente

criar_tabela_cliente()
criar_tabela_agendamento()

st.set_page_config(
    page_title="Agendamento",
    page_icon="📅",
    layout="centered"
)

paginas = [
    st.Page("menu.py", title="Início"),
    st.Page("cadastro.py", title="Cadastro"),
    st.Page("login.py", title="Login"),
    st.Page("agendamento.py", title="Agendamento")
]

pagina = st.navigation(
    paginas,
    position="hidden"
)

pagina.run()