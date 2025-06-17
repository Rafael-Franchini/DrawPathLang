
# DrawPathLang 🎨

Uma Linguagem Específica de Domínio (DSL) para criação de desenhos gráficos usando comandos textuais simples, com execução via Python e Turtle Graphics.

---

## 📌 Descrição

DrawPathLang é uma linguagem desenvolvida como projeto acadêmico para a disciplina de Teoria da Computação e Compiladores – 2025.

Ela permite ao usuário criar formas geométricas básicas como linhas e círculos através de uma linguagem textual própria, interpretada por um conjunto de módulos que inclui análise léxica, sintática, semântica e execução gráfica.

---

## 🚀 Como Executar

### Requisitos:

- Python 3.x
- Módulo turtle (padrão do Python)

### Passos:

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/DrawPathLang.git
```

2. Acesse a pasta do projeto:

```bash
cd DrawPathLang
```

3. Execute o programa principal:

```bash
python main.py
```

4. Escolha uma das opções de entrada:

- 1 → Ler comandos de um arquivo `.dpath`
- 2 → Digitar comandos manualmente
- 3 → Modo interativo simples (linha por linha)

---

## 🖋️ Exemplo de Código DrawPathLang (.dpath)

Exemplo de um desenho de uma casa com uma janela circular:

```
iniciar_em (0, 0)
linha_para (50, 0)
linha_para (50, 50)
linha_para (0, 50)
linha_para (0, 0)
circulo_em (25, 25) raio 20
```

---

## 📂 Estrutura de Arquivos

```
DrawPathLang/
├── comandos.py       # Definição das funções de comandos (ex: iniciar_em, linha_para)
├── executar.py       # Gerencia o fluxo de execução da linguagem
├── lexer.py          # Analisador Léxico
├── parser.py         # Analisador Sintático
├── semantic.py       # Analisador Semântico
├── semantico.py      # Regras e validações adicionais da semântica
├── token_type.py     # Definição dos tipos de tokens
├── tokens_util.py    # Funções utilitárias para manipulação de tokens
├── main.py           # Arquivo principal de execução (entrada do programa)
├── exemplo.dpath     # Exemplo de código fonte em DrawPathLang
├── ex2.dpath         # Segundo exemplo de código fonte
└── README.md         # Este arquivo
```

---

## 🧱 Fluxo de Execução Interno

1. main.py → Lê a entrada do usuário.
2. lexer.py → Tokenização dos comandos.
3. parser.py → Análise sintática.
4. semantic.py / semantico.py → Análise semântica e validação.
5. comandos.py → Implementação dos comandos da linguagem.
6. executar.py → Faz a execução dos comandos.
7. Turtle → Gera o desenho gráfico.

---


## 👨‍💻 Autores

Rafael Franchini  
Otavio Fadini  
Danilo Muller  

Estudantes de Engenharia da Computação  
Disciplina: Teoria da Computação e Compiladores – 2025  
