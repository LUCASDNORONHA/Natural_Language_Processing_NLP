import re

frase = "O rato roeu a roupa do rei de Roma."
busca = re.search("[Rr][a-z]*", frase)
print(busca)
print(busca[0])

frase2 = "Hoje é um lindo dia."
busca2 = re.search("l.*o", frase2)
print(busca2)
print(busca2[0])

frase3 = "O sucesso é a soma de pequenos esforços repetidos dia após dia."
busca3 = re.search("^O.*", frase3)
print(busca3)
print(busca3[0])

frase4 = "Penso, logo existo."
busca4 = re.search("e[a-z]{1,5}\.$", frase4)
print(busca4)
print(busca4[0])

frase5 = "Conhece-te a ti mesmo e conhecerás o universo e os deuses."
busca5 = re.findall("[Cc]onhec[a-z]{1,6}", frase5)
print(busca5)
print(busca5[0][1])
