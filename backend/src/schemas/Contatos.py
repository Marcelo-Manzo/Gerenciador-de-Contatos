from pydantic import BaseModel

class ContatoCreate(BaseModel):
    nome : str
    numero : int
    email : str
    completed : bool = False