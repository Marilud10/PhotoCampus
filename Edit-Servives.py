
def buscar_servicio(servicios, id_buscar):
    for servicio in servicios:
        if servicio["id"] == id_buscar:
            return servicio
    return None


def editar_servicio(servicios):
    id_editar = int(input("ID del servicio a editar: "))
    servicio = buscar_servicio(servicios, id_editar)

    if servicio:
        servicio["nombre"] = input("Nuevo nombre: ")
        servicio["precio"] = float(input("Nuevo precio: "))
        servicio["tipo_evento"] = input("Nuevo tipo: ")
        servicio["duracion"] = int(input("Nueva duración: "))
        print("✏️ Servicio actualizado")
    else:
        print("Servicio no encontrado")