
def menu_principal():
    # Lista de diccionarios para almacenar los gastos
    gastos = []
    
    while True:
        print("--- CONTROL DE GASTOS HORMIGA ---")
        print("1. Registrar gasto")
        print("2. Gastos registrados (Mayor a menor)")
        print("3. Editar/Eliminar gastos")
        print("4. Calcular total")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar.registrar_gasto(gastos)
        elif opcion == "2":
            listar.mostrar_gastos(gastos)
        elif opcion == "3":
            editar.menu_edicion(gastos)
        elif opcion == "4":
            calcular.total_gastos(gastos)
        elif opcion == "5":
            print("La aplicacion se cerro con exito")
            break
        else:
            print("Opcion no valida.")
