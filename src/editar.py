import listar

def menu_edicion(lista_gastos):
    while True:
        print("--- Menu de Edicion ---")
        print("1. Ver gastos registrados")
        print("2. Editar nombre, descripcion o costo")
        print("3. Eliminar un gasto")
        print("4. Volver al menú principal")
        
        sub_opcion = input("Seleccione una opcion: ").lower()

        if sub_opcion == "1":
            listar.mostrar_gastos(lista_gastos)
        elif sub_opcion == "2":
            editar_detalles(lista_gastos)
        elif sub_opcion == "3":
            eliminar_gasto(lista_gastos)
        elif sub_opcion == "4":
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
    print("No se encontro ese gasto.")

def eliminar_gasto(lista_gastos):
    nombre_buscar = input("Ingrese el nombre exacto del gasto que desea eliminar: ")
    for i, g in enumerate(lista_gastos):
        if g['nombre'] == nombre_buscar: # Validación de seguridad estricta
            confirmacion = input(f"Para confirmar, escriba de nuevo el nombre '{g['nombre']}': ")
            if confirmacion == g['nombre']:
                lista_gastos.pop(i)
                print("Gasto eliminado con exito.")
                return
            else:
                print("Los nombres no coinciden. Operacion cancelada.")
                return
    print("No se encontró un gasto con ese nombre exacto.")