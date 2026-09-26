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

