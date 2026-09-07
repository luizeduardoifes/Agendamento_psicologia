from validate_docbr import CPF
import streamlit as st
from phonenumbers import NumberParseException,parse, is_valid_number
from model.cliente import Cliente


def validar_dados(nome,whatsapp,cpf,data,hora):
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

    if erro:
        for erros in erro:
            st.error(erros)
        return

    else:
        Cliente(nome = nome, telefone= telefone_valido,cpf= cpf ,data= data, hora= hora)
        st.success("Agendamento, com sucesso")
        

    

    

            

    