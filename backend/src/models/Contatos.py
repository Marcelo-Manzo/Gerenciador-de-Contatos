from sqlalchemy import Column, Integer, String, Boolean
from src.database import Base

# representa o banco de dados
# É a estrutura da tabela no banco. O SQLAlchemy usa isso pra criar e manipular as linhas do banco. É o "espelho" da sua tabela SQL. 

class Contato(Base):
    __tablename__ = "contatos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    numero = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    completed = Column(Boolean, default=False)