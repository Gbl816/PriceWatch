from database import cadastrar_produto, listar_produtos

cadastrar_produto("Notebook Dell", "https://example.com", "Site A", 3000)

produtos = listar_produtos()

for p in produtos:
    print(p)