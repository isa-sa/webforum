from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    
    nome = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    senha_hash = Column(String(255))

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(150), index=True)
    conteudo = Column(Text) 
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))