import streamlit as st
from phonenumbers import NumberParseException,parse, is_valid_number
from hash import hash_password
from model.cliente import Cliente
from email_validator import validate_email, EmailNotValidError
from repo.cliente_repo import inserir_cliente, verificar_cliente_existente

def validar_dados(nome,whatsapp,email, senha, confirmar_senha):
    cliente_existente = verificar_cliente_existente(whatsapp, email)
    if cliente_existente:
        st.error("Email ou telefone já cadastrado")

    else:
        erro = []

        try:
            email_valido = validate_email(email, check_deliverability=False)
            email_verificado = email_valido.normalized

        except EmailNotValidError:
            erro.append("Email inválido")

        try:
            telefone = parse(whatsapp, "BR")
            telefone_valido = is_valid_number(telefone)

            if telefone_valido:
                pass

            else:
                erro.append("Número de telefone inválido")

        except NumberParseException:
            erro.append("Número de telefone inválido")

        if senha != confirmar_senha:
            erro.append("As senhas não coincidem")

        if erro:
            for erros in erro:
                st.error(erros)
            return

        senha_hash = hash_password(senha)
        dados = Cliente(id= 0,nome = nome, telefone= telefone_valido,email= email_verificado, senha= senha_hash)
        inserir_cliente(dados)
        st.success("Cadastro realizado com sucesso")