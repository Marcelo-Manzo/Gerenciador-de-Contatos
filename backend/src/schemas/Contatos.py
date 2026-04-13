from pydantic import BaseModel

class Contato(BaseModel):
    id: int
    nome : str
    numero : int
    email : str
    completed : bool = False