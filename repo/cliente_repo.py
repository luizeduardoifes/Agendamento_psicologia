from data.database import conectar_banco
from model.cliente import Cliente
from sql.cliente_sql import *

def criar_tabela_cliente():
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(CREATE_TABLE_CLIENTE)
        conn.commit()
    finally:
        conn.close()

def inserir_cliente(dados: Cliente) -> Cliente:
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(INSERT_CLIENTE, (dados.nome, dados.telefone, dados.email, dados.senha))
        conn.commit()
    finally:
        conn.close()

def verificar_cliente_existente(telefone: str, email: str) -> bool:
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(VERIFICAR_CLIENTE_EXISTENTE, (email, telefone))
        resultado = cursor.fetchone()
        return resultado is not None
    finally:
        conn.close()

def verificar_login_cliente(nome):
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(VERIFICAR_LOGIN_CLIENTE, (nome,))
        resultado = cursor.fetchone()
        return resultado
    finally:
        conn.close()

def pegar_id_cliente(nome):
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(PEGAR_ID_CLIENTE, (nome,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
    finally:
        conn.close()

def pegar_nome_cliente_e_email(usuario_id):
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(PEGAR_NOME_CLIENTE_E_EMAIL, (usuario_id,))
        resultado = cursor.fetchone()
        if resultado:
            nome, email = resultado
            return nome, email
        else:
            return None, None
    finally:
        conn.close()