
def main():
    arquivo = open("aut", "r")
    linhas = arquivo.readlines()
    cabecalho = linhas[0]
    linhas.pop(0)
    automato = []
    for elemento in linhas:
        automato.append(elemento.split())
    tam = automato[0]
    # print(len(tam))
    '''
        Cria uma lista [vetor] com as linhas e colunas do automato eliminando a linha 1 que é os simbolos a serem lidos
    '''
    for i in range(len(automato)):
        for j in range(len(tam)):
            # print(automato[i][j])
            if "," in automato[i][j]:
                novoEstado = automato[i][j]
                novoEstado = novoEstado.replace(",", "")
                automato[i][j] = novoEstado
    novoAutomato = []
    novoAutomato.append(automato[0])
    estadosExistentes = []
    estadosExistentes.append(automato[0][0])
    # print(novoAutomato)
    novosEstados = []
    '''
        Cria uma lista com os estados existentes
    '''
    for i in range(len(automato)):
        for j in range(len(tam)):
            # print(automato[i][0])
            if automato[i][0] not in estadosExistentes:
                estadosExistentes.append(automato[i][0])
    # print(estadosExistentes)
    for elemento in automato:
        print(elemento)







if __name__ == '__main__':
    main()