def eliminar_servicio(servicios):
    id_eliminar = int(input("ID del servicio a eliminar: "))

    for servicio in servicios:
        if servicio["id"] == id_eliminar:
            servicios.remove(servicio)
            print(" Servicio eliminado")
            return

    print("Servicio no encontrado")