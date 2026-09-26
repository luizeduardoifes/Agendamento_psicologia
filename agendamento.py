import streamlit as st


st.set_page_config(
    page_title="Agendamento",
    page_icon="📅",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background-color: #634020;
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



horarios = { 
    0: ["08:00", "09:00", "10:00"],              # segunda 
    1: ["08:00", "13:00", "14:00"],              # terça 
    2: ["09:00", "10:00", "15:00"],              # quarta 
    3: ["08:00", "14:00", "16:00"],              # quinta 
    4: ["08:00", "10:00", "15:00"],              # sexta 
    5: ["08:00", "09:00", "10:00"]               # sabado 
} 
 
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
    if not verificar_agendamento(data, horario): 
        horarios_disponiveis.append(horario) 
 
if horarios_disponiveis: 

    hora = st.selectbox(
        "Horários disponíveis", 
        horarios_disponiveis, 
        index=None, 
        placeholder="Selecione um horário"
    ) 