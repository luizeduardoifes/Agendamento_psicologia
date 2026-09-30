import streamlit as st 
from validar_dados import validar_dados 
 
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

/* Cor do formulário */
[data-testid="stForm"] {
    background-color: #1F0F0B;
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #4A281B;
}

/* Campos do formulário */
[data-testid="stForm"] input {
    background-color: #634020;
    color: white !important;
    -webkit-text-fill-color: white !important;
}

/* Placeholder dos campos */
[data-testid="stForm"] input::placeholder {
    color: white !important;
    opacity: 0.8;
}

/* Selectbox */
[data-testid="stForm"] [data-baseweb="select"] > div {
    background-color: #634020;
    color: white !important;
}

/* Texto dentro do Selectbox */
[data-testid="stForm"] [data-baseweb="select"] * {
    color: white !important;
}

/* Date input */
[data-testid="stForm"] [data-baseweb="input"] {
    background-color: #634020;
    color: white !important;
}

[data-testid="stForm"] [data-baseweb="input"] * {
    color: white !important;
}

/* Textos e labels do formulário */
[data-testid="stForm"] label {
    color: white !important;
}

/* Botão do formulário */
[data-testid="stFormSubmitButton"] button {
    background-color: #634020 !important;
    color: white !important;
    border: none !important;
}

[data-testid="stFormSubmitButton"] button:hover {
    background-color: #634020 !important;
    color: white !important;
}


.voltar button {
    background-color: #1F0F0B;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px 18px;
}

.voltar button:hover {
    background-color: #321914;
}

</style>
""", unsafe_allow_html=True)


st.markdown('<div class="voltar">', unsafe_allow_html=True)

if st.button("← Voltar"):
    st.switch_page("menu.py")

st.markdown('</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col2:
    st.image("image.png")
    st.title("Cadastro")

with st.form("formulario_cadastro"):
    nome = st.text_input("Nome completo").capitalize() 
    
    whatsapp = st.text_input(
        "Telefone / Whatsapp", 
        placeholder="(99) 99999-9999"
    ) 
    
    email = st.text_input(
        "Email",
        placeholder="example@email.com"
    )

    senha = st.text_input(
        "Senha",
        type="password"
    ) 
    
    confirmar_senha = st.text_input(
        "Confirmar Senha",
        type="password"
    ) 

    enviar = st.form_submit_button("Cadastrar") 
 
if enviar: 
    erro = [] 
    if not nome: 
        erro.append("Erro, Preenche o nome") 

    if not whatsapp: 
        erro.append("Erro, preenche numero de telefone") 

    if not email: 
        erro.append("Erro, preenche o email") 

    if not senha: 
        erro.append("Erro, preenche a senha")

    if not confirmar_senha: 
        erro.append("Erro, preenche a confirmação da senha")

    if erro: 
        for erros in erro: 
            st.error(erros) 
    else: 
        validar_dados(nome, whatsapp, email, senha, confirmar_senha)