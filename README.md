# Documentação do Backend
---

# LigaAPI-Backend
## Sistema de Gestão de Ligas Desportivas (Futebol)

**Ano letivo: 2025/2026**

![Django](https://img.shields.io/badge/Django-4.x-092E20)
![DRF](https://img.shields.io/badge/DRF-3.x-a30000)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB)
![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

**API REST | Django REST Framework**
Este projeto corresponde ao **backend de uma API REST pública**, desenvolvida com **Django REST Framework**, destinada à gestão de ligas de futebol.

---

## 1. 📌 Visão Geral

Este backend foi desenvolvido com **Django REST Framework** e fornece uma **API REST pública** para a gestão de ligas desportivas, equipas, jogadores e jogos.

---

A API permite gerir:
- Ligas
- Equipas
- Jogadores
- Jogos

Todas as entidades possuem **CRUD completo** e relacionamentos bem definidos.

---

## 2. 🛠️ Tecnologias Utilizadas

- Python 3
- Django
- Django REST Framework
- SQLite
- django-cors-headers
- python-decouple (Gestão de Variáveis de Ambiente)
- dj-database-url (Simplifica a configuração da base de dados usando uma única variável de ambiente)

---

## 3. 📂 Estrutura do Projeto

```
backend/
├── manage.py
├── db.sqlite3
│
├── backend/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── liga_api/
│   ├── models.py
│   ├── serializer.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── requirements.txt
```

---

## 4. 📊 Modelos de Dados

### Liga
- nome
- pais
- epoca

### Equipa
- nome
- cidade
- treinador
- ano_fundacao
- liga (FK)

### Jogador
- nome
- posicao
- numero
- idade
- equipa (FK)

### Jogo
- data
- golos_casa
- golos_fora
- liga (FK)
- equipa_casa (FK)
- equipa_visitante (FK)

---

## 5. 🧩 Diagrama de Relacionamento entre Entidades

O diagrama abaixo representa os relacionamentos entre as entidades do sistema:

- Uma **Liga** possui várias **Equipas**
- Uma **Liga** possui vários **Jogos**
- Uma **Equipa** possui vários **Jogadores**
- Um **Jogo** envolve duas **Equipas** (casa e visitante)

---

### Diagrama Entidade-Relacionamento (ER)

```
┌──────────┐        1       N        ┌──────────┐
│  Liga    │────────────────────────▶│  Equipa  │
│──────────│                         │──────────│
│ id       │                         │ id       │
│ nome     │                         │ nome     │
│ pais     │                         │ cidade   │
│ epoca    │                         │ treinador│
└──────────┘                         │ ano_fund │
      │                              │ liga_id  │
      │                              └──────────┘
      │ 1
      │
      │ N
┌──────────┐        1       N        ┌──────────┐
│  Liga    │────────────────────────▶│  Jogo    │
│──────────│                         │──────────│
│ id       │                         │ id       │
│ nome     │                         │ data     │
└──────────┘                         │ golos_c  │
                                     │ golos_f  │
                                     │ liga_id  │
                                     │ equipa_c │
                                     │ equipa_v │
                                     └──────────┘

┌──────────┐        1       N        ┌──────────┐
│  Equipa  │────────────────────────▶│ Jogador  │
│──────────│                         │──────────│
│ id       │                         │ id       │
│ nome     │                         │ nome     │
└──────────┘                         │ posicao  │
                                     │ numero   │
                                     │ idade    │
                                     │ equipa_id│
                                     └──────────┘
```

---

### Resumo dos Relacionamentos

| Entidade Origem | Relação | Entidade Destino |
| --------------- | ------- | ---------------- |
| Liga            | 1 : N   | Equipa           |
| Liga            | 1 : N   | Jogo             |
| Equipa          | 1 : N   | Jogador          |
| Equipa          | 1 : N   | Jogo (casa)      |
| Equipa          | 1 : N   | Jogo (visitante) |

---

## 6. 🌐 Endpoints da API

**URL Base**
```
http://127.0.0.1:8000/api/
```

| Entidade   | Endpoint           | Métodos              |
|------------|--------------------|----------------------|
| Ligas      | `/ligas/`          | GET, POST            |
|            | `/ligas/{id}/`     | GET, PUT, DELETE     |
| Equipas    | `/equipas/`        | GET, POST            |
|            | `/equipas/{id}/`   | GET, PUT, DELETE     |
| Jogadores  | `/jogadores/`      | GET, POST            |
|            | `/jogadores/{id}/` | GET, PUT, DELETE     |
| Jogos      | `/jogos/`          | GET, POST            |
|            | `/jogos/{id}/`     | GET, PUT, DELETE     |

---

## 7. 🔄 Serializers

Os serializers convertem os modelos em JSON e validam os dados recebidos.

Incluem campos apenas de leitura para facilitar o consumo da API:
- `equipa_casa_nome`
- `equipa_visitante_nome`
- `liga_nome`

---

## 8. ⚙️ Instalação e Execução

### Pré-requisitos
- Python 3.10+
- pip

### Passos

Clone o repositório:
```bash
git clone https://github.com/Afons19/LigasApi-Backend.git
```

Aceda o diretório:
```bash
cd backend
```

Crie ambiente virtual:
```bash
python -m venv venv
```

Ativar ambiente virtual:

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

Instalar dependências:
```bash
pip install -r requirements.txt
```

Executar migrações:
```bash
python manage.py migrate
```

Criar superutilizador (opcional):
```bash
python manage.py createsuperuser
```

Iniciar servidor:
```bash
python manage.py runserver
```

API disponível em:
```
http://127.0.0.1:8000/api/
```

---

## ✅ Requisitos Cumpridos

* API REST funcional
* CRUD completo para todas as entidades
* Relacionamentos claros entre modelos
* Código organizado por responsabilidade
* Base de dados SQLite

---

## 🎓 Projeto Académico

Este projeto foi desenvolvido para fins académicos no âmbito da unidade curricular de desenvolvimento web, cumprindo boas práticas de organização, modularidade e integração frontend-backend.

---

## 🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias abrindo um problema ou enviando um pull request.

---

## 📄 Licença

Este projeto é licenciado sob a Licença MIT.

---

# Backend Documentation
---

# LigaAPI-Backend
## Sports League Management System (Football)

**Academic Year: 2025/2026**

![Django](https://img.shields.io/badge/Django-4.x-092E20)
![DRF](https://img.shields.io/badge/DRF-3.x-a30000)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB)
![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

**REST API | Django REST Framework**
This project corresponds to the **backend of a public REST API**, developed with **Django REST Framework**, designed for managing football leagues.

---

## 1. 📌 Overview

This backend was developed with **Django REST Framework** and provides a **public REST API** for managing sports leagues, teams, players, and matches.

---

The API allows management of:
- Ligas (Leagues)
- Equipas (Teams)
- Jogadores (Players)
- Jogos (Matches)

All entities have **full CRUD** and well-defined relationships.

---

## 🛠️ Technologies Used

- Python 3
- Django
- Django REST Framework
- SQLite
- django-cors-headers
- python-decouple (Environment Variables Management)
- dj-database-url (Simplifies database configuration using a single environment variable)

---

## 📂 Project Structure

```
backend/
├── manage.py
├── db.sqlite3
│
├── backend/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── liga_api/
│   ├── models.py
│   ├── serializer.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── requirements.txt
```

---

## 📊 Data Models

### Liga
- nome
- pais
- epoca

### Equipa
- nome
- cidade
- treinador
- ano_fundacao
- liga (FK)

### Jogador
- nome
- posicao
- numero
- idade
- equipa (FK)

### Jogo
- data
- golos_casa
- golos_fora
- liga (FK)
- equipa_casa (FK)
- equipa_visitante (FK)

---

## 🧩 Entity Relationship Diagram

The diagram below represents the relationships between the system entities:

- One **Liga** has many **Equipas**
- One **Liga** has many **Jogos**
- One **Equipa** has many **Jogadores**
- One **Jogo** involves two **Equipas** (home and away)

---

### Entity-Relationship (ER) Diagram

```
┌──────────┐        1       N        ┌──────────┐
│  Liga    │────────────────────────▶│  Equipa  │
│──────────│                         │──────────│
│ id       │                         │ id       │
│ nome     │                         │ nome     │
│ pais     │                         │ cidade   │
│ epoca    │                         │ treinador│
└──────────┘                         │ ano_fund │
      │                              │ liga_id  │
      │                              └──────────┘
      │ 1
      │
      │ N
┌──────────┐        1       N        ┌──────────┐
│  Liga    │────────────────────────▶│  Jogo    │
│──────────│                         │──────────│
│ id       │                         │ id       │
│ nome     │                         │ data     │
└──────────┘                         │ golos_c  │
                                     │ golos_f  │
                                     │ liga_id  │
                                     │ equipa_c │
                                     │ equipa_v │
                                     └──────────┘

┌──────────┐        1       N        ┌──────────┐
│  Equipa  │────────────────────────▶│ Jogador  │
│──────────│                         │──────────│
│ id       │                         │ id       │
│ nome     │                         │ nome     │
└──────────┘                         │ posicao  │
                                     │ numero   │
                                     │ idade    │
                                     │ equipa_id│
                                     └──────────┘
```

---

### Relationship Summary

| Source Entity | Relationship | Target Entity |
| ------------- | ------------ | ------------- |
| Liga          | 1 : N        | Equipa        |
| Liga          | 1 : N        | Jogo          |
| Equipa        | 1 : N        | Jogador       |
| Equipa        | 1 : N        | Jogo (home)   |
| Equipa        | 1 : N        | Jogo (away)   |

---

## 🌐 API Endpoints

**Base URL**
```
http://127.0.0.1:8000/api/
```

| Entity      | Endpoint           | Methods           |
|-------------|--------------------|-------------------|
| Ligas       | `/ligas/`          | GET, POST         |
|             | `/ligas/{id}/`     | GET, PUT, DELETE  |
| Equipas     | `/equipas/`        | GET, POST         |
|             | `/equipas/{id}/`   | GET, PUT, DELETE  |
| Jogadores   | `/jogadores/`      | GET, POST         |
|             | `/jogadores/{id}/` | GET, PUT, DELETE  |
| Jogos       | `/jogos/`          | GET, POST         |
|             | `/jogos/{id}/`     | GET, PUT, DELETE  |

---

## 🔄 Serializers

Serializers convert models to JSON and validate received data.

Include read-only fields to facilitate API consumption:
- `equipa_casa_nome`
- `equipa_visitante_nome`
- `liga_nome`

---

## ⚙️ Installation and Execution

### Prerequisites
- Python 3.10+
- pip

### Steps

Clone the repository:
```bash
git clone https://github.com/Afons19/LigasApi-Backend.git
```

Access the directory:
```bash
cd backend
```

Create virtual environment:
```bash
python -m venv venv
```

Activate virtual environment:

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run migrations:
```bash
python manage.py migrate
```

Create superuser (optional):
```bash
python manage.py createsuperuser
```

Start server:
```bash
python manage.py runserver
```

API available at:
```
http://127.0.0.1:8000/api/
```

---

## ✅ Requirements Met

* Functional REST API
* Full CRUD for all entities
* Clear relationships between models
* Code organized by responsibility
* SQLite database

---

## 🎓 Academic Project

This project was developed for academic purposes within the web development course unit, following best practices for organization, modularity, and frontend-backend integration.

---

## 🤝 Contribution

Feel free to contribute with improvements by opening an issue or submitting a pull request.

---

## 📄 License

This project is licensed under the MIT License.