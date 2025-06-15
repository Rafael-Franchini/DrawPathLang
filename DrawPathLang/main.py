from parser import parser
from semantico import analise_semantica
from executar import executar

print("=== DrawPathLang ===")
print("Escolha a forma de entrada:")
print("1 - Ler de arquivo .dpath")
print("2 - Digitar comandos DrawPathLang diretamente")

opcao = input("Opção (1 ou 2): ")

if opcao == "1":
    caminho = input("Nome do arquivo .dpath (padrão: exemplo.dpath): ") or "exemplo.dpath"
    with open(caminho, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
    comandos = parser(texto)
    comandos = analise_semantica(comandos)
    executar(comandos)

elif opcao == "2":
    print("Digite os comandos da DrawPathLang (linha por linha). Digite 'FIM' para terminar:")
    linhas = []
    while True:
        linha = input(">> ")
        if linha.strip().upper() == "FIM":
            break
        linhas.append(linha)
    texto = "\n".join(linhas)
    comandos = parser(texto)
    comandos = analise_semantica(comandos)
    executar(comandos)

else:
    print("Opção inválida. Encerrando.")
