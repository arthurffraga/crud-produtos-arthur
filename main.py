from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Produtos")

@app.get("/produtos", response_model=list[schemas.ProdutoResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar_produtos(db)

@app.get("/produtos/{produto_id}", response_model=schemas.ProdutoResponse)
def buscar(produto_id: int, db: Session = Depends(get_db)):
    p = crud.buscar_produto(db, produto_id)
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return p

@app.post("/produtos", response_model=schemas.ProdutoResponse, status_code=201)
def criar(dados: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.criar_produto(db, dados)

@app.put("/produtos/{produto_id}", response_model=schemas.ProdutoResponse)
def substituir(produto_id: int, dados: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    p = crud.substituir_produto(db, produto_id, dados)
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return p

@app.patch("/produtos/{produto_id}", response_model=schemas.ProdutoResponse)
def atualizar(produto_id: int, dados: schemas.ProdutoUpdate, db: Session = Depends(get_db)):
    p = crud.atualizar_produto(db, produto_id, dados)
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return p

@app.delete("/produtos/{produto_id}", status_code=204)
def deletar(produto_id: int, db: Session = Depends(get_db)):
    p = crud.deletar_produto(db, produto_id)
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return None
