import re

print(re.match("[Cc]arro", "Carro azul."))
frase = "Carro azul"
busca = re.match("[Cc]arro", frase)
print(busca[0])
