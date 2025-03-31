# __________________ COMENTARIO PESSOAL ___________________

# delirei? sim
# talvez tenha tido muito o pensamento obsessivo de
# reaproveitamento herdado do C? sim
# mas tudo operante e belo :)

# ______________________ IMPORTAÇÕES ______________________
from math import *                              # Requisito 1

# ____________________ FUNÇÕES CRIADAS ____________________

def lerPontos():                                # Requisito 2
    pontos = []
    for i in range(3):
        entrada = input(f"Digite o ponto {i+1} (x,y): ").strip()
        x, y = map(float, entrada.split(','))
        pontos.append((x, y))
    return pontos

def verificarTrianguloValido(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("Não é um triângulo válido!")
        exit()

# ____________________ Exibições 

def exibirLados(a, b, c):                       # Requisito 3
    print("\n----------------- LADOS DO TRIÂNGULO -----------------")
    print(f"| a = {a:.2f}")
    print(f"| b = {b:.2f}")
    print(f"| c = {c:.2f}")

def exibirAngulos(anguloA, anguloB, anguloC):   # Requisito 4
    print("\n---------------- ÂNGULOS DO TRIÂNGULO ----------------")
    print(f"| Ângulo A = {anguloA:.2f}°")
    print(f"| Ângulo B = {anguloB:.2f}°")
    print(f"| Ângulo C = {anguloC:.2f}°")

def exibirPerimetroArea(perimetro, area):       # Requisito 5
    print("\n----------------- PERÍMETRO E ÁREA ------------------")
    print(f"| Perímetro = {perimetro:.2f}")
    print(f"| Área = {area:.2f}")

def exibirClassificacaoLados(tipoLados):        # Requisito 6
    print("\n------------- CLASSIFICAÇÃO POR LADOS ---------------")
    print(f"| Tipo: {tipoLados}")

def exibirClassificacaoAngulos(tipoAngulos):    # Requisito 7
    print("\n------------ CLASSIFICAÇÃO POR ÂNGULOS --------------")
    print(f"| Tipo: {tipoAngulos}")
    print("_____________________________________________________")

# ____________________ CÁLCULOS 

def calcularDistancia(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def calcularAngulos(a, b, c):
    anguloA = degrees(acos((b**2 + c**2 - a**2) / (2 * b * c)))
    anguloB = degrees(acos((a**2 + c**2 - b**2) / (2 * a * c)))
    anguloC = 180 - anguloA - anguloB
    return anguloA, anguloB, anguloC

def calcularPerimetroArea(a, b, c):
    perimetro = a + b + c
    s = perimetro / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return perimetro, area

def classificarPorLados(a, b, c):
    epsilon = 1e-3
    if abs(a - b) < epsilon and abs(b - c) < epsilon:
        return "EQUILÁTERO"
    elif abs(a - b) < epsilon or abs(a - c) < epsilon or abs(b - c) < epsilon:
        return "ISÓSCELES"
    return "ESCALENO"

def classificarPorAngulos(anguloA, anguloB, anguloC):
    epsilon = 1e-3
    if any(abs(ang - 90) < epsilon for ang in (anguloA, anguloB, anguloC)):
        return "RETÂNGULO"
    elif max(anguloA, anguloB, anguloC) > 90:
        return "OBTUSÂNGULO"
    return "ACUTÂNGULO"

# ____________________ PROGRAMA PRINCIPAL ____________________

pontos = lerPontos()

a = calcularDistancia(pontos[1], pontos[2])
b = calcularDistancia(pontos[0], pontos[2])
c = calcularDistancia(pontos[0], pontos[1])

verificarTrianguloValido(a, b, c)

exibirLados(a, b, c)

anguloA, anguloB, anguloC = calcularAngulos(a, b, c)
exibirAngulos(anguloA, anguloB, anguloC)

perimetro, area = calcularPerimetroArea(a, b, c)
exibirPerimetroArea(perimetro, area)

tipoLados = classificarPorLados(a, b, c)
exibirClassificacaoLados(tipoLados)

tipoAngulos = classificarPorAngulos(anguloA, anguloB, anguloC)
exibirClassificacaoAngulos(tipoAngulos)