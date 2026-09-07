import streamlit as st
from validar_dados import validar_dados

horarios = {
    0: ["08:00", "09:00", "10:00"],              # segunda
    1: ["08:00", "13:00", "14:00"],              # terça
    2: ["09:00", "10:00", "15:00"],              # quarta
    3: ["08:00", "14:00", "16:00"],              # quinta
    4: ["08:00", "10:00", "15:00"],              # sexta
    5: ["08:00", "09:00", "10:00"]               # sabado
}


st.title("AGENDAMENTO")


nome = st.text_input("Nome completo").capitalize()
whatsapp = st.text_input("Telefone / Whatsapp", placeholder= "(99) 99999-9999")
cpf = st.text_input("CPF",placeholder="123.456.789-10")
data = st.date_input("Escolha data", format= "DD/MM/YYYY")
dia_semana = data.weekday()
horarios_disponiveis = horarios.get(dia_semana, [])
if horarios_disponiveis:
    hora = st.selectbox("Escolha horário", horarios_disponiveis)
    enviar = st.button("Confirmar Agendamento")

    if enviar:
        erro = []
        if not nome:
            erro.append("Erro, Preenche o nome")
        
        if not whatsapp:
            erro.append("Erro, preenche numero de telefone")
    
        if not cpf:
            erro.append("Erro, preenche o cpf")
    
        if erro:
            for erros in erro:
                st.error(erros)

        else:
            validar_dados(nome,whatsapp,cpf,data,hora)

else:
    st.error("Horário indisponivel nesta data")



