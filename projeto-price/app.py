from database import listar_produtos, salvar_preco, listar_historico, buscar_historico_produto
from scraper import pegar_preco
from datetime import datetime

def coletar_precos():
    produtos = listar_produtos()

    for p in produtos:
        produto_id = p[0]
        url = p[2]

        preco = pegar_preco(url)

        if preco:
            salvar_preco(produto_id, preco)

def analisar_precos():
    produtos = listar_produtos()

    for p in produtos:
        produto_id = p[0]
        nome = p[1]

        historico = buscar_historico_produto(produto_id)

        if len(historico) >= 2:
            preco_antigo = historico[-2][0]
            preco_atual = historico[-1][0]

            if preco_atual > preco_antigo:
                print(f"{nome}: preço subiu")
            elif preco_atual < preco_antigo:
                print(f"{nome}: preço caiu")
            else:
                print(f"{nome}: preço estável")

def mostrar_historico():
    produtos = listar_produtos()
    for p in produtos:
        produto_id = p[0]
        nome = p[1]
        historico = listar_historico(produto_id)
        print(f"Histórico para {nome}:")
        for h in historico:
            print(f"  {h}")

if __name__ == "__main__":
    coletar_precos()
    mostrar_historico()
    analisar_precos()

