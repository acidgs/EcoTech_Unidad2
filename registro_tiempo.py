
from empleado import Empleado
from proyecto import Proyecto


class RegistroTiempo:

    def __init__(self, idRegistro, fecha, cantidadHoras,
                 descripcionTareas, empleado, proyecto):

        self.__idRegistro = idRegistro
        self.__fecha = fecha
        self.__cantidadHoras = cantidadHoras
        self.__descripcionTareas = descripcionTareas
        self.__empleado = empleado
        self.__proyecto = proyecto

    def validarHoras(self):
        return (
            isinstance(self.__cantidadHoras, (int, float))
            and not isinstance(self.__cantidadHoras, bool)
            and 0 < self.__cantidadHoras <= 24
        )

    def crearRegistro(self):

        if not isinstance(self.__empleado, Empleado):
            print("Error: empleado no válido")
            return False

        if not isinstance(self.__proyecto, Proyecto):
            print("Error: proyecto no válido")
            return False

        if not self.validarHoras():
            print("Error: las horas deben estar entre 0 y 24")
            return False

        if not self.__proyecto.tieneEmpleado(self.__empleado):
            print("Error: empleado no asignado al proyecto")
            return False

        print("Registro de tiempo creado correctamente")
        return True

    def mostrarRegistro(self):
        print("ID Registro:", self.__idRegistro)
        print("Fecha:", self.__fecha)
        print("Horas trabajadas:", self.__cantidadHoras)
        print("Descripción:", self.__descripcionTareas)
