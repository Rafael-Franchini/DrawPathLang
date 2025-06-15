import turtle

def interpretar(comandos):
    turtle.title("DrawPathLang")
    turtle.speed(1)

    for linha in comandos:
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue

        if linha.startswith("iniciar_em"):
            x, y = extrair_coordenadas(linha)
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

        elif linha.startswith("linha_para"):
            x, y = extrair_coordenadas(linha)
            turtle.goto(x, y)

        elif linha.startswith("curva_para"):
            x, y, r = extrair_coordenadas_raio(linha)
            turtle.goto(x, y)
            turtle.circle(r, 90)

        elif linha.startswith("circulo_em"):
            x, y, r = extrair_coordenadas_raio(linha)
            turtle.penup()
            turtle.goto(x, y - r)
            turtle.pendown()
            turtle.circle(r)

    try:
        turtle.done()
    except turtle.Terminator:
        pass

def extrair_coordenadas(texto):
    coords = texto.split("(")[1].split(")")[0]
    x_str, y_str = coords.split(",")
    return float(x_str.strip()), float(y_str.strip())

def extrair_coordenadas_raio(texto):
    partes = texto.split("raio")
    coords = partes[0].split("(")[1].split(")")[0]
    x_str, y_str = coords.split(",")
    raio = float(partes[1].strip())
    return float(x_str.strip()), float(y_str.strip()), raio