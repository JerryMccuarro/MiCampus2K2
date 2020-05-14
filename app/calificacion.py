class Calificacion(object):
    def __init__(self, nombre, apellido, matricula,materia,calificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.materia = materia
        self.calificacion = calificacion


class ListaDeCalificaciones(list):

    def append(self, __object):
        assert  type(__object) is Calificacion, "Solo puedes agregar calificaciones"
        super().append(__object)

    def extend(self, __iterable):
        for __object in __iterable:
            assert type(__object) is Calificacion, "Solo puedes agregar calificaciones"
        super().extend(__iterable)

    def insert(self, __index: int, __object):
        assert type(__object) is Calificacion, "Solo puedes agregar calificaciones"
        super().insert(__index,__object)

