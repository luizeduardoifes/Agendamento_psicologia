from hash import check_password
from repo.cliente_repo import verificar_login_cliente
import streamlit as st

st.markdown("""
<style>

.stApp {
    background-color: #7E6444;
}

h1 {
    text-align: center;
}

/* Botão do formulário */
[data-testid="stFormSubmitButton"] button {
    background-color: #634020 !important;
    color: white !important;
    border: none !important;
}

/* Textos e labels do formulário */
[data-testid="stForm"] label {
    color: white !important;
}

/* Campos do formulário */
[data-testid="stForm"] input {
    background-color: #634020;
    color: white !important;
    -webkit-text-fill-color: white !important;
}

/* Cor do formulário */
[data-testid="stForm"] {
    background-color: #1F0F0B;
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #4A281B;
}

</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col2:
    st.image("image.png")
st.title("Login")

with st.form("login_form"):
    nome = st.text_input("Nome")
    senha = st.text_input("Senha", type="password")
    botao = st.form_submit_button("Entrar")

if botao:
    erro = []
    if not nome:
        erro.append("Erro, preenche o nome")
    if not senha:
        erro.append("Erro, preenche a senha")

    if erro:
        for erros in erro:
            st.error(erros)

    else:
        hash_banco = verificar_login_cliente(nome)
        if hash_banco:
            if check_password(senha, hash_banco[0]):
                st.success("Login realizado com sucesso!")
            else:
                st.error("Senha incorreta!")