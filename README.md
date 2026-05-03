# Micro-API de Gerenciamento de Tarefas

Este é um Produto Mínimo Viável (MVP) desenvolvido como Laboratório Introdutório para a Pós-Graduação. O objetivo é demonstrar a construção de uma aplicação simples, usando e testando diversas ferramentas de Inteligência Artificial Generativa em todas as etapas do ciclo de desenvolvimento de software.

## Objetivo e Descrição
Desenvolvimento de uma API RESTful simples construída em **Python (FastAPI)** que permite realizar operações CRUD (Criar, Ler, Atualizar e Excluir). A persistência de dados foi implementada em memória para que o escopo ficasse restrito e assim fosse possível atingir os objetivos do laboratório.

## Tech Stack
* **Linguagem/Framework:** Python 3.10+, FastAPI, Pydantic
* **Testes:** Pytest, HTTPX
* **Ferramentas de IA:** GitHub Copilot (geração de testes e autocomplete) e Claude 3.5/Gemini (Arquitetura, Refatoração e Documentação).

## Como a IA Acelerou Este Projeto
A IA Generativa foi o foco central durante esse estudo e a produção desse MVP. Seu uso, ao longo desse Ciclo de Vida de Desenvolvimento de Software (SDLC), se deu predominantemente atraves do pair programming.

Ao todo, foram mais de 70 interações com as IAs:

1. **Geração de Boilerplate e Modelos:** Começou-se com a metodologia dp Zero-Shot, para analisar como era o comportamento das ferramentas em prompts mais genéricos. Depois, para continuar a criação da api adicionou-se Persona + Constraints + Detalhes ao prompt inicial através de iterações. Por ultimo, retirou-se elementos que apenas acrescentavam verbosidade e chegou-se ao seguinte prompt: 

```
Atue como um Engenheiro de Software Sênior com solida experiencia em API RESTful em Python, Pytest e FastAPI. Crie uma micro-API CRUD usando FastAPI para gerenciar tarefas (To-Do List). Restrições: Use apenas uma lista em memória para persistência (sem banco de dados real), utilize Pydantic para modelagem e inclua tratamento de erros com HTTP Status Code(400 e 404).
```

Aqui, notou-se um pequeno ganho de tempo apenas. Talvez por ser uma arquitetura já muito conhecida e utilizada. 

2. **Desenvolvimento Orientado a Testes (TDD):** A IA foi instruída a gerar os casos de teste (no arquivo `test_main.py`) com base na regra de negócio dos endpoints, economizando muitas horas de codificação manual e acelerou ainda mais quando solicitou-se a geração de testes que cobrissem cenários de borda e chegou-se ao seguinte prompt: 

```
Dado o código `main.py` assuma o papel de Engenheiro Especialista em QA e escreva testes unitários e testes de borda, utilizando o framework `pytest` e o `TestClient` do FastAPI.
```

3. **Documentação e Empacotamento:** O formato estruturado deste README, bem como a geração dos arquivos `.gitignore` e `Makefile`, foram acelerados utilizando estruturação do prompt através do padrão: Contexto, Objetivo, Audiência e Formato de Resposta (CO-STAR).


## Instalação e Execução

**1. Instale as dependências:**
`make install` ou `pip install -r requirements.txt`

**2. Rode a aplicação:**
`make run` ou `uvicorn main:app --reload`

**3. Rode os testes:**
`make test` ou `pytest test_main.py`

----

Troubleshooting for macOS: Erro de Instalação (macOS / Python 3.14+)
Se a instalação falhar no pacote pydantic-core (erro de compilação Rust/Maturin), devido ao Python 3.14+ ainda ser recente para alguns binários.

Instale o Python 3.13: `brew install python@3.13`

Recrie o ambiente forçando esta versão: 
```
rm -rf .venv
/opt/homebrew/bin/python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Guia do Usuário (Para iniciantes)
Se você não é desenvolvedor ou é iniciante, siga este passo a passo para rodar a aplicação em sua máquina:

a. Ative o ambiente: No terminal, dentro da pasta onde o projeto foi clonado, digite source .venv/bin/activate (Mac/Linux) ou .venv\Scripts\activate (Windows).

b. Inicie o servidor: Digite uvicorn main:app --reload.

c. Acesse a Interface: Com o terminal aberto, abra o seu navegador e acesse: http://127.0.0.1:8000/docs. Você verá algo assim:

<img width="626" height="586" alt="image" src="https://github.com/user-attachments/assets/a763a3e4-fa6d-4735-aaad-6ff55f8dd626" />




Como usar/testar/brincar:

- Escolha um dos métodos e edite a request (ex: POST para criar tarefa).
- Clique em "Try it out".
- Preencha os dados e clique em "Execute".

Você deverá ver uma response tipo essa:

  <img width="1093" height="526" alt="image" src="https://github.com/user-attachments/assets/e28f5eb8-ea5f-456a-a8e4-555343578550" />
  </br>
  <img width="1092" height="510" alt="image" src="https://github.com/user-attachments/assets/c53fb402-ea21-40b6-a52a-7a3efa40b749" />


