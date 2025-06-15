from comandos import IniciarEm, LinhaPara, CurvaPara, CirculoEm

def analise_semantica(comandos):
    pos_inicializada = False

    for cmd in comandos:
        if isinstance(cmd, IniciarEm):
            pos_inicializada = True

        elif isinstance(cmd, LinhaPara):
            if not pos_inicializada:
                raise Exception("Erro semântico: 'linha_para' usado antes de 'iniciar_em'")

        elif isinstance(cmd, CurvaPara):
            if not pos_inicializada:
                raise Exception("Erro semântico: 'curva_para' usado antes de 'iniciar_em'")
            if cmd.r <= 0:
                raise Exception(f"Erro semântico: raio inválido {cmd.r} em 'curva_para'")

        elif isinstance(cmd, CirculoEm):
            if cmd.r <= 0:
                raise Exception(f"Erro semântico: raio inválido {cmd.r} em 'circulo_em'")

        else:
            raise Exception(f"Erro semântico: comando desconhecido {cmd}")

    return comandos
