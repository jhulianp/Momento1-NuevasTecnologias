from datetime import datetime

def registrar_gasto(lista_gastos):
    print("--- Nuevo Registro ---")
    nombre = input("Nombre del gasto: ")
    desc = input("Descripcion breve: ")
    try:
        costo = float(input("Costo: "))
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Almacenamos el gasto como un diccionario
        nuevo_gasto = {
            "nombre": nombre,
            "descripcion": desc,
            "costo": costo,
            "fecha": fecha
        }
        lista_gastos.append(nuevo_gasto)
        print("Gasto registrado exitosamente.")
    except ValueError:
        print("Error: El costo debe ser un numero.")