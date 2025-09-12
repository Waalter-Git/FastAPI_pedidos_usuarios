from fastapi import APIRouter , Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema , LoginSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])


def criar_token(email):
    token = f'aysfgiayffsa{email}'
    return token

def autenticar_usuario(email: str, senha: str, session: Session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if not usuario:
        return False
    if not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario

@auth_router.get("/")
async def home():
    return {"message": "Acesso à página inicial de autenticação", "autenticado": False}


@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session:Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    
    if usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(nome=usuario_schema.nome, email=usuario_schema.email, senha=senha_criptografada , ativo=usuario_schema.ativo, admin=usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"message": f"Conta criada com sucesso {usuario_schema.email}"}
    

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session:Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(LoginSchema.email, LoginSchema.senha, session)
    
    if not usuario:
        raise HTTPException(status_code=400, detail="usuario não cadastrado ou credenciais inválidas")
    else:
        acess_token = criar_token(login_schema.email)
        return{
            "access_token": acess_token,
            "token_type": "Bearer"
            }


