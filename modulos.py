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
        c = 0
        for j in range(1, len(automato[i])):
            # print(automato[i][j])
            if automato[i][j] == '-':
                c += 1
            if c == 2 and "*" not in automato[i][0]:
                c = 0
                automato[i][0] = "-"
    # for elemento in automato:
    #     print(elemento)
    return automato


def eliminainalcancaveis(automato):
    automatoaux = []
    alcancados = []
    for elemento in automato:
        automatoaux.append(elemento.split())
    # print(automatoaux)
    for elemento in automatoaux:
        for transicao in elemento:
            # print(transicao)
            if "->" in elemento[0]:
                alcancados.append(transicao)
    if len(alcancados) > 0:
        alcancados.pop(0)
    # print(alcancados)
    for tr in alcancados:
        for elemento in automatoaux:
            if tr in elemento[0]:
                for i in range(1, len(elemento)):
                    # print(elemento[i])
                    if elemento[i] not in alcancados:
                        alcancados.append(elemento[i])
    alcancados.append(automatoaux[0][0])
    for i in range(len(alcancados)):
        alcancados.append("*"+alcancados[i])
        alcancados.append("->" + alcancados[i])
        alcancados.append("*->" + alcancados[i])
    # print(alcancados)
    for i in range(len(automatoaux)):
        # print(automatoaux[i][0])
        if automatoaux[i][0] not in alcancados:
            automatoaux[i][0] = "-"

    # for elemento in automatoaux:
    #     if elemento[0] != "-":
    #         print(elemento)
    return automatoaux

def eliminanaoexistente(automato):
    existe = []
    for elemento in automato:
        if elemento[0] != "-":
            existe.append(elemento[0])

    for j in range(2):
        for i in range(len(existe)):
            if "*" in existe[i]:
                existe.append(existe[i].replace("*", ""))
            if "->" in existe[i]:
                existe.append(existe[i].replace("->", ""))
            if "*->" in existe[i]:
                existe.append(existe[i].replace("*->", ""))
            if "=" in existe[i]:
                existe.append(existe[i].replace("=", ""))
    # print(existe)
    for i in range(len(automato)):
        for j in range(len(automato[i])):
            if automato[i][j] not in existe:
                automato[i][j] = "-"
    return automato

def mostraoriginal(cabecalho, original):
    print("\n\n-----AUTOMATO ORIGINAL-----\n")
    for elemento in cabecalho:
        print("  " + elemento, end="")
    print("\n______________________________\n")
    for elemento in original:
        print(elemento)

if __name__ == '__main__':
    try:
        arquivo1 = open("Como usar", "r")
        texto = arquivo1.readlines()
        for elemento in texto:
            print(elemento)
    except:
        print("Arquivo de ajuda não encontrado!")
        print("Para rodar o programa compile o arquivo main.")

