
import random 

characters="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

digitos=int(input("Introduce el numero de digitos que quieres que tenga tu contraseña:"))

password = ""

for i in range(digitos):
    password += random.choice(characters)

print("Tu contraseña generada es:", password)
