from fastapi import APIRouter

router = APIRouter(prefix="/Contatos", tags = ["Contatos"])

@router.post("/crate-Contato")

def crateContato():
    return {"mensage" : "Novo contato criado"}