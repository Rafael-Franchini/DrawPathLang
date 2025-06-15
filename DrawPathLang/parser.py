from lexer import Lexer, TokenType
from comandos import IniciarEm, LinhaPara, CurvaPara, CirculoEm

def parser(texto):
    lexer = Lexer(texto)
    tokens = lexer.tokenizar()
    comandos = []
    pos = 0

    def eat(tipo_esperado):
        nonlocal pos
        if pos >= len(tokens):
            raise Exception("Fim inesperado dos tokens")
        token = tokens[pos]
        if token.tipo != tipo_esperado:
            raise Exception(f"Esperado {tipo_esperado}, mas encontrou {token.tipo} ({token.valor})")
        pos += 1
        return token

    while pos < len(tokens) and tokens[pos].tipo != TokenType.EOF:
        token = tokens[pos]

        if token.tipo == TokenType.IDENT:
            nome = token.valor
            pos += 1  # consumiu o IDENT

            eat(TokenType.LPAREN)
            x = eat(TokenType.NUM).valor
            eat(TokenType.VIRGULA)
            y = eat(TokenType.NUM).valor
            eat(TokenType.RPAREN)

            if nome == "iniciar_em":
                comandos.append(IniciarEm(x, y))
            elif nome == "linha_para":
                comandos.append(LinhaPara(x, y))
            elif nome == "curva_para":
                eat(TokenType.RAIO)
                r = eat(TokenType.NUM).valor
                comandos.append(CurvaPara(x, y, r))
            elif nome == "circulo_em":
                eat(TokenType.RAIO)
                r = eat(TokenType.NUM).valor
                comandos.append(CirculoEm(x, y, r))
            else:
                raise Exception(f"Comando desconhecido: {nome}")

        else:
            raise Exception(f"Token inesperado: {token}")

    return comandos
