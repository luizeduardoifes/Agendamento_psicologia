import psycopg2
import streamlit as st
from email_automatico import enviar_email
from id_usuario_logado import usuario_logado
from repo.agenda_repo import verificar_agendamento_existente
from repo.cliente_repo import pegar_nome_cliente_e_email

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

booleano, id_usuario = usuario_logado()

try:
    if not booleano:
        st.error("Sua sessão foi encerrada,faça login novamente")
        
        if st.button("Voltar para o login"):
            st.switch_page("login.py")
        st.stop()

except Exception:
    st.error("Ocorreu um erro ao verificar sua sessão.")
    st.stop()

except psycopg2.OperationalError:
    st.error("Não foi possível conectar ao banco de dados.")
    st.stop()

horarios = { 
    0: ["08:00", "09:00", "10:00"],              # segunda 
    1: ["08:00", "13:00", "14:00"],              # terça 
    2: ["09:00", "10:00", "15:00"],              # quarta 
    3: ["08:00", "14:00", "16:00"],              # quinta 
    4: ["08:00", "10:00", "15:00"],              # sexta 
    5: ["08:00", "09:00", "10:00"]               # sabado 
} 

col1, col2, col3 = st.columns(3)

with col2:

    st.image("image.png")

    st.markdown(
    "<h3 style='text-align: center;'>Agendamento</h3>",
    unsafe_allow_html=True
    )

tipos_de_servico = [ 
    "Consulta psicológica", 
    "Terapia de casal", 
    "Atendimento infantil", 
    "Atendimento aos Adulto", 
    "Atendimento aos idosos", 
    "Atendimento online", 
    "atendimento presencial e online", 
    "atendimento aos Adolescente", 
    "neuropsicologia" 
] 
 
servico = st.selectbox(
    "Escolha o tipo de serviço", 
    tipos_de_servico, 
    index=None, 
    placeholder="Selecione um serviço"
) 

data = st.date_input(
    "Escolha data", 
    format="DD/MM/YYYY"
) 

dia_semana = data.weekday()

horarios_do_dia = horarios.get(dia_semana, []) 
 
horarios_disponiveis = [] 
 
for horario in horarios_do_dia: 
    if not verificar_agendamento_existente(usuario_id=usuario_logado(), data=data, horario=horario): 
        horarios_disponiveis.append(horario) 

if horarios_disponiveis: 

    hora = st.selectbox(
        "Horários disponíveis", 
        horarios_disponiveis, 
        index=None, 
        placeholder="Selecione um horário"
    )

    botao_agendar = st.button("Agendar")

    if botao_agendar:
        erro = []
        if not servico:
            erro.append("Escolha um serviço")
        
        if not data:
            erro.append("Escolha uma data")

        if not hora:
            erro.append("Escolha a hora")

        if erro:
            for erros in erro:
                st.error(erros)

        else:
            st.success(f"Agendamento feito,irá receber um e-mail de confirmação com os detalhes do agendamento.")
            nome_cliente, email_cliente = pegar_nome_cliente_e_email(id_usuario)
            enviar_email(nome_cliente, email_cliente, data, hora, servico)
    
else:
    st.warning("Horário indisponível. Por favor, escolha outro horário.")