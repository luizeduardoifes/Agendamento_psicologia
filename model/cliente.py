from dataclasses import dataclass
from datetime import date, time


@dataclass
class Cliente:
    nome: str
    telefone: str
    cpf: str
    data: date
    hora: time