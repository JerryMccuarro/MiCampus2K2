import jsonpickle
import os.path

class JSONHelper:


    @staticmethod
    def CreaJSON(lista,nombre_archivo):
        datos = jsonpickle.dumps(lista)
        with open(nombre_archivo, "w") as archivo:
            archivo.write(datos)

    @staticmethod
    def LeerJSON(nombre_archivo):
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo) as archivo:
                json = archivo.read()
                lista = jsonpickle.decode(json)
            return  lista
