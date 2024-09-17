def obter_lista_produtos():
    produtos = []
    while True:
        print("===============================================================")
        produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
        if produto.lower() == 'sair':
            break
        produtos.append(produto)
    return produtos