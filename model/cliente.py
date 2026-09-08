from dataclasses import dataclass
from datetime import date, time


@dataclass
class Cliente:
    id: int
    nome: str
    telefone: str
    cpf: str
    tipo_servico: str
    data: date
    hora: time