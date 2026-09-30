import bcrypt

def hash_password(senha):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha.encode("utf-8"), salt)
    return hashed.decode("utf-8")

def check_password(senha,cliente):
        return bcrypt.checkpw(senha.encode("utf-8"), cliente.encode("utf-8"))