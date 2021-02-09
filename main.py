import numpy as np

neuronas=[]
no_capas=0
max_neuronas=0
pesos=[]
umbrales =[]
activacion=[]







def sigmoide(acumulador):
    return 1 / (1 + np.exp(-acumulador))


def feedforwar(enter):
    global activacion, pesos, umbrales, neuronas, max_neuronas, no_capas, salidas

    activacion[0, 0] = enter[0]
    activacion[0, 1] = enter[1]


    for i in range(no_capas - 1):

        for j in range(neuronas[i + 1]):
            acumulador = 0
            for k in range(neuronas[i]):
                acumulador += activacion[i, k] * pesos[i, k, j]
                print(" {}   {}  ".format(activacion[i, k],pesos[i, k, j]))

            acumulador += umbrales[i, j]
            print("{}  \n".format(umbrales[i,j]))

            activacion[i+1, j] = sigmoide(acumulador)


entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
flag=int(input("1 o 0"))0

if(flag):
    neuronas = [2, 2, 1]
    no_capas = 3

    max_neuronas = max((neuronas))
    pesos = np.zeros((no_capas - 1, max_neuronas, max_neuronas))
    umbrales = np.zeros((no_capas - 1, max_neuronas))
    activacion = np.zeros((no_capas, max_neuronas))

    pesos[0, 0, 0] = 5.191129
    pesos[0, 0, 1] = 2.758669
    pesos[0, 1, 0] = 5.473012
    pesos[0, 1, 1] = 2.769596
    pesos[1, 0, 0] = 5.839709
    pesos[1, 1, 0] = -6.186834

    umbrales[0, 0] = -1.90289
    umbrales[0, 1] = -4.127002
    umbrales[1, 0] = -2.570539
else:
    neuronas=[2,2,2,2]
    no_capas=4
    max_neuronas = max((neuronas))
    pesos = np.ones((no_capas - 1, max_neuronas, max_neuronas))
    umbrales = np.zeros((no_capas - 1, max_neuronas))
    activacion = np.zeros((no_capas, max_neuronas))

    for i in range(no_capas-1):
        for j in range(max_neuronas):
            umbrales[i,j]=0.5



for i in range(len(entrada)):
    feedforwar(entrada[i])

    print(activacion)

