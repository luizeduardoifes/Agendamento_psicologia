from validate_docbr import CPF
import streamlit as st
from phonenumbers import NumberParseException,parse, is_valid_number
from model.cliente import Cliente
from repo.cliente_repo import inserir_agendamento, verificar_agendamento


def validar_dados(nome,whatsapp,cpf,servico,data,hora):
    erro = []
    cpf_valido = CPF()
    
    if not cpf_valido.validate(cpf):
        erro.append("CPF inválido")

    try:
        validacao = parse(whatsapp, "BR")
        telefone_valido = is_valid_number(validacao)

        if telefone_valido:
            pass

        else:
            erro.append("Número de telefone inválido")

    except NumberParseException:
        erro.append("Insira apenas números no telefone e adiciona (DDD) no início")

    verificar = verificar_agendamento(data, hora)
    if verificar == True:
        erro.append("Este horário já está agendado, escolha outro horário")

    if erro:
        for erros in erro:
            st.error(erros)
        return

    dados = Cliente(id= 0,nome = nome, telefone= telefone_valido,cpf= cpf ,tipo_servico= servico, data= data, hora= hora)
    inserir_agendamento(dados)
    st.success("Agendamento, com sucesso")