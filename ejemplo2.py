import struct
from cryptography.fernet import Fernet

texto = 'abhBHYHBHYHVt1651m165►5tÄ65Ð4Æ1É46'

#generar clave en secuencia de bytes
key = Fernet.generate_key()
objeto_cifrado = Fernet(key)
texto_encriptado = objeto_cifrado.encrypt(str.encode(texto))
print(texto_encriptado)

# desencriptar
texto_desencriptado = objeto_cifrado.decrypt(texto_encriptado)
print(texto_desencriptado)
texto_desencriptado=texto_desencriptado.decode()
print(texto_desencriptado)
print(type(texto_desencriptado))