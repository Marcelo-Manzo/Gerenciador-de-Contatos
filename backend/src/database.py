from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()  # ← abre a conexão
    try:
        yield db         # ← entrega pra rota usar
    finally:
        db.close()       # ← fecha ao terminar


# Tecnicamente o SessionLocal() não abre uma conexão direta com o banco imediatamente — ele cria uma Session, que é um objeto que gerencia a conversa com o banco. A conexão física só acontece quando você executa a primeira query, tipo db.query(...).
# É uma distinção sutil mas importante:
# SessionLocal() → cria a Session (objeto de gerenciamento)
# db.query()     → aí sim abre a conexão física com o banco
# db.commit()    → confirma as mudanças
# db.close()     → encerra tudo
# O yield no meio é o que torna o get_db um gerador — ele pausa ali, entrega o db pra rota usar, e só continua pro finally depois que a rota terminar. Por isso o Depends funciona tão bem com ele — o FastAPI controla esse ciclo de vida automaticamente.
