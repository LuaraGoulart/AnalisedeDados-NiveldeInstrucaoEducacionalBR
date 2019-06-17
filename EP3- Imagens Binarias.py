############################### ||>>  funcoes  <<|| ###############################################
# 3 sem - ADS turma A
# Luara Cristine Lopes Goulart
# Luiz Henrique Silva

def searchAndAdd(itemUPorLEFTCord, itemCord, matrizRegioes):
    for i in range(len(matrizRegioes)):
        if itemUPorLEFTCord in matrizRegioes[i]:
            matrizRegioes[i].insert(i, itemCord)
    return matrizRegioes

def exibirMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def searchAndAddAndRemove(itemUPCord, itemLEFTCord, itemCord, matrizRegioes):
    for i in range(len(matrizRegioes)):
        # matrizRegioes = []
        if itemUPCord in matrizRegioes[i]:
            matrizRegioes[i].append(itemCord)
            mDel = i
            break
    stohp = True
    j = 0
    while (stohp):
        if itemLEFTCord in matrizRegioes[j]:
            matrizRegioes[mDel].extend(matrizRegioes[j])
            stohp = False
            j -= 1
        j += 1
    if mDel != j:
        matrizRegioes.remove(matrizRegioes[j])
    else:
        pass
    return matrizRegioes

def buscRetReg(item, listaregioes):  # busca item na matrix de regioes e retorna o index/regiao q ele esta
    indx = 0
    sai = True
    i = 0
    while i < len(listaregioes) and sai == True:
        if len(listaregioes[i]) == 2 and len(listaregioes) > 2:
            if item in listaregioes:
                indx = i + 1
                sai = False
        if item in listaregioes[i]:
            indx = i + 1
            sai = False
        else:
            i += 1
    return indx

def hardWork(maEntrada):
    mareg = []
    R = 0
    for L in range(len(maEntrada)):

        for C in range(len(maEntrada[L])):
            conexaoUP = False
            conexaoLEFT = False
            item = maEntrada[L][C]
            itemAcima = maEntrada[L - 1][C]
            itemAnterior = maEntrada[L][C - 1]
            itemCord = [L, C]
            itemAcimaCord = [L - 1, C]
            itemAnteriorCord = [L, C - 1]

            if item == 1:
                # se o comprimento da matriz de regioes for 0 adiciona im item, so pra nao dar "index out of range"
                if len(mareg) == 0:
                    mareg.append([])

                # verifica se nao e a primeira linha da matriz
                if L > 0:
                    if itemAcima == 1:
                        conexaoUP = True
                        # addOnRegion(item, itemAcima)

                # verifica se nao e a primeira coluna da matriz
                if C > 0:
                    if itemAnterior == 1:
                        conexaoLEFT = True

                # se tem conexao acima ele adiciona na lista qual esta conectado
                if (conexaoUP and conexaoLEFT) == True:
                    mareg = searchAndAddAndRemove(itemAcimaCord, itemAnteriorCord, itemCord, mareg)
                    R = len(mareg)
                elif conexaoUP == True:
                    mareg = searchAndAdd(itemAcimaCord, itemCord, mareg)
                    R = len(mareg)
                elif conexaoLEFT == True:
                    mareg = searchAndAdd(itemAnteriorCord, itemCord, mareg)
                    R = len(mareg)
                # se nao tem conexao nenhuma ele adiciona mais uma regiao na matriz, (uma linha da matriz equivale uma regiao)
                if conexaoLEFT == False and conexaoUP == False:

                    if len(mareg) - 1 < R:
                        mareg.append([])
                    mareg[R].append(itemCord)
                    R += 1
            else:
                pass
    return mareg

def subsDeCoords(matrizEntrada, matrizCord):
    R = 0
    a = 0
    b = 0
    maFinal = []


    for L in range(len(matrizEntrada)):
        a = b
        for C in range(len(matrizEntrada[L])):
            item = matrizEntrada[L][C]
            itemCord = [L, C]

            if item == 1:
                itemFinal = buscRetReg(itemCord, matrizCord)
            else:
                itemFinal = 0
            if a == b:
                maFinal.append([])
                a = b + 1
            else:
                pass
            maFinal[L].append(itemFinal)
    return maFinal

maEntrada1 = [[1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]
maEntrada2 = [[0, 1, 0], [1, 1, 1], [0, 0, 0], [1, 0, 1]]
maEntrada3 = [[0, 0, 1, 1, 0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 0]]

############################### ||>> entradas e saidas <<|| ###############################################
print("§§§§§§§§§§§§§§§§    Entrada 1    §§§§§§§§§§§§§§§§")
m1 = hardWork(maEntrada1)
m1s = subsDeCoords(maEntrada1, m1 )
exibirMatriz(m1s)
print("§§§§§§§§§§§§§§§§    Entrada 2    §§§§§§§§§§§§§§§§")
m2 = hardWork(maEntrada2)
m2s = subsDeCoords(maEntrada2, m2)
exibirMatriz(m2s)
print("§§§§§§§§§§§§§§§§    Entrada 3    §§§§§§§§§§§§§§§§")
m3 = hardWork(maEntrada3)
m3s = subsDeCoords(maEntrada3, m3)
exibirMatriz(m3s)
