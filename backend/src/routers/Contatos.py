from fastapi import APIRouter
from src.schemas.Contatos import ContatoCreate

router = APIRouter(prefix="/Contatos", tags = ["Contatos"])

@router.post("/post")

def postContato():
    return {"message" : "post contato"}

router.post("/get")

def getContato():
    return {"message" : "conatatox"}

@router.post("/create")

def crateContato(contato : ContatoCreate):
    return {"message" : "Novo contato criado"}

@router.post("/update")

def UpdateContato():
    return {"message" : "update contato"}

@router.post("/delete")

def deleteContato():
    return {"message" : "delete contato"}

@router.post("/post")

def postContato():
    return {"message" : "post contato"}