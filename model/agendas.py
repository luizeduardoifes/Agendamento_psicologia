from realtime import dataclass
from datetime import date, time

@dataclass
class Agenda:
    usuario_id: int
    data: date
    horario: time