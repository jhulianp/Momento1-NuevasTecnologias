def total_gastos(lista_gastos):
    total = sum(g['costo'] for g in lista_gastos)
    print(f"================================")
    print(f"el total de sus gastos: ${total:.2f}")
    print(f"================================")