from pydantic import BaseModel

class Contato(BaseModel):
    nome : str
    numero : int
    email : str
    completed : bool = False