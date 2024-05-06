# Importação da biblioteca nativa do Python => math
import math

# Declaração da variável number, que é do tipo int
number = int(input("Digite um número: "))

# Variável double, explicação: usa o valor que foi digitado
# no input da variável number e multiplica por 2
double = number * 2

# Variável double, explicação: usa o valor que foi digitado
# no input da variável number e multiplica por 3
triple = number * 3

# Variável para raíz quadrada, explicação: usa o valor que foi digitado
# no input da variável number, utilizando o método sqrt() para realizar o cálculo
# da raíz quadrada
square_root = math.sqrt(number)


print(f"O dobro de {number} é {double}")
print(f"O triplo de {number} é {triple}")
print(f"A raíz quadrada de {number} é {square_root}")
