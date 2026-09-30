CREATE_TABLE_AGENDAMENTO = """
CREATE TABLE IF NOT EXISTS agendamento (
    usuario_id INTEGER NOT NULL,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    PRIMARY KEY (usuario_id, data, horario),
    FOREIGN KEY (usuario_id) REFERENCES cliente(id)
);
"""

INSERT_AGENDAMENTO = """
INSERT INTO agendamento (usuario_id, data, horario)
VALUES (%s, %s, %s);
"""

VERIFICAR_AGENDAMENTO_EXISTENTE = """
SELECT * FROM agendamento
WHERE usuario_id = %s AND data = %s AND horario = %s;
"""