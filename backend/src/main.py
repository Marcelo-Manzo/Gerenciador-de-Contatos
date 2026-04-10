from fastapi import FastAPI
from .routers import Contatos


app = FastAPI()

@app.get("/")
def root():
    return {"status" : "backend is running"}

app.include_router(Contatos.router)