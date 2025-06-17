
# DrawPathLang 🎨

Uma Linguagem Específica de Domínio (DSL) para Desenho de Caminhos Gráficos utilizando Python e Turtle Graphics.

---

## 📌 Descrição

DrawPathLang é uma linguagem criada como projeto acadêmico para a disciplina de Fundamentos em Linguagens Formais e Autômatos.

Ela permite ao usuário criar formas geométricas básicas como linhas e círculos através de uma linguagem textual própria, interpretada por um conjunto de módulos que inclui análise léxica, sintática, semântica e execução gráfica.

O projeto implementa um pipeline completo de linguagem:

- Lexer (Analisador Léxico)
- Parser (Analisador Sintático)
- Analisador Semântico
- Máquina Virtual / Interpretador
- Exemplo de uso com arquivos `.dpath`

---

## 🚀 Como Executar

Pré-requisitos:

- Python 3.x
- Módulo turtle (padrão no Python)

Passos:

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/DrawPathLang.git
```

2. Navegue até a pasta:

```bash
cd DrawPathLang
```

3. Execute o programa principal:

```bash
python main.py
```

4. Escolha o modo de entrada:

- Opção 1: Ler de um arquivo `.dpath`
- Opção 2: Digitar comandos diretamente
- Opção 3: Modo interativo via terminal

---

## 🖋️ Exemplo de Código DrawPathLang

Exemplo de um desenho simples de uma casa com uma janela circular:

```
iniciar_em (0, 0)
linha_para (50, 0)
linha_para (50, 50)
linha_para (0, 50)
linha_para (0, 0)
circulo_em (25, 25) raio 20
```

---

## 📂 Estrutura de Pastas

```
DrawPathLang/
├── comandos.py       # Definição das funções de comandos (ex: iniciar_em, linha_para)
├── executar.py       # Função que executa o fluxo de execução da linguagem
├── lexer.py          # Analisador Léxico
├── parser.py         # Analisador Sintático
├── semantic.py       # Analisador Semântico
├── semantico.py      # Regras e validações adicionais da semântica
├── token_type.py     # Tipos de tokens (enum ou constantes)
├── tokens_util.py    # Funções utilitárias para manipulação de tokens
├── main.py           # Arquivo principal de execução (interface com o usuário)
├── exemplo.dpath     # Exemplo de código fonte em DrawPathLang
├── ex2.dpath         # Segundo exemplo de código fonte
└── README.md         # Este arquivo

```

---

