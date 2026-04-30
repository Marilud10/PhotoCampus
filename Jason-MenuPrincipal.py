import json

ARCHIVO = "servicios.json"

def cargar():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except:
        return []

def guardar(servicios):
    with open(ARCHIVO, "w") as f:
        json.dump(servicios, f, indent=4)



def menu():
    servicios = cargar()

    while True:
        print("---------------------------------------")
        print("\n ---SISTEMA FOTOGRÁFICO---")
        print("1. Ver catálogo de servicios(Paquetes)")
        print("2. Buscar servicios por tipo de evento")
        print("3. Registrar nuevo servicio")
        print("4. Editar Paquete")
        print("5. Eliminar servicio")
        print("6. Salir")
        print("---------------------------------------")


        op = input("Seleccione una opción: ")

        if op == "1":
            mostrar(servicios)
        elif op == "2":
            buscar_por_tipo(servicios)
        elif op == "3":
            agregar(servicios)
        elif op == "4":
            editar(servicios)
        elif op == "5":
            eliminar(servicios)
        elif op == "6":
            print("Saliendo del sistema")
            break
        else:
            print("Opción inválida")

menu()