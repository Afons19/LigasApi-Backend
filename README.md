# Documentação do Backend
---

# LigasAPI-Backend
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

Crie o ambiente virtual:
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

Este projeto foi desenvolvido para fins académicos.

---

## 🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias abrindo um problema ou enviando um pull request.

---

## 📄 Licença

Este projeto é licenciado sob a Licença MIT.
