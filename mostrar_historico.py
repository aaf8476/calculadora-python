def mostrar_historico(historico):
    if historico:
        print("Histórico de operações:")
        for operacao in historico:
            print(operacao)
    else:
        print("Nenhuma operação realizada ainda.")