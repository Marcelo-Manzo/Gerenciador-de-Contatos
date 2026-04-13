from fastapi import APIRouter
from src.schemas.Contatos import Contato

router = APIRouter(prefix="/Contatos", tags = ["Contatos"])

@router.post("/post")

def postContato(contato : Contato):
    return {"message" : "post contato"}

router.post("/get")

def getContato(contato : Contato):
    return {"message" : "conatatox"}

@router.post("/create")

def crateContato(contato : Contato):
    return {"message" : "Novo contato criado"}

@router.post("/update")

def UpdateContato(contato : Contato):
    return {"message" : "update contato"}

@router.post("/delete")

def deleteContato(contato : Contato):
    return {"message" : "delete contato"}

@router.post("/post")

def postContato(contato : Contato):
    return {"message" : "post contato"}