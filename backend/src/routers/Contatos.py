from fastapi import APIRouter, Depends
# o session instancia a conexão com o banco e o sqlarchemi traduz os comandos do python para sql


from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.Contatos import Contato
from src.models import Contatos as model

router = APIRouter(prefix="/Contatos", tags=["Contatos"])


# . O ORM (Object Relational Mapper) traduz código Python para SQL automaticamente. Você escreve Python, ele escreve o SQL por baixo:


# Sem Depends — trabalhoso e perigoso(ele pode não encerrar após dar algum erro)

@router.get("/")
def get_contatos(db: Session = Depends(get_db)):
    contatos = db.query(model.Contato).all()
    return contatos
# ## Você escreve isso:
# db.query(model.Contato).all()

# # O SQLAlchemy executa isso:
# SELECT * FROM contatos;

#esse {id} é a forma de receber o id pela rota
@router.get("/{id}")
def get_contato(id: int, db: Session = Depends(get_db)):
            # busca(Contato(modelo))    filtra pelo id           pega o primeiro
    contato = db.query(model.Contato).filter(model.Contato.id == id).first()
    return contato
# # Você escreve isso:
# db.query(model.Contato).filter(model.Contato.id == id).first()

# # O SQLAlchemy executa isso:
# SELECT * FROM contatos WHERE id = 1 LIMIT 1;


@router.post("/")
def create_contato(contato: Contato, db: Session = Depends(get_db)):
    novo = model.Contato(**contato.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
# # Você escreve isso:
# db.add(novo)
# db.commit()

# # O SQLAlchemy executa isso:
# INSERT INTO contatos (nome, numero, email, completed) VALUES (...);

@router.put("/{id}")
def update_contato(id: int, contato: Contato, db: Session = Depends(get_db)):
    existente = db.query(model.Contato).filter(model.Contato.id == id).first()
    existente.nome = contato.nome
    existente.numero = contato.numero
    existente.email = contato.email
    existente.completed = contato.completed
    db.commit()
    db.refresh(existente)
    return existente

@router.delete("/{id}")
def delete_contato(id: int, contato : Contato, db: Session = Depends(get_db)):
    contato = db.query(model.Contato).filter(model.Contato.id == id).first()
    db.delete(contato)
    if contato is None:
        raise HTTPException(status_code=404, detail=f"Contato {id} não encontrado")
    #perguntar pq eu dou um commit no final de cada metodo
    # Duas ótimas perguntas!

# 1. Por que dar db.commit() no final?
# A Session do SQLAlchemy funciona como um "rascunho". Tudo que você faz fica em memória até o commit — só aí vai pro banco de verdade:
# pythondb.delete(contato)  # ← marca pra deletar (só em memória)
# db.commit()         # ← executa no banco de verdade

    db.commit()
    return {"message": f"contato {id} deletado"}



# Por que toda função recebe db: Session = Depends(get_db)?
# São dois conceitos juntos:
# Session é a conexão com o banco. Pensa nela como um "contexto" — tudo que você faz no banco dentro de uma requisição passa por ela. É ela que executa as queries, guarda as mudanças e faz o commit.
# Depends(get_db) é o sistema de injeção de dependência do FastAPI. Lembra do get_db que criamos no database.py?
# pythondef get_db():
#     db = SessionLocal()
#     try:
#         yield db        # ← entrega a conexão pra rota
#     finally:
#         db.close()      # ← fecha a conexão ao terminar
# O Depends faz o FastAPI chamar o get_db automaticamente antes de executar a rota, e fechar a conexão depois. Sem isso você teria que fazer isso manualmente em cada rota:
# python# Sem Depends — trabalhoso e perigoso
# @router.get("/")
# def get_contatos():
#     db = SessionLocal()     # abre manualmente
#     contatos = db.query(model.Contato).all()
#     db.close()              # e se der erro antes disso? conexão fica aberta!
#     return contatos

# # Com Depends — o FastAPI gerencia tudo
# @router.get("/")
# def get_contatos(db: Session = Depends(get_db)):
#     return db.query(model.Contato).all()
# O Depends garante que a conexão sempre fecha, mesmo se der erro no meio da requisição.
