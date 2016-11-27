from modulos import *


def main():
    while True:
        nome = input("Nome do arquivo com o AFD ou digite ajuda para saber como usar: ")
        try:
            arquivo = open(nome, "r")
            linhas = arquivo.readlines()
            descricao = linhas[0]
            linhas.pop(0)
            cabecalho = linhas[0]
            linhas.pop(0)
            original = []
            print("\n\n\n__Eliminando estados incalcançaveis__\n")
            newautomato = eliminainalcancaveis(linhas)
            for elemento in linhas:
                original.append(elemento.split())
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
            # print("\nRemovendo estados vazios...")
            print("\n\n\n" + descricao)
            mostraoriginal(cabecalho, original)
            print("\n\n-----AUTOMATO FINAL-----\n")
            for elemento in cabecalho:
                print("  " + elemento, end="")
            print("\n______________________________\n")
            automato = eliminavazio(automato)
            automato = eliminanaoexistente(automato)
            for elemento in automato:
                if elemento[0] != "-":
                    print(elemento)
            break
        except:
            print("Nome do arquivo ou formato incorreto,"
                  " tente novamente...")
            continue

if __name__ == '__main__':
    print("O programa já conta com 5 exemplos camados aut1, aut2, aut3, aut4, aut5.")
    print("Apenas digite o nome do automato que deseja testar e compare a saída com o arquivo de texto.")
    print("Qualquer problema entrar em contato com: rafahelmello@gmail.com")
    main()
