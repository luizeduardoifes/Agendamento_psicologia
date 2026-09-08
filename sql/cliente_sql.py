CREATE_TABLE_AGENDAMENTO = """
CREATE TABLE IF NOT EXISTS agendamento (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    cpf TEXT NOT NULL,
    data DATE NOT NULL,
    hora TIME NOT NULL
);
"""

INSERT_AGENDAMENTO = """
INSERT INTO agendamento (nome, telefone, cpf, data, hora) VALUES (%s, %s, %s, %s, %s);
"""

VERIFICAR_AGENDAMENTO = """
SELECT * FROM agendamento WHERE data = %s AND hora = %s;

"""