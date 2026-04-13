from sqlalchemy import Column, Integer, String, Boolean
from src.database import Base

class Contato(Base):
    __tablename__ = "contatos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    numero = Column(Integer, nullable=False)
    email = Column(String(100), nullable=False)
    completed = Column(Boolean, default=False)