stock = {}

while True:
    item = input("Nome do item para adicionar (ou 'x' para encerrar): ").strip().lower()
    if item == "x":  # comparar com string 'x'
        break
    
    try:
        quantidade = int(input("Adicione o número de produtos: "))
    except ValueError:
        print("Digite apenas números válidos!")
        continue

    # Atualiza o estoque
    if item in stock:
        stock[item] += quantidade
    else:
        stock[item] = quantidade
    
    # Exibe tabela
    print("\nEstoque Atual:")
    print(f"{'Item':<15} {'Quantidade':<10}")
    print("-" * 25)
    for k, v in stock.items():
        print(f"{k:<15} {v:<10}")
    print("\n")
