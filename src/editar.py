import listar

def menu_edicion(lista_gastos):
    while True:
        print("--- Menú de Edición ---")
        print("a. Ver gastos registrados")
        print("b. Editar nombre, descripción o costo")
        print("c. Eliminar un gasto")
        print("d. Volver al menú principal")
        
        sub_opcion = input("Seleccione una opción: ").lower()

        if sub_opcion == "a":
            listar.mostrar_gastos(lista_gastos)
        elif sub_opcion == "b":
            editar_detalles(lista_gastos)
        elif sub_opcion == "c":
            eliminar_gasto(lista_gastos)
        elif sub_opcion == "d":
            break

def editar_detalles(lista_gastos):
    nombre_buscar = input("Nombre del gasto que desea editar: ")
    for g in lista_gastos:
        if g['nombre'].lower() == nombre_buscar.lower():
            g['nombre'] = input(f"Nuevo nombre ({g['nombre']}): ") or g['nombre']
            g['descripcion'] = input(f"Nueva descripción ({g['descripcion']}): ") or g['descripcion']
            nuevo_costo = input(f"Nuevo costo ({g['costo']}): ")
            if nuevo_costo: g['costo'] = float(nuevo_costo)
            print("Gasto actualizado.")
            return
    print("No se encontró ese gasto.")

def eliminar_gasto(lista_gastos):
    nombre_buscar = input("Ingrese el nombre EXACTO del gasto que desea eliminar: ")
    for i, g in enumerate(lista_gastos):
        if g['nombre'] == nombre_buscar: # Validación de seguridad estricta
            confirmacion = input(f"Para confirmar, escriba de nuevo el nombre '{g['nombre']}': ")
            if confirmacion == g['nombre']:
                lista_gastos.pop(i)
                print("Gasto eliminado con éxito.")
                return
            else:
                print("Los nombres no coinciden. Operación cancelada.")
                return
    print("No se encontró un gasto con ese nombre exacto.")