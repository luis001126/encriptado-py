from werkzeug.security import generate_password_hash, check_password_hash

texto = 'ncjjakaa5c116891616♦@@sdj*JDHN'

texto_encriptado = generate_password_hash(texto)
texto_encriptado1 = generate_password_hash(texto, 'sha256', 30)

print(texto_encriptado)
print(texto_encriptado1)

print(check_password_hash(texto_encriptado1,texto))