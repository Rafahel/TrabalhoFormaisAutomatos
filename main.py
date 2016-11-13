
def main():
    arquivo = open("aut3", "r")
    linhas = arquivo.readlines()
    cabecalho = linhas[0]
    linhas.pop(0)
    automato = []
    for elemento in linhas:
        automato.append(elemento.split())
    tam = len(automato[0])
    automato = eliminaMortos(automato, tam)
    print("Automato com os estados mortos removidos:")
    for elemento in automato:
        print(elemento)


def eliminaInalcancaveis(automato):
    pass



def eliminaMortos(automato, tam):
    flag = 0
    novoatutomato = []
    rmEstados = []
    nEstados = []
    for elemento in automato:
        t = len(elemento)
        estado = elemento[0]
        for i in range(len(elemento)):
            if elemento[i] == estado:
                flag+=1
                # print(flag)
        if flag == t:
            rmEstados.append(estado)
        flag = 0
    for x in rmEstados:
        for i in range(len(automato)):
            for j in range(len(automato[i])):
                if automato[i][j] == x:
                    automato[i][j] = "-"
                # print(automato[i][j])
    # for elemento in automato:
    #     print(elemento)
    return automato











if __name__ == '__main__':
    main()