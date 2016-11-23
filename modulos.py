def eliminainalcansaveis(automato):
    estadosalcansados = []
    for elemento in automato:
        for i in range(1, len(elemento)):
            # print(elemento[i])
            if elemento[i] != elemento[0] and elemento[i] not in estadosalcansados:
                if elemento[i] != "-":
                    estadosalcansados.append(elemento[i])
    for i in range(len(estadosalcansados)):
        estadosalcansados.append("*" + estadosalcansados[i])
    for i in range(1,len(automato)):
        # print(automato[i][0])
        if automato[i][0] not in estadosalcansados:
            automato[i][0] = "-"
            for k in range(len(automato[i])):
                automato[i][k] = '-'

    return automato



def eliminaMortos(automato):
    flag = 0
    rmEstados = []
    for elemento in automato:
        t = len(elemento)
        estado = elemento[0]
        for i in range(len(elemento)):
            if elemento[i] == estado:
                flag += 1
        if flag == t:
            rmEstados.append(estado)
        flag = 0
    for x in rmEstados:
        for i in range(len(automato)):
            for j in range(len(automato[i])):
                if automato[i][j] == x:
                    automato[i][j] = "-"
    return automato



def eliminavazio(automato):
    contador = 0
    estadoeliminado = []
    for elemento in automato:


        for i in elemento:
            if i == "-":
                contador += 1
                # print(contador)
            if contador == 2:
                # print(elemento[0] + " sera eliminado")
                estadoeliminado.append(elemento[0])
                contador = 0
            elif i != "-":
                contador = 0
    # print("lista estados eliminados tamanho : " + format(len(estadoeliminado)) + " =", end="")
    # print(estadoeliminado)
    for i in range(len(automato)):
        for j in range(len(automato[i])):
            if automato[i][j] == estadoeliminado[0]:
                automato[i][j] = "-"
    # for e in automato:
    #     print(e)


    return automato



if __name__ == '__main__':
    try:
        arquivo = open("Como usar", "r")
        texto = arquivo.readlines()
        for elemento in texto:
            print(elemento)
    except:
        print("Arquivo de ajuda não encontrado!")
        print("Para rodar o programa compile o arquivo main.")
