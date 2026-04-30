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
            salvar_preco(produto_id, preco, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

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
    historico = listar_historico()
    for h in historico:
        print(h)

if __name__ == "__main__":
    coletar_precos()
    mostrar_historico()
    analisar_precos()

import matplotlib.pyplot as plt
from database import buscar_historico_produto, listar_produtos

def gerar_grafico(produto_id, nome):
    historico = buscar_historico_produto(produto_id)

    datas = []
    precos = []

    for h in historico:
        precos.append(float(h[0]))
        datas.append(h[1])

    if len(precos) > 0:
        plt.figure()
        plt.plot(datas, precos, marker='o')
        plt.title(f"Histórico de Preços - {nome}")
        plt.xlabel("Data")
        plt.ylabel("Preço")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def mostrar_graficos():
    produtos = listar_produtos()

    for p in produtos:
        gerar_grafico(p[0], p[1])

if __name__ == "__main__":
    coletar_precos()
    analisar_precos()
    mostrar_graficos()