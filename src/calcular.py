def total_gastos(lista_gastos):
    total = sum(g['costo'] for g in lista_gastos)
    print(f"\n================================")
    print(f"TOTAL GASTADO HORMIGA: ${total:.2f}")
    print(f"================================")