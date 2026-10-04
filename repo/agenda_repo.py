from data.database import conectar_banco
from model.agendas import Agenda
from sql.agenda_sql import *
from datetime import date, time

def criar_tabela_agendamento():
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(CREATE_TABLE_AGENDAMENTO)
        conn.commit()
    finally:
        conn.close()

def inserir_agendamento(dados: Agenda) -> Agenda:
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(INSERT_AGENDAMENTO, (dados.usuario_id, dados.data, dados.horario))
        conn.commit()
    finally:
        conn.close()

def verificar_agendamento_existente(usuario_id: int, data: date, horario: time) -> bool:
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(VERIFICAR_AGENDAMENTO_EXISTENTE, (usuario_id, data, horario))
        return cursor.fetchone() is not None
    finally:
        conn.close()