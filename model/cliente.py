from dataclasses import dataclass

@dataclass
class Cliente:
    id: int
    nome: str
    telefone: str
    email: str
    senha: str