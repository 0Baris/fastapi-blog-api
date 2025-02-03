import bcrypt

# Şifreyi hashleyip kaydetme ve istenildiği zaman decrypt etme işlemi.
def hash_password(password: str) -> str:
    """ Parola şifreleme fonksiyonu """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """ Parola şifresini açma fonksiyonu """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))