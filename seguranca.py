from cryptography.fernet import Fernet

# Em um projeto real, essa chave não ficaria aqui, mas para o T2, 
# você pode gerar uma e colar aqui como string.
CHAVE = Fernet.generate_key() 
cipher = Fernet(CHAVE)

def criptografar(texto):
    return cipher.encrypt(texto.encode()).decode()

def descriptografar(texto_cifrado):
    return cipher.decrypt(texto_cifrado.encode()).decode()