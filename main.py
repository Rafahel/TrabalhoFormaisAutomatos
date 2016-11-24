from modulos import *


def main():
    nome = input("Nome do arquivo com o AFD: ")
    try:
        arquivo = open(nome, "r")
        linhas = arquivo.readlines()
        cabecalho = linhas[0]
        linhas.pop(0)
        print("\n\n\n__Eliminando estados incalcansaveis__\n")
        newautomato = eliminainalcansaveis(linhas)
        for elemento in newautomato:
            if elemento[0] != '-':
                print(elemento)
        automato = eliminaMortos(newautomato)
        print("\n\n__Automato com os estados mortos removidos__\n")
        for elemento in cabecalho:
            print("  " + elemento + "  ", end="")
        print("")
        print("______________________________")
        for elemento in automato:
            if elemento[0] != "-":
                print(elemento)
        print("\nRemovendo estados vazios...")
        print("\n\n-----AUTOMATO FINAL-----\n")
        for elemento in cabecalho:
            print("  " + elemento, end="")
        print("\n______________________________\n")
        automato = eliminavazio(automato)
        automato = eliminanaoexistente(automato)
        # for i in range(len(automato)):
        #     if automato[i][0] == "-":
        #         continue
        #     else:
        #         for j in range(len(automato[i])):
        #             print(automato[i][j], end="  ")
        #         print("")
        for elemento in automato:
            if elemento[0] != "-":
                print(elemento)
    except ValueError:
        print("Nome do arquivo ou formato incorreto,"
              " rode o programa e tente novamente...")

if __name__ == '__main__':
    print("O programa já conta com 5 exemplos camados aut1, aut2, aut3, aut4, aut5.")
    print("Apenas digite o nome do automato que deseja testar e compare a saída com o arquivo de texto.")
    print("Qualquer problema entrar em contato com: rafahelmello@gmail.com")
    main()
