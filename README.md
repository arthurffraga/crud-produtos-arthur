# API de Catálogo de Produtos

Arthur Fraga

## Como instalar e rodar localmente

1. Crie um ambiente virtual e o ative:
   `python -m venv venv`
   `source venv/bin/activate` (no Linux/Mac) ou `venv\Scripts\activate` (no Windows)

2. Instale as dependências:
   `pip install fastapi[all] sqlalchemy pydantic`

3. Inicie o servidor:
   `uvicorn main:app --reload`

4. Acesse a documentação Swagger UI para testar as rotas em: `http://localhost:8000/docs`

## Justificativa das Decisões

* **Estrutura de arquivos:** Optei por utilizar módulos separados (main.py, crud.py, schemas.py, models.py, database.py) pois cada arquivo passa a ter uma responsabilidade única, nenhum arquivo faz tudo.
* **Memória vs Banco de Dados:** Utilizei o SQLite para a persistência dos dados no disco. Isso garante que os dados de produtos e estoque não sumam caso o servidor seja reiniciado.
* **Campos Obrigatórios e Opcionais:** Na criação (POST) e substituição (PUT), utilizamos o schema `ProdutoCreate`, tornando `nome`, `preco`, `categoria` e `quantidade` campos 100% obrigatórios. Na atualização parcial (PATCH), definimos todos os atributos como opcionais usando o tipo `Optional` do Pydantic para processar apenas as alterações enviadas.
* **Códigos de Status HTTP:** Adotei 200 OK como padrão de retorno para leitura/edição. Para criar utilizamos o código 201 (Created), e para deleção o código 204 (No Content), seguindo as boas práticas apresentadas.
* **Erros de "Produto não encontrado":** Quando uma requisição por `produto_id` falha em achar o registro no banco, lança imediatamente um `HTTPException` com status 404 (Not Found) detalhando que o recurso não existe na nossa tabela de produtos.
