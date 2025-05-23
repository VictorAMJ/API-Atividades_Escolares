# 🖥️ API - Atividades Escolares 📘

Esta API foi desenvolvida para gerenciar atividades escolares de uma instituição de ensino. Ela depende da **API Gestão Escolar**, que fornece informações sobre os alunos, professores e turmas vinculadas às atividades.

## ⚙️ Tecnologias Utilizadas

- Python 3
- Flask
- SQLAlchemy
- SQLite (banco de dados local)
- Docker

## 📁 Estrutura do Projeto

```bash
API-Atividades_Escolares/
├── app.py                # Inicialização da aplicação Flask
├── config.py             # Configurações de banco de dados
├── modelAtividade.py     # Modelo da tabela Atividades
├── rotasAtividade.py     # Rotas para manipulação das atividades
├── requirements.txt      # Dependências da aplicação
├── Dockerfile            # Dockerização do projeto
└── instance/app.db       # Banco de dados SQLite
```

---

## ▶️ Como Executar a API

```bash
# Clone o repositório
git clone <repositorio-url>
cd API-Atividades_Escolares

# Crie ambiente virtual e ative
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor
python app.py
```

A aplicação estará disponível em:
📍 `http://localhost:8081`

---

## 📌 Endpoints Disponíveis

- `POST /atividade` – Cria uma nova atividade
- `GET /atividade` – Lista todas os alunos

## 🧑‍💻 Autores

- Gabriela Araujo Rodrigues
- Victor Alexandre Martuzzo de Jesus
- Yara Castro Lima









