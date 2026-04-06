import consultas
import util

opcao = 0 
while opcao != 3: 
    print("----------------------------------\n")
    print("1 - Gerenciamento \n")
    print("2 - Votação \n")
    print("3 - Sair \n")
    print("----------------------------------\n")
    opcao = int(input("Selecione uma opção: "))
    print("----------------------------------\n")


    match opcao: 
        case 1:
            print("Opção de gerenciamento selecionado")
            with open("historico.txt", "a", encoding="utf-8") as arq:
                arq.write("Opção de gerenciamento selecionado\n")
            
            pass
        case 2:
            print("Opção de votação selecionado")
            with open("historico.txt", "a", encoding="utf-8") as arq:
                arq.write("Opção de votação selecionado\n")
            
            pass
        case 3:
            print("Saindo")
            with open("historico.txt", "a", encoding="utf-8") as arq:
                arq.write("Saindo\n")
            
            pass
        case default :
            print("Ops! Houve um erro. Opção inválida")
            with open("historico.txt", "a", encoding="utf-8") as arq:
                arq.write("Ops! Houve um erro. Opção inválida\n")
            
            pass 
else :
    with open("historico.txt", "r", encoding="utf-8") as arq:
        print("\nHistórico:")
        print(arq.read())

    print("\nVocê saiu do projeto de votação\n")
