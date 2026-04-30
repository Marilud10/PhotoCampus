def eliminar(servicios):
    nombre = input("Nombre del servicio a eliminar: ")

    for s in servicios:
        if s["nombre"] == nombre:
            servicios.remove(s)
            guardar(servicios)
            print("Servicio eliminado")
            return

    print("-Servicio no encontrado-")