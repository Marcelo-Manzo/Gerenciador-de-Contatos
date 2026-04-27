from pydantic import BaseModel

# representa os dados da API
# É o que entra e sai pela API. O Pydantic usa isso pra validar e serializar os dados. Você pode ter schemas diferentes para a mesma entidade. 

# O que o usuário manda pra criar (sem id)
class Contato(BaseModel):
    nome : str
    numero : str
    email : str
    completed : bool = False

# O que a API retorna (com id)
class ContatoResponse(BaseModel):
    id: int
    nome: str
    numero: str
    email: str
    completed: bool

    class Config:
        from_attributes = True
        # diz ao Pydantic que ele pode converter um objeto SQLAlchemy diretamente pra esse schema — sem isso ele não consegue serializar o model do banco.