# drawpathlang/main.py
from parser import interpretar
import re

print("=== DrawPathLang ===")
print("Escolha a forma de entrada:")
print("1 - Ler de arquivo .dpath")
print("2 - Digitar comandos DrawPathLang diretamente")
print("3 - Conversar com o terminal (formato simples: comando valor x,y)")

opcao = input("Opção (1, 2 ou 3): ")

if opcao == "1":
    caminho = input("Nome do arquivo .dpath (padrão: exemplo.dpath): ") or "exemplo.dpath"
    with open(caminho, "r") as arquivo:
        comandos = arquivo.readlines()
        interpretar(comandos)

elif opcao == "2":
    print("Digite os comandos da DrawPathLang (linha por linha). Digite 'FIM' para terminar:")
    comandos = []
    while True:
        linha = input(">> ")
        if linha.strip().upper() == "FIM":
            break
        if any(linha.strip().startswith(val) for val in ["iniciar_em", "linha_para", "curva_para", "circulo_em"]):
            comandos.append(linha)
        else:
            print("[ERRO] Comando inválido. Use: iniciar_em, linha_para, curva_para ou circulo_em.")
    if comandos:
        interpretar(comandos)
    else:
        print("Nenhum comando válido foi fornecido. Encerrando.")

elif opcao == "3":
    print("Formato simples: circulo 10 0,0  | linha 100,200  | curva 150,150 30 | retangulo 10,10 40x30")
    print("Digite 'FIM' para encerrar.")
    comandos = []
    while True:
        entrada = input(">> ").lower().strip()
        if entrada == "fim":
            break

        if entrada.startswith("circulo"):
            match = re.findall(r"\d+", entrada)
            if len(match) >= 3:
                raio, x, y = match[0], match[1], match[2]
                comandos.append(f"circulo_em ({x}, {y}) raio {raio}")

        elif entrada.startswith("linha"):
            match = re.findall(r"\d+", entrada)
            if len(match) >= 2:
                x, y = match[0], match[1]
                comandos.append(f"linha_para ({x}, {y})")

        elif entrada.startswith("iniciar") or entrada.startswith("inicio"):
            match = re.findall(r"\d+", entrada)
            if len(match) >= 2:
                x, y = match[0], match[1]
                comandos.append(f"iniciar_em ({x}, {y})")

        elif entrada.startswith("curva"):
            match = re.findall(r"\d+", entrada)
            if len(match) >= 3:
                x, y, raio = match[0], match[1], match[2]
                comandos.append(f"curva_para ({x}, {y}) raio {raio}")

        elif entrada.startswith("retangulo"):
            match = re.findall(r"\d+", entrada)
            if len(match) >= 4:
                x, y, largura, altura = match[0], match[1], match[2], match[3]
                comandos.append(f"linha_para ({int(x)+int(largura)}, {y})")
                comandos.append(f"linha_para ({int(x)+int(largura)}, {int(y)+int(altura)})")
                comandos.append(f"linha_para ({x}, {int(y)+int(altura)})")
                comandos.append(f"linha_para ({x}, {y})")
                comandos.insert(0, f"iniciar_em ({x}, {y})")

        else:
            print("[!] Entrada inválida ou incompleta.")

    if comandos:
        interpretar(comandos)
    else:
        print("Nenhum comando válido foi fornecido. Encerrando.")

else:
    print("Opção inválida. Encerrando.")
