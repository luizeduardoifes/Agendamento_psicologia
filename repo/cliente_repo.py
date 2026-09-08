from data.database import conectar_banco
from model.cliente import Cliente
from sql.cliente_sql import *

def criar_tabela_agendamento():
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(CREATE_TABLE_AGENDAMENTO)
        conn.commit()
    finally:
        conn.close()

def inserir_agendamento(dados: Cliente) -> Cliente:
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(INSERT_AGENDAMENTO, (dados.nome, dados.telefone, dados.cpf, dados.data, dados.hora))
        conn.commit()
    finally:
        conn.close()

def verificar_agendamento(data, hora):
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(VERIFICAR_AGENDAMENTO, (data, hora))
        resultado = cursor.fetchone()
        return resultado is not None
    finally:
        conn.close()