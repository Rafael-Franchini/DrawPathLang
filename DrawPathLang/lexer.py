import re
from enum import Enum, auto

class TokenType(Enum):
    IDENT = auto()
    NUM = auto()
    LPAREN = auto()
    RPAREN = auto()
    VIRGULA = auto()
    RAIO = auto()
    EOF = auto()  # Fim do arquivo

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
    def __repr__(self):
        return f"Token({self.tipo}, {self.valor})"

class Lexer:
    def __init__(self, texto):
        self.texto = texto
        self.pos = 0
        self.tokens = []

#Função principal que lê o texto e gera os tokens
    def tokenizar(self):
        texto = self.texto
        padrao = re.compile(r'\s*(#.*|iniciar_em|linha_para|curva_para|circulo_em|-?\d+|\(|\)|,|raio)', re.IGNORECASE) #Expressão regular para encontrar partes válidas do código:
        while self.pos < len(texto):
            match = padrao.match(texto, self.pos)
            if not match:
                raise Exception(f"Erro léxico na posição {self.pos}")
            token_str = match.group(1)

            # Ignora comentários
            if token_str.startswith("#"):
                self.pos = match.end()
                continue

            # Verifica qual é o tipo do token encontrado e adiciona à lista
            if token_str.lower() in ["iniciar_em", "linha_para", "curva_para", "circulo_em"]:
                self.tokens.append(Token(TokenType.IDENT, token_str.lower()))
            elif re.match(r'-?\d+', token_str):
                self.tokens.append(Token(TokenType.NUM, int(token_str)))
            elif token_str == "(":
                self.tokens.append(Token(TokenType.LPAREN, token_str))
            elif token_str == ")":
                self.tokens.append(Token(TokenType.RPAREN, token_str))
            elif token_str == ",":
                self.tokens.append(Token(TokenType.VIRGULA, token_str))
            elif token_str.lower() == "raio":
                self.tokens.append(Token(TokenType.RAIO, token_str.lower()))
            else:
                raise Exception(f"Token desconhecido: {token_str}")

            self.pos = match.end()   # Avança a posição no texto
        # fim de arquivo
        self.tokens.append(Token(TokenType.EOF, None))
        return self.tokens
