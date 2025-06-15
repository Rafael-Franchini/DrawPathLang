def analisar_semantica(comandos):
    iniciou = False
    for cmd in comandos:
        if cmd.__class__.__name__ == "IniciarEm":
            iniciou = True
        elif not iniciou:
            raise Exception("Erro semântico: comando antes de iniciar_em")
