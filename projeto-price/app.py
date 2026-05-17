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

from alerts import verificar_alerta

resultado = verificar_alerta(2500, 3000)
print(resultado)

from database import listar_produtos
from alerts import verificar_alerta

def testar_alertas():
    produtos = listar_produtos()

    for p in produtos:
        nome = p[1]
        preco_alvo = p[4]

        preco_atual = 2500

        resultado = verificar_alerta(preco_atual, preco_alvo)

        print(f"\nProduto: {nome}")
        print(f"Preço atual: R$ {preco_atual}")
        print(f"Preço alvo: R$ {preco_alvo}")
        print(resultado)

if __name__ == "__main__":
    testar_alertas()