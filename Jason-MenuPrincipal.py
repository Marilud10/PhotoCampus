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
        