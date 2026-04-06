def salvar_log(texto):
    with open("historico.txt", "a", encoding="utf-8") as arq:
        arq.write(texto + "\n")