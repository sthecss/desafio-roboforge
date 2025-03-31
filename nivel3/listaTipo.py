# __________________ COMENTARIO PESSOAL ___________________
# Essa foi um desafiozim maior, mas foi legal. Foi interes-
# sante buscar funções como: [isdigit, count, replace, split],
# readequando e redescobrindo o pensamento computacional de
# outras situações nesse desafio

# ____________________ FUNCOES CRIADAS ____________________
def verificarTipo():                            # Requisito 1 2
    entrada = input("Digite algo: ")
    
    # Determina o tipo
    if entrada.isdigit():
        valor = int(entrada)
        tipo = "int"
    elif entrada.replace('.', '', 1).isdigit() and entrada.count('.') < 2:
        valor = float(entrada)
        tipo = "float"
    elif entrada.lower() in ('true', 'false'):
        valor = entrada.lower() == 'true'
        tipo = "bool"
    else:
        valor = entrada
        tipo = "str"
    
    print("\n-> Informações sobre o input ")
    print(f"\n| Tipo  : {tipo}")
    print(f"| Valor : {valor}")
    return valor, tipo

def criarLista():                               # Requisito 3
    lista = []

    print("\n-> Agora vamos criar uma lista!")
    print("\n-> Digite os elementos da lista (digite 'sair' para terminar):")
    while True:
        entrada = input("> ")
        if entrada.lower() == 'sair':
            break
        
        if entrada.isdigit():
            valor = int(entrada)
        elif entrada.replace('.', '', 1).isdigit() and entrada.count('.') < 2:
            valor = float(entrada)
        elif entrada.lower() in ('true', 'false'):
            valor = entrada.lower() == 'true'
        else:
            valor = entrada
        
        lista.append(valor)
    
    print("\n| Lista criada:")            
    print(lista)
    return lista

def codificarLista(lista):                      # Requisito 4
    partes = []
    for elemento in lista:
        tipo = type(elemento).__name__
        if tipo == 'str':
            partes.append(f"(str: '{elemento}')")
        elif tipo == 'bool':
            partes.append(f"(bool: {elemento})")
        else:
            partes.append(f"({tipo}: {elemento})")
    
    stringCodificada = ", ".join(partes)

    stringCodificada = stringCodificada[::-1].replace(")", "]", 1)[::-1]
    print("\n| Lista codificada:")
    print(stringCodificada)
    return stringCodificada

def decodificarString(stringCodificada):        # Requisito 5
    elementos = stringCodificada.replace('[', '').replace(']', '').split('), ')
    
    lista_decodificada = []
    for elemento in elementos:
        if '(' in elemento:
            elemento = elemento.replace('(', '')
        if ')' in elemento:
            elemento = elemento.replace(')', '')
        
        tipo, valor = elemento.split(': ')
        
        if 'str' in tipo:
            valor = valor.strip("'")
        elif 'int' in tipo:
            valor = int(valor)
        elif 'float' in tipo:
            valor = float(valor)
        elif 'bool' in tipo:
            valor = valor == 'True'
        
        lista_decodificada.append(valor)
    
    print("\n| Lista decodificada:")
    print(lista_decodificada)
    return lista_decodificada


# ____________________ DESENVOLVIMENTO ____________________

print("\n[ Vamos testar o funcionamento do código... ]\n")
valor, tipo = verificarTipo()

minha_lista = criarLista()

codificada = codificarLista(minha_lista)

decodificarString(codificada)