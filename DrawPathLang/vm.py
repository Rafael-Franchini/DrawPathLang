def executar(comandos):
    pos_atual = None
    for cmd in comandos:
        if cmd.__class__.__name__ == "IniciarEm":
            pos_atual = (cmd.x, cmd.y)
            print(f"Iniciando em {pos_atual}")

        elif cmd.__class__.__name__ == "LinhaPara":
            print(f"Linha de {pos_atual} para ({cmd.x}, {cmd.y})")
            pos_atual = (cmd.x, cmd.y)

        elif cmd.__class__.__name__ == "CurvaPara":
            print(f"Curva de {pos_atual} para ({cmd.x}, {cmd.y}) com raio {cmd.raio}")
            pos_atual = (cmd.x, cmd.y)

        elif cmd.__class__.__name__ == "CirculoEm":
            print(f"Círculo em ({cmd.x}, {cmd.y}) com raio {cmd.raio}")

