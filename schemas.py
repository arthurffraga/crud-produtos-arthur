from pydantic import BaseModel, ConfigDict
from typing import Optional
class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    categoria: str
    quantidade: int

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    preco: Optional[float] = None
    categoria: Optional[str] = None
    quantidade: Optional[int] = None

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    categoria: str
    quantidade: int
    model_config = ConfigDict(from_attributes=True)
