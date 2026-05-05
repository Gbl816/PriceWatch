def analisar_precos(dados):
    return {}
import matplotlib.pyplot as plt
from database import listar_historico

def mostrar_grafico(produto_id):
    dados = listar_historico(produto_id)
    
    if not dados:
        print("Sem dados para gráfico")
        return
    
    precos = [d[0] for d in dados]
    datas = [d[1] for d in dados]
    
    plt.plot(datas, precos)
    plt.xticks(rotation=45)
    plt.title("Histórico de preços")
    plt.show()