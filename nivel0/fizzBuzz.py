# __________________ COMENTARIO PESSOAL ___________________

# Aqui decidi desenvolver mais a função FIZZBUZZ,
# com input de quantidade dada pelo usuario, podendo
# testar o comportamento da função, mas em reusmo a
# reposta é só a funcao fizzBuzz


# ______________________ IMPORTAÇÕES ______________________

from random import randint

# ____________________ FUNCOES CRIADAS ____________________

def fizzBuzz(num):
    if num%3 == 0 and num%5 ==0:
        return "FizzBuzz"
    elif num%3 == 0:
        return "Fizz"
    elif num%5 == 0:
        return "Buzz"
    else:
        return "#"
    

# ____________________ DESENVOLVIMENTO ____________________

numerosFB = [] 

quant = int(input("\n- Quantidade de numeros pra checar se\n>>> FIZZ (div por 3);\n>>> BUZZ (div por 5);\n>>> FIZZBUZZ (div por 3 e 5)\n-> "))

for i in range(quant):
    numerosFB.append(randint(0,100))

print("________________________________________________\n")
for i in range(quant):
    print("- ",numerosFB[i],"é: ",fizzBuzz(numerosFB[i]),"\n")
print("________________________________________________\n")