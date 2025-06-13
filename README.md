          
# 🍽️ API de Reservas

API REST desenvolvida em FastAPI para gerenciamento de reservas de restaurante, incluindo controle de mesas e diferentes níveis de usuários.

## ✨ Funcionalidades

- 📋 Gerenciamento de mesas e status
- 🎫 Sistema de reservas
- 👨‍🍳 Confirmação por garçons
- 📊 Relatórios personalizados

## 🛠️ Tecnologias

- FastAPI
- SQLAlchemy
- SQLite
- Alembic
- Pydantic
- Uvicorn

## 📦 Pré-requisitos

- Python 3.8+
- pip

## 🚀 Instalação

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/api-reservas.git
cd api-reservas
```

2. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure o ambiente
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Execute as migrações
```bash
alembic upgrade head
```

6. Inicie o servidor
```bash
uvicorn src.main:app --reload
```

## 📚 Documentação

Acesse a documentação interativa em:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔍 Endpoints Principais

- `GET /`: Página inicial
- `POST /tables/`: Criar mesa
- `GET /tables/`: Listar mesas
- `POST /reservations/`: Criar reserva
- `DELETE /reservations/{id}`: Cancelar reserva
- `PUT /reservations/{id}/confirm`: Confirmar reserva

## 📊 Relatórios

- `GET /reservations/reports/by-period`: Reservas por período
- `GET /reservations/reports/by-table/{id}`: Reservas por mesa
- `GET /reservations/reports/by-waiter/{id}`: Reservas por garçom

## 👥 Autores

- William Rigne - [GitHub](github.com/Wilwalker27)
- Antonio Favero - [Linkedin](https://www.linkedin.com/in/antonio-cardoso-favero-8a1301296?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes

---
⌨️ com ❤️ por Will 🚀
        
