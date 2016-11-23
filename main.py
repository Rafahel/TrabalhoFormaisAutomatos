from modulos import *
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
            # automatoinicial = automato
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
            print("\n\n\n __Eliminando estados incalcansaveis__\n")
            for i in range(len(automato)):
                newautomato = eliminainalcansaveis(automato)
            for elemento in cabecalho:
                print("  " + elemento + "  ", end="")
            print("")
            print("______________________________")
            for elemento in newautomato:
                if elemento[0] != "-":
                    print(elemento)
            try:
                newautomato = eliminavazio(newautomato)
                print("\n\n\n    ---  Automato final  ---\n")
                for i in range(len(automato)):
                    newautomato = eliminainalcansaveis(automato)
                for elemento in cabecalho:
                    print("  " + elemento + "  ", end="")
                print("")
                print("______________________________")
                for elemento in newautomato:
                    if elemento[0] != "-":
                        print(elemento)
            except:
                print("\n\nNada mais a eliminar.")
            break
        except:
            print("Nome do arquivo ou formato incorreto,"
                  " rode o programa e tente novamente...")
            break










if __name__ == '__main__':
    main()
