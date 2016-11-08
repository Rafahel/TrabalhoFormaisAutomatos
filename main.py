
def main():
    arquivo = open("aut", "r")
    linhas = arquivo.readlines()
    cabecalho = linhas[0]
    linhas.pop(0)
    novosEstados = []
    automato = []
    for elemento in linhas:
        automato.append(elemento.split())
    tam = automato[0]
    print(len(tam))
    for i in range(len(automato)):
        for j in range(len(tam)):
            print(automato[i][j])
            if "," in automato[i][j]:
                novoEstado = automato[i][j]
                novoEstado = novoEstado.replace(",", "")
                automato[i][j] = novoEstado

    for elemento in automato:
        print(elemento)

    for i in range(len(automato)):
        for j in range(len(tam)):
            print(automato[i][j])
            if "," in automato[i][j]:
               print(automato[i][j])







if __name__ == '__main__':
    main()