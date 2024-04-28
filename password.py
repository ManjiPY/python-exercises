import random # Biblioteca random, implementação de gerador de números pseudoaleatórios
import string # Biblioteca string, suporte de ascii, caracteres especiais etc.

# Variável amount, recebe um valor da extensão da senha
amount = 35

# Variável characteres, recebe um conjunto de ascii, dígitos e pontuações através da string lib
characteres = string.ascii_letters + string.digits + string.punctuation

# Variável password, inicialmente definida como vazia
password = ""

# Laço de repetição for que irá repetir de acordo com a variável amount, e incrementar
# a variável password uma escolha aleatória dentre os valores de characteres
for _ in range(amount):
    password += random.choice(characteres)

# Mostrar a nova senha gerada no console
print(f"Password generated: {password}")