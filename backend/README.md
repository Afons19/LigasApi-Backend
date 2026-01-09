```markdown
# 📘 Sistema de Gestão de Ligas Desportivas (Futebol)
**API REST + Frontend Web**  
**Ano letivo: 2025/2026**

---

## 📌 Descrição do Projeto

Este projeto consiste no desenvolvimento de um **sistema completo de gestão de ligas desportivas**, focado no futebol, composto por:

- **Backend**: API REST desenvolvida em Django REST Framework  
- **Frontend**: Aplicação web desenvolvida em Vue.js  

O sistema permite gerir **ligas, equipas, jogadores e jogos**, com relacionamentos claros entre as entidades e operações CRUD completas.

---

## 🛠️ Tecnologias Utilizadas

### Backend
- Python 3
- Django
- Django REST Framework
- SQLite
- CORS Headers

### Frontend
- Vue.js 3
- Vite
- Vue Router
- Axios
- CSS puro

---

## 🧱 Arquitetura Geral

A aplicação segue uma arquitetura **cliente-servidor**:

```

Frontend (Vue.js) → API REST → Base de Dados (SQLite)

```

- O backend fornece dados via endpoints REST
- O frontend consome a API e apresenta a informação ao utilizador

---

## 📂 Estrutura do Projeto

### Backend

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
└── liga_api/
├── models.py
├── serializer.py
├── views.py
├── urls.py
└── admin.py

```

---

### Frontend

```

frontend/
└── src/
├── assets/
│   └── style.css
│
├── componentes/
│   ├── Navbar.vue
│   ├── StatCard.vue
│   └── LigaCard.vue
│
├── router/
│   └── router.js
│
├── services/
│   └── api.js
│
└── views/
├── Home.vue
├── Gerenciar.vue
├── LigaDetalhe.vue
├── EquipaDetalhe.vue
└── JogadorDetalhe.vue

```

---

## 📊 Modelos de Dados (Backend)

### Liga
- nome
- país
- época

Relacionamentos:
- 1 Liga → N Equipas
- 1 Liga → N Jogos

---

### Equipa
- nome
- cidade
- treinador
- ano_fundacao
- liga (FK)

Relacionamentos:
- 1 Equipa → N Jogadores
- 1 Equipa → N Jogos

---

### Jogador
- nome
- posição
- número
- idade
- equipa (FK)

---

### Jogo
- data
- golos_casa
- golos_fora
- liga (FK)
- equipa_casa (FK)
- equipa_visitante (FK)

---

## 🌐 Endpoints da API

**Base URL**
```

[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

````

| Entidade   | Endpoint           | Métodos              |
|-----------|--------------------|----------------------|
| Ligas     | `/ligas/`          | GET, POST            |
|           | `/ligas/{id}/`     | GET, PUT, DELETE     |
| Equipas   | `/equipas/`        | GET, POST            |
|           | `/equipas/{id}/`   | GET, PUT, DELETE     |
| Jogadores | `/jogadores/`      | GET, POST            |
|           | `/jogadores/{id}/` | GET, PUT, DELETE     |
| Jogos     | `/jogos/`          | GET, POST            |
|           | `/jogos/{id}/`     | GET, PUT, DELETE     |

---

## 🖥️ Funcionalidades do Frontend

### Página Inicial (Home)
- Estatísticas globais (ligas, equipas, jogadores, jogos)
- Listagem de ligas com os respetivos jogos
- Listagem de equipas clicáveis

### Gerenciar
- CRUD completo de:
  - Ligas
  - Equipas
  - Jogadores
  - Jogos

### Detalhes
- **LigaDetalhe**: dados da liga + jogos
- **EquipaDetalhe**: dados da equipa + tabela de jogadores
- **JogadorDetalhe**: dados completos do jogador

---

## ⚙️ Instalação e Execução

### Pré-requisitos
- Python 3.10+
- pip
- Ambiente virtual

---

### Backend

```bash
cd backend
python -m venv venv
````

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

---

## ✅ Requisitos Cumpridos

* ✔ API REST funcional
* ✔ CRUD completo para todas as entidades
* ✔ Relacionamentos claros (1:N)
* ✔ Integração frontend ↔ backend
* ✔ Código organizado e legível
* ✔ Interface funcional e intuitiva