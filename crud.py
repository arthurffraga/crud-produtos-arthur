from sqlalchemy.orm import Session
import models, schemas

def listar_produtos(db: Session):
    return db.query(models.Produto).all()

def buscar_produto(db: Session, produto_id: int):
    return db.query(models.Produto).filter(models.Produto.id == produto_id).first()

def criar_produto(db: Session, dados: schemas.ProdutoCreate):
    produto = models.Produto(**dados.model_dump())
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto

def substituir_produto(db: Session, produto_id: int, dados: schemas.ProdutoCreate):
    p = buscar_produto(db, produto_id)
    if not p:
        return None
    p.nome = dados.nome
    p.preco = dados.preco
    p.categoria = dados.categoria
    p.quantidade = dados.quantidade
    db.commit()
    db.refresh(p)
    return p

def atualizar_produto(db: Session, produto_id: int, dados: schemas.ProdutoUpdate):
    p = buscar_produto(db, produto_id)
    if not p:
        return None
    atualizacoes = dados.model_dump(exclude_unset=True)
    for campo, valor in atualizacoes.items():
        setattr(p, campo, valor)
    
    db.commit()
    db.refresh(p)
    return p

def deletar_produto(db: Session, produto_id: int):
    p = buscar_produto(db, produto_id)
    if p:
        db.delete(p)
        db.commit()
    return p
