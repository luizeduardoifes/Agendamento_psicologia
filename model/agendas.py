from realtime import dataclass
from datetime import date, time

@dataclass
class Agenda:
    usuario_id: int
    nome: str
    data: date
    horario: time
    servico: str