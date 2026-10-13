CREATE_TABLE_AGENDAMENTO = """
CREATE TABLE IF NOT EXISTS agendamento (
    usuario_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    servico TEXT NOT NULL,
    PRIMARY KEY (usuario_id),
    FOREIGN KEY (usuario_id) REFERENCES cliente(id)
);
"""

INSERT_AGENDAMENTO = """
INSERT INTO agendamento (usuario_id, nome, data, horario, servico)
VALUES (%s, %s, %s, %s, %s);
"""

VERIFICAR_AGENDAMENTO_EXISTENTE = """
SELECT * FROM agendamento
WHERE usuario_id = %s AND nome = %s AND data = %s AND horario = %s AND servico = %s;
"""