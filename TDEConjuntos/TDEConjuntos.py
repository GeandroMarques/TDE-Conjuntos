#Função que realiza a União
def uniao(conjunto1, conjunto2):
    resultadoU = conjunto1.copy()
    for i in range(len(conjunto2)):
        if conjunto2[i] not in resultadoU:
            resultadoU.append(conjunto2[i])
    return resultadoU


#Função que realiza a interseção
def intersecao(conjunto1, conjunto2):
    resultadoI = []
    for i in range(len(conjunto2)):
        if conjunto2[i] in conjunto1:
            resultadoI.append(conjunto2[i])
        else:
            pass
    return resultadoI


#Função que realiza a diferença
def diferenca(conjunto1, conjunto2):
    resultadoD = []
    for i in range(len(conjunto1)):
        if conjunto1[i] not in conjunto2:
            resultadoD.append(conjunto1[i])
    return resultadoD


#Função que realiza o produto cartesiano
def produto_cartesiano(conj1, conj2):
    resultadoPC = ""
    for i in range(len(conj1)):
        for j in range(len(conj2)):
            resultadoPC = resultadoPC + (f"({conj1[i]},{conj2[j]})")
    return resultadoPC

#Função que verifica as operações
def operacao(operacaon, conj1, conj2):
    if operacaon == "U":
        resultadoU = uniao(conj1, conj2)
        printconj1 = '{' + ', '.join(map(str, conj1)) + '}'
        printconj2 = '{' + ', '.join(map(str, conj2)) + '}'
        printresU = '{' + ', '.join(map(str, resultadoU)) + '}'
        print(f'União: conjunto 1 {printconj1}, conjunto 2 {printconj2}. Resultado: {printresU}')
    elif operacaon == "I":
        resultadoI = intersecao(conj1,conj2)
        printconj1 = '{' + ', '.join(map(str, conj1)) + '}'
        printconj2 = '{' + ', '.join(map(str, conj2)) + '}'
        printresI = '{' + ', '.join(map(str, resultadoI)) + '}'
        print(f'Interseção: conjunto 1 {printconj1}, conjunto 2 {printconj2}. Resultado: {printresI}')
    elif operacaon == "D":
        resultadoD = diferenca(conj1, conj2)
        printconj1 = '{' + ', '.join(map(str, conj1)) + '}'
        printconj2 = '{' + ', '.join(map(str, conj2)) + '}'
        printresD = '{' + ', '.join(map(str, resultadoD)) + '}'
        print(f'Diferença: conjunto 1 {printconj1}, conjunto 2 {printconj2}. Resultado: {printresD}')
    elif operacaon == "C":
        resultadoPC = produto_cartesiano(conj1, conj2)
        printconj1 = '{' + ', '.join(map(str, conj1)) + '}'
        printconj2 = '{' + ', '.join(map(str, conj2)) + '}'
        printresPC = '{' + str(resultadoPC).replace('[', '{').replace(']', '}').replace('), {', '), (') + '}'
        print(f'Produto Cartesiano: conjunto 1 {printconj1}, conjunto 2 {printconj2}. Resultado: {printresPC} ')
    else:
        print("Operação inválida")

def ler_conjuntos(linha):
    return linha.strip().split(', ')

print("Faça a escolha do arquivo que vai ser lido")
print("Digite 1 para escolher o Exemplo 1")
print("Digite 2 para escolher o Exemplo 2")
print("Digite 3 para escolher o Exemplo 3")
escolhaARQUIVO = input("Digite 4 para escolher o Exemplo 4 (Arquivo editado pelo professor): ")

if escolhaARQUIVO == '1':
    with open("Exemplo1.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    ndeoperacoes = linhas[0].strip()

elif escolhaARQUIVO == '2':
    with open("Exemplo2.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    ndeoperacoes = linhas[0].strip()

elif escolhaARQUIVO == '3':
    with open("Exemplo3.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    ndeoperacoes = linhas[0].strip()

elif escolhaARQUIVO == '4':
    with open("Exemplo4.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    ndeoperacoes = linhas[0].strip()

else:
    print("Escolha inválida")

if ndeoperacoes == "4":
    primeiraOPERACAO = linhas[1].strip()
    conjunto1 = ler_conjuntos(linhas[2])
    conjunto2 = ler_conjuntos(linhas[3])
    segundaOPERACAO = linhas[4].strip()
    conjunto3 = ler_conjuntos(linhas[5])
    conjunto4 = ler_conjuntos(linhas[6])
    terceiraOPERACAO = linhas[7].strip()
    conjunto5 = ler_conjuntos(linhas[8])
    conjunto6 = ler_conjuntos(linhas[9])
    quartaOPERACAO = linhas[10].strip()
    conjunto7 = ler_conjuntos(linhas[11])
    conjunto8 = ler_conjuntos(linhas[12])

    operacao(primeiraOPERACAO, conjunto1, conjunto2)
    operacao(segundaOPERACAO, conjunto3, conjunto4)
    operacao(terceiraOPERACAO, conjunto5, conjunto6)
    operacao(quartaOPERACAO, conjunto7, conjunto8)

elif ndeoperacoes == "3":
    primeiraOPERACAO = linhas[1].strip()
    conjunto1 = ler_conjuntos(linhas[2])
    conjunto2 = ler_conjuntos(linhas[3])
    segundaOPERACAO = linhas[4].strip()
    conjunto3 = ler_conjuntos(linhas[5])
    conjunto4 = ler_conjuntos(linhas[6])
    terceiraOPERACAO = linhas[7].strip()
    conjunto5 = ler_conjuntos(linhas[8])
    conjunto6 = ler_conjuntos(linhas[9])

    operacao(primeiraOPERACAO, conjunto1, conjunto2)
    operacao(segundaOPERACAO, conjunto3, conjunto4)
    operacao(terceiraOPERACAO, conjunto5, conjunto6)

elif ndeoperacoes == "2":
    primeiraOPERACAO = linhas[1].strip()
    conjunto1 = ler_conjuntos(linhas[2])
    conjunto2 = ler_conjuntos(linhas[3])
    segundaOPERACAO = linhas[4].strip()
    conjunto3 = ler_conjuntos(linhas[5])
    conjunto4 = ler_conjuntos(linhas[6])

    operacao(primeiraOPERACAO, conjunto1, conjunto2)
    operacao(segundaOPERACAO, conjunto3, conjunto4)

elif ndeoperacoes == "1":
    primeiraOPERACAO = linhas[1].strip()
    conjunto1 = ler_conjuntos(linhas[2])
    conjunto2 = ler_conjuntos(linhas[3])

    operacao(primeiraOPERACAO, conjunto1, conjunto2)

else:
    print("Numero de operações inválido, você deve escolher entre 1 e 4 operações")








