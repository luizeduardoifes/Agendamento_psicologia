import streamlit as st
from repo.cliente_repo import criar_tabela_agendamento, verificar_agendamento
from validar_dados import validar_dados

criar_tabela_agendamento()

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
    "Atendimento online", "atendimento presencial e online",
    "atendimento aos Adolescente",
    "neuropsicologia"
]

st.title("AGENDAMENTO")


nome = st.text_input("Nome completo").capitalize()

whatsapp = st.text_input("Telefone / Whatsapp", placeholder= "(99) 99999-9999")

cpf = st.text_input("CPF",placeholder="123.456.789-10")

servico = st.selectbox("Escolha o tipo de serviço", tipos_de_servico, index = None, placeholder="Selecione um serviço")

data = st.date_input("Escolha data", format= "DD/MM/YYYY")

dia_semana = data.weekday()

horarios_do_dia = horarios.get(dia_semana, [])

horarios_disponiveis = []

for horario in horarios_do_dia:
    if not verificar_agendamento(data, horario):
        horarios_disponiveis.append(horario)

if horarios_disponiveis:
    hora = st.selectbox("Horários disponíveis", horarios_disponiveis, index = None, placeholder="Selecione um horário")
    enviar = st.button("Confirmar Agendamento")

    if enviar:
        erro = []
        if not nome:
            erro.append("Erro, Preenche o nome")

        if not whatsapp:
            erro.append("Erro, preenche numero de telefone")

        if not cpf:
            erro.append("Erro, preenche o cpf")

        if not servico:
            erro.append("Erro, preenche o tipo de serviço")

        if not hora:
            erro.append("Erro, preenche o horário")

        if erro:
            for erros in erro:
                st.error(erros)
        else:
            validar_dados(nome,whatsapp,cpf,servico,data,hora)



