import json

def cargar_datos():
    try:
        with open("servicios.json", "r") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_datos(servicios):
    with open("servicios.json", "w") as archivo:
        json.dump(servicios, archivo, indent=4)

def mostrar_servicios(servicios):
    for s in servicios:
        print(s)


def menu():
    servicios = cargar_datos()

    while True:
        print("\n1. Ver servicios")
        print("2. Agregar servicio")
        print("3. Editar servicio")
        print("4. Eliminar servicio")
        print("5. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            mostrar_servicios(servicios)
        elif opcion == "2":
            agregar_servicio(servicios)
        elif opcion == "3":
            editar_servicio(servicios)
        elif opcion == "4":
            eliminar_servicio(servicios)
        elif opcion == "5":
            guardar_datos(servicios)
            break
        else:
            print("Opción inválida")