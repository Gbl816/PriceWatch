def verificar_alerta(preco_atual, preco_alvo):
    if preco_atual <= preco_alvo:
        return "ALERTA: preço abaixo do valor desejado!"
    
    return "Preço ainda acima do alvo."