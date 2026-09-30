import streamlit as st

st.set_page_config(
    page_title="Agendamento",
    page_icon="📅",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background-color: #7E6444;
}

.stButton > button {
    background-color: #1F0F0B;
    color: white;
    border: none;
}

.stButton > button:hover {
    background-color: #1F0F0B;
    color: white;
}

/* Esconder sidebar */
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="stSidebarCollapsedControl"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col2:

    st.image("image.png")

    st.markdown(
    "<h3 style='text-align: center;'>Aqui, cuidar de si é prioridade.</h3>",
    unsafe_allow_html=True
    )

    st.markdown(
    "<p style='text-align: center;'>Venha nos conhecer</p>",
    unsafe_allow_html=True
)

    agendamento = st.button("📅 Fazer Agendamento", use_container_width=True)
    cadastro = st.button("👤 Cadastrar", use_container_width=True)

if cadastro:
    st.switch_page("cadastro.py")

if agendamento:
    st.switch_page("login.py")