from sqlalchemy import create_engine, Column , String, Integer, Boolean, Float , ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType
#cria  a conexão do seu banco
db = create_engine("sqlite:///banco.db")

#cria a base do banco de dados

Base = declarative_base()

#criar as classes/tabelas do banco
#usuário
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


#pedidos

class Pedido(Base):
    __tablename__ = "pedidos"

    # STATUS_PEDIDOS =(
    #     ("PENDENTE", "Pendente"),
    #     ("CANCELADO", "Cancelado"),
    #     ("FINALIZADO", "Finalizado"),
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    usuario = Column("usuario", Integer, ForeignKey("usuarios.id"), nullable=False)
    preco = Column("preco", Float, nullable=False)

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.status = status
        self.usuario = usuario
        self.preco = preco


#ItensPedido
class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer, nullable=False)
    sabor = Column("sabor", String, nullable=False)
    tamanho = Column("tamanho", String, nullable=False)
    preco_unitario = Column("preco_unitario", Float, nullable=False)
    pedido = Column("pedido", Integer, ForeignKey("pedidos.id"), nullable=False)

    def __init__(self, pedido, sabor, tamanho, preco_unitario , quantidade):
        self.pedido = pedido
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

#executa a criação dos metadados do seu banco (cria ao banco de fato)


