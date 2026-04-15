from pydantic import BaseModel

# representa os dados da API
# É o que entra e sai pela API. O Pydantic usa isso pra validar e serializar os dados. Você pode ter schemas diferentes para a mesma entidade. 

class Contato(BaseModel):
    nome : str
    numero : int
    email : str
    completed : bool = False