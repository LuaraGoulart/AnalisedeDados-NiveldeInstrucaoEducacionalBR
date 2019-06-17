import random
import time

#Luara Cristine Lopes Goulart
#Luiz Henrique silva 
vetArr = []  # declara uma lista vazia


# funcao cria uma lista de vetores aleatorios entre 0 e 100
def criarandomvet(x):
    for i in range(x):
        vetArr.append(random.randrange(100))
    return vetArr


def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r


def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)


def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivô = lista[0]
    iguais = [x for x in lista if x == pivô]
    menores = [x for x in lista if x < pivô]
    maiores = [x for x in lista if x > pivô]
    return quicksort(menores) + \
           iguais + quicksort(maiores)


def selection(v):
    resp = []
    while v:
        m = min(v)
        resp.append(m)
        v.remove(m)
    return resp


totaltime = 0

x = 0
listadetempos_mergesort = []
listadetempos_quicksort = []
listadetempos_selection = []
listadetempos_native = []

listadevetores = []

while totaltime < 30:
    vetcriado = criarandomvet(x)

    vetnovo_native = vetcriado
    start = time.time()
    vetnovo_native.sort()
    end = time.time()
    totaltime = (end - start)
    listadetempos_native.append(totaltime)

    start = time.time()
    vetnovo_mgs = mergesort(vetcriado)
    end = time.time()
    totaltime = (end - start)
    listadetempos_mergesort.append(totaltime)

    start = time.time()
    vetnovo_qs = quicksort(vetcriado)
    end = time.time()
    totaltime = (end - start)
    listadetempos_quicksort.append(totaltime)

    start = time.time()
    vetnovo_sel = selection(vetcriado)
    end = time.time()
    totaltime = (end - start)
    listadetempos_selection.append(totaltime)

    x += 2000
    listadevetores.append(x)

i = 0
print("|| =========================== Estrutura de dados =========================== ||")
print("||  tempo   ||== mergesort ==||== quicksort ==||== Selection ==||== Native == ||")
for i in range(len(listadevetores)):
    print("||  " + '{:<8}'.format(str(listadevetores[i])) + "||   "
          + '{:<12}'.format(str(round(listadetempos_mergesort[i], 2))) + "||   "
          + '{:<12}'.format(str(round(listadetempos_quicksort[i], 2))) + "||   "
          + '{:<12}'.format(str(round(listadetempos_selection[i], 2))) + "||   "
          + '{:<10}'.format(str(round(listadetempos_native[i], 2))) + "||"
          )
