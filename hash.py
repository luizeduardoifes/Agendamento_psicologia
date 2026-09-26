import bcrypt

def hash_password(senha):
    password = senha.encode("utf-8")

    hash_senha = bcrypt.hashpw(
        password,
        bcrypt.gensalt()
    )

    return hash_senha