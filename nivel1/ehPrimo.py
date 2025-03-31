# __________________ COMENTARIO PESSOAL ___________________

# Pode parecer esquisito o if case da linha 43, POREM
# ele está apra auxiliar os prints a fiarem alinhados

# ______________________ CONSTANTES _______________________
TAM = 10

# ______________________ IMPORTAÇÕES ______________________
from random import randint

# ____________________ FUNCOES CRIADAS ____________________
def eh_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def criarLista():
    listaNumeros = [] 
    for i in range(TAM):
        listaNumeros.append(randint(0, 99))
    return listaNumeros

# ____________________ DESENVOLVIMENTO ____________________

listaCriada     = criarLista()
listaTrueFalse  = listaCriada.copy() 
listaProduto    = listaCriada.copy()   

print("\n-> A lista original é: ", listaCriada)

print("\n-> Verificação de primos (True/False):")

for i in range(TAM):
    listaTrueFalse[i] = eh_primo(listaTrueFalse[i])
    if   listaCriada[i] <= 9:
        print("|  ", listaCriada[i]," : ",listaTrueFalse[i])
    else:
        print("| ", listaCriada[i]," : ",listaTrueFalse[i])

produto = 1
for i in range(TAM):
    if eh_primo(listaProduto[i]): 
        produto *= listaProduto[i]

print("\n-> E multiplicando os primos entre si retorna: ", produto)