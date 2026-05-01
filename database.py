from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
DATABASE_URL = "sqlite:///./produtos.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} # Obrigatório para SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    """Uma session por requisição, fechada automaticamente."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
