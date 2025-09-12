from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import PedidoSchema
from models import Pedido
order_router = APIRouter(prefix="/orders", tags=["orders"])


@order_router.get("/")
async def pedidos():
    return {"message": "Acesso Lista de pedidos"}


@order_router.post("/pedidos")
async def criar_pedido(pedido_shema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usiario=PedidoSchema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {"message": "Pedido criado com sucesso", "pedido": novo_pedido.id}
