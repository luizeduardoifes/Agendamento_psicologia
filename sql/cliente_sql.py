CREATE_TABLE_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome TEXT NOT NULL,
    telefone TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
);
"""

INSERT_CLIENTE = """
INSERT INTO cliente (nome, telefone, email, senha) VALUES (%s, %s, %s, %s);
"""

VERIFICAR_CLIENTE_EXISTENTE = """
SELECT * FROM cliente WHERE email = %s OR telefone = %s;
"""
