import consultas
import util

opcao = 0 
while opcao != 3: 
    print("----------------------------------\n")
    print("1 - Gerenciamento \n")
    print("2 - Votação \n")
    print("3 - Sair \n")
    print("----------------------------------\n")
    try:
        opcao = int(input("Selecione uma opção: "))
    except:
        print("Digite um número válido!")
        opcao = 0
    print("----------------------------------\n")


    match opcao: 
        case 1:
            print("Opção de gerenciamento selecionado\n")
            util.salvar_log("Opção de gerenciamento selecionado")

            opcaoGerenciamento = -1
            while opcaoGerenciamento != 0:
                print("-----------GERENCIAMENTO-----------\n")
                print("1 - Cadastrar Eleitor \n")
                print("2 - Editar Eleitor \n")
                print("3 - Remover Eleitor \n")
                print("4 - Buscar Eleitor \n")
                print("5 - Listar Eleitores \n")
                print("6 - Gerenciar Candidatos \n")
                print("0 - Voltar ao menu principal \n")
                print("----------------------------------\n")
                try:
                    opcaoGerenciamento = int(input("Selecione uma opção: "))
                except:
                    print("Digite um número válido!")
                    opcaoGerenciamento = -1
                print("----------------------------------\n")

                match opcaoGerenciamento:
                    case 1 :
                        print("Entrou em Gerenciamento -> Cadastrar Eleitor\n")
                        util.salvar_log("GERENCIMANETO - Cadastrar Eleitor")
                        pass
                    case 2 :
                        print("Entrou em Gerenciamento -> Editar Eleitor\n")
                        util.salvar_log("GERENCIMANETO - Editar Eleitor")
                        pass
                    case 3 :
                        print("Entrou em Gerenciamento -> Remover Eleitor\n")
                        util.salvar_log("GERENCIMANETO - Remover Eleitor")
                        pass
                    case 4 :
                        print("Entrou em Gerenciamento -> Buscar Eleitor\n")
                        util.salvar_log("GERENCIMANETO - Buscar Eleitor")
                        pass
                    case 5 :
                        print("Entrou em Gerenciamento -> Listar Eleitores\n")
                        util.salvar_log("GERENCIMANETO - Listar Eleitores")
                        pass
                    case 6 :
                        print("Entrou em Gerenciamento -> Gerenciar Candidatos\n")
                        util.salvar_log("GERENCIMANETO - Gerenciar Candidatos")
                        pass
                    case 0 :
                        print("Entrou em Gerenciamento -> Voltar ao menu principal\n")
                        util.salvar_log("GERENCIMANETO - Voltar ao menu principal")
                        pass
                    case _:
                        print("Gerencimaneto -> Ops! Houve um erro. Opção inválida\n")
                        util.salvar_log("Gerencimaneto -> Ops! Houve um erro. Opção inválida")
            
            pass
        case 2:
            print("Opção de votação selecionado\n")
            util.salvar_log("Opção de votação selecionado")
            
            opcaoVotacao = -1
            while opcaoVotacao != 0:
                print("-----------VOTAÇÃO-----------\n")
                print("1 - Abrir sistema de votação \n")
                print("2 - Resultados \n")
                print("3 - Auditoria \n")
                print("0 - Sair \n")
                print("----------------------------------\n")
                try:
                    opcaoVotacao = int(input("Selecione uma opção: "))
                except:
                    print("Digite um número válido!")
                    opcaoVotacao = -1
                print("----------------------------------\n")

                match opcaoVotacao:
                    case 1 :
                        print("Entrou em Votação -> Abrir sistema de votação\n")
                        util.salvar_log("VOTAÇÃO - Abrir sistema de votação")
                        pass
                    case 2 :
                        print("Entrou em Votação -> Resultados\n")
                        util.salvar_log("VOTAÇÃO - Resultados")
                    
                        opcaoVotacaoResultados = -1
                        while opcaoVotacaoResultados != 0:
                            print("-----------VOTAÇÃO RESULTADOS-----------\n")
                            print("1 - Boletim de urna \n")
                            print("2 - Estatística \n")
                            print("3 - Votos por partido \n")
                            print("4 - Validação integridade \n")
                            print("0 - Voltar \n")
                            print("----------------------------------\n")
                            try:
                                opcaoVotacaoResultados = int(input("Selecione uma opção: "))
                            except:
                                print("Digite um número válido!")
                                opcaoVotacaoResultados = -1
                            print("----------------------------------\n")

                            match opcaoVotacaoResultados:
                                case 1 :
                                    print("Entrou em Votação Resultados -> Boletim de urna\n")
                                    util.salvar_log("VOTAÇÃO RESULTADOS - Boletim de urna")
                                    pass
                                case 2 :
                                    
                                    print("Entrou em Votação Resultados -> Estatística\n")
                                    util.salvar_log("VOTAÇÃO RESULTADOS - Estatística")
                                    pass
                                case 3 :
                                    print("Entrou em Votação Resultados -> Votos por partido\n")
                                    util.salvar_log("VOTAÇÃO RESULTADOS - Votos por partido")
                                    pass
                                case 4 :
                                    print("Entrou em Votação Resultados -> Validação integridade\n")
                                    util.salvar_log("VOTAÇÃO RESULTADOS - Validação integridade")
                                    pass
                                case 0 :
                                    print("Entrou em Votação Resultados -> Voltar\n")
                                    util.salvar_log("VOTAÇÃO RESULTADOS - Voltar")
                                    pass
                                case _:
                                    print("Votação -> Resultados -> Ops! Houve um erro. Opção inválida\n")
                                    util.salvar_log("Votação -> Resultados -> Ops! Houve um erro. Opção inválida")
                        pass
                    case 3 :
                        print("Entrou em Votação -> Auditoria\n")
                        util.salvar_log("VOTAÇÃO - Auditoria")

                        opcaoVotacaoAuditoria = -1
                        while opcaoVotacaoAuditoria != 0:
                            print("-----------VOTAÇÃO AUDITORIA-----------\n")
                            print("1 - Logs Ocorrencia \n")
                            print("2 - Protocolos \n")
                            print("0 - Voltar \n")
                            print("----------------------------------\n")
                            try:
                                opcaoVotacaoAuditoria = int(input("Selecione uma opção: "))
                            except:
                                print("Digite um número válido!")
                                opcaoVotacaoAuditoria = -1
                            print("----------------------------------\n")

                            match opcaoVotacaoAuditoria:
                                case 1 :
                                    print("Entrou em Votação Auditoria -> Logs Ocorrencia\n")
                                    util.salvar_log("VOTAÇÃO AUDITORIA - Logs Ocorrencia")
                                    pass
                                case 2 :
                                    print("Entrou em Votação Auditoria -> Protocolos\n")
                                    util.salvar_log("VOTAÇÃO AUDITORIA - Protocolos")
                                    pass
                                case 0 :
                                    print("Entrou em Votação Auditoria -> Voltar\n")
                                    util.salvar_log("VOTAÇÃO AUDITORIA - Voltar")
                                    pass
                                case _:
                                    print("Votação -> Auditoria -> Ops! Houve um erro. Opção inválida\n")
                                    util.salvar_log("Votação -> Auditoria -> Ops! Houve um erro. Opção inválida")
                        pass

                    case 0 :
                        print("Entrou em Votação -> Sair\n")
                        util.salvar_log("VOTAÇÃO - Sair")
                        pass
                    case _:
                        print("Votação -> Ops! Houve um erro. Opção inválida\n")
                        util.salvar_log("Votação -> Ops! Houve um erro. Opção inválida")
            pass
        case 3:
            print("Saindo do programa\n")
            util.salvar_log("MENU INICIAL - Saindo do programa")
            
            pass
        case _ :
            print("Ops! Houve um erro. Opção inválida\n")
            util.salvar_log("MENU INICIAL - Ops! Houve um erro. Opção inválida")
            
            pass 
else :
    with open("historico.txt", "r", encoding="utf-8") as arq:
        print("\nHistórico:")
        print(arq.read())

    print("\nVocê saiu do projeto de votação\n")
