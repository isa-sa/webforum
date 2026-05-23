from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str

class PostCreate(BaseModel):
    titulo: str
    conteudo: str
    usuario_id: int


@app.get("/")
def raiz():
    return {"mensagem": "API conectada ao MySQL com sucesso!"}

@app.post("/usuarios")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
   
    novo_usuario = models.Usuario(nome=usuario.nome, email=usuario.email, senha_hash=usuario.senha)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@app.post("/posts")
def criar_post(post: PostCreate, db: Session = Depends(get_db)):
    novo_post = models.Post(titulo=post.titulo, conteudo=post.conteudo, usuario_id=post.usuario_id)
    db.add(novo_post)     
    db.commit()           
    db.refresh(novo_post) 
    return novo_post

@app.get("/posts")
def listar_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()