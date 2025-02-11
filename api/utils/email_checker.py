import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def checker(email):
    """ Email geçerli mi diye kontrol eder. """
    valid = re.match(regex, email)
    
    if valid:
        return True

    else:
        return False