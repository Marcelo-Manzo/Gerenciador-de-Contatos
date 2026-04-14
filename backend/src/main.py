from fastapi import FastAPI
from .routers import Contatos
from .database import engine, Base

Base.metadata.create_all(bind=engine)
# Isso faz o SQLAlchemy olhar todos os models que você criou e criar as tabelas no banco automaticamente se elas ainda não existirem. É equivalente a rodar o CREATE TABLE no SQL Server manualmente — mas automático toda vez que o servidor inicia.

app = FastAPI()

@app.get("/")
def root():
    return {"status": "backend is running"}

app.include_router(Contatos.router)