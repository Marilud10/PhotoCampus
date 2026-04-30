
def editar(servicios):
    nombre = input("Nombre del servicio a editar: ")

    for s in servicios:
        if s["nombre"] == nombre:
            print("\n Editando servicio")

            s["nombre"] = input("Nuevo nombre: ")
            s["precio"] = input("Nuevo precio: ")
            s["tipo_evento"] = input("Nuevo tipo: ")
            s["duracion"] = input("Nueva duración: ")

            guardar(servicios)
            print("¡Servicio actualizado!")
            return

    print("-Servicio no encontrado-")