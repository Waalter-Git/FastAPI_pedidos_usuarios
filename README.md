# FastAPI Pedidos & Usuários

API REST desenvolvida com **FastAPI** para gerenciamento de usuários e pedidos.

---

## 📋 Conteúdo

- [Funcionalidades](#funcionalidades)  
- [Tecnologias](#tecnologias)  
- [Instalação](#instalação)  
- [Configuração](#configuração)  
- [Como usar](#como-usar)  
- [Estrutura do Projeto](#estrutura-do-projeto)  
- [Testes](#testes)  
- [Contribuição](#contribuição)  
- [Licença](#licença)  

---

## Funcionalidades

- Cadastro de usuários  
- Autenticação (login / logout)  
- Criação, leitura, atualização e deleção de pedidos (CRUD)  
- Relacionamento entre usuários e pedidos  
- Validações de dados via schemas  

---

## Tecnologias

- Python  
- FastAPI  
- SQLAlchemy / banco SQLite (aparentemente `banco.db`)  
- Alembic para migrações  
- Pydantic (para schemas / validações)  

---

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Waalter-Git/FastAPI_pedidos_usuarios.git
   cd FastAPI_pedidos_usuarios
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate   # no Linux/macOS
   venv\Scripts\activate      # no Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

   *Obs.: Se não houver `requirements.txt`, instale manualmente: `fastapi`, `uvicorn`, `sqlalchemy`, `alembic`, etc.*

---

## Configuração

- Verifique o arquivo `.env` se existir, para definir variáveis como URL do banco, settings da aplicação, etc.  
- Alembic: configure `alembic.ini` para apontar para o banco certo e gerar migrações se necessário.  

---

## Como usar

1. Inicie a aplicação:

   ```bash
   uvicorn main:app --reload
   ```

   Isso iniciará o server em modo de desenvolvimento (hot-reload).

2. Acesse a documentação interativa no navegador:

   ```
   http://127.0.0.1:8000/docs
   ```

3. Rotas principais:

   - `/auth` — endpoints de autenticação  
   - `/usuarios` — endpoints para usuários  
   - `/pedidos` — endpoints para pedidos  

   *(Ajuste os caminhos conforme definidos no código: `auth_routes.py`, `order_routes.py` etc.)*

---

## Estrutura do Projeto

```
FastAPI_pedidos_usuarios/
├── alembic/              # migrações do banco
├── .env                  # configurações de ambiente
├── alembic.ini
├── banco.db              # banco SQLite (arquivo local)
├── main.py               # ponto de entrada da aplicação
├── models.py             # definição dos modelos ORM
├── schemas.py            # schemas / validações com Pydantic
├── auth_routes.py        # rotas de autenticação
├── order_routes.py       # rotas de pedidos
├── dependencies.py       # dependências usadas nas rotas (ex: sessão de banco, autenticação)
├── venv/                 # ambiente virtual
└── README.md             # este arquivo
```

---

## Testes

*Até o momento não há testes automatizados incluídos.*  
Você pode adicionar testes com **pytest** ou outra ferramenta de sua escolha.  

---

## Contribuição

Contribuições são bem-vindas! Se quiser implementar algo ou corrigir, siga estes passos:

1. Fork deste repositório  
2. Crie uma branch para sua feature ou correção (`git checkout -b minha-feature`)  
3. Faça commits claros e atômicos  
4. Abra um Pull Request descrevendo o que foi feito  

---

## Licença

Este projeto está sob uma licença a definir — caso não exista um arquivo LICENSE, é bom adicionar um para deixar claro os termos de uso e compartilhamento.
