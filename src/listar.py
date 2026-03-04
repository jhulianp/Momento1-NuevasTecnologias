def mostrar_gastos(lista_gastos):
    if not lista_gastos:
        print("No hay gastos registrados.")
        return

    # Ordenar de mayor a menor costo
    gastos_ordenados = sorted(lista_gastos, key=lambda x: x['costo'], reverse=True)
    
    print("--- Gastos Registrados ---")
    for g in gastos_ordenados:
        print(f"Nombre: {g['nombre']} | Desc: {g['descripcion']} | Costo: ${g['costo']} | Fecha: {g['fecha']}")