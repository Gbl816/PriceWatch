from database import listar_produtos, salvar_preco, listar_historico
from scraper import pegar_preco
from datetime import datetime

def coletar_precos():
    produtos = listar_produtos()

    for p in produtos:
        produto_id = p[0]
        url = p[2]

        preco = pegar_preco(url)

        if preco:
            salvar_preco(produto_id, preco, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def mostrar_historico():
    historico = listar_historico()
    for h in historico:
        print(h)

if __name__ == "__main__":
    coletar_precos()
    mostrar_historico()
    from database import cadastrar_produto