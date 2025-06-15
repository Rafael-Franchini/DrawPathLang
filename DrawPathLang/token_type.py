from enum import Enum

class TokenType(Enum):
    IDENT = "IDENT"
    NUM = "NUM"
    LPAREN = "("
    RPAREN = ")"
    VIRGULA = ","
    RAIO = "RAIO"
    EOF = "EOF"