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
    c = 0
    for i in range(len(automato)):
        # print(automato[i][0])
        for j in range(1, len(automato[i])):
            # print(automato[i][j])
            if automato[i][j] == '-':
                c += 1
            if c == 2:
                c = 0
                automato[i][0] = "-"
    # for elemento in automato:
    #     print(elemento)
    return automato


def eliminainalcansaveis(automato):
    automatoaux = []
    alcansados = []
    for elemento in automato:
        automatoaux.append(elemento.split())
    # print(automatoaux)
    for elemento in automatoaux:
        for transicao in elemento:
            # print(transicao)
            if "->" in elemento[0]:
                alcansados.append(transicao)
    if len(alcansados) > 0:
        alcansados.pop(0)
    # print(alcansados)
    for tr in alcansados:
        for elemento in automatoaux:
            if tr in elemento[0]:
                for i in range(1, len(elemento)):
                    # print(elemento[i])
                    if elemento[i] not in alcansados:
                        alcansados.append(elemento[i])
    alcansados.append(automatoaux[0][0])
    for i in range(len(alcansados)):
        alcansados.append("*"+alcansados[i])
        alcansados.append("->" + alcansados[i])
        alcansados.append("*->" + alcansados[i])
    # print(alcansados)
    for i in range(len(automatoaux)):
        # print(automatoaux[i][0])
        if automatoaux[i][0] not in alcansados:
            automatoaux[i][0] = "-"

    # for elemento in automatoaux:
    #     if elemento[0] != "-":
    #         print(elemento)
    return automatoaux


if __name__ == '__main__':
    try:
        arquivo1 = open("Como usar", "r")
        texto = arquivo1.readlines()
        for elemento in texto:
            print(elemento)
    except:
        print("Arquivo de ajuda não encontrado!")
        print("Para rodar o programa compile o arquivo main.")

