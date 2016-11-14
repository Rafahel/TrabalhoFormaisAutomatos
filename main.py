def main():
    while True:
        nome = input("Nome do arquivo com o AFD: ")
        try:
            arquivo = open(nome, "r")
            linhas = arquivo.readlines()
            cabecalho = linhas[0]
            linhas.pop(0)
            automato = []
            for elemento in linhas:
                automato.append(elemento.split())
            automato = eliminaMortos(automato)
            print("Automato com os estados mortos removidos:\n")
            for elemento in cabecalho:
                print("  " + elemento + "  ", end="")
            print("")
            print("______________________________")
            for elemento in automato:
                if elemento[0] != "-":
                    print(elemento)
            print("FIM.")
            break
        except:
            print("Nome do arquivo ou formato incorreto,"
                  " rode o programa e tente novamente...")





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


if __name__ == '__main__':
    main()
