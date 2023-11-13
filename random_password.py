import secrets
import string

def password_random():
    chars=string.ascii_letters+string.digits+string.punctuation
    password=''
    longitud=secrets.choice(range(8,18))
    
    for x in range(longitud):
        password+=secrets.choice(chars)
            
    print(f'Su contraseña es {password}')
        
password_random()
