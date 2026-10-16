
from empleado import Empleado


class Proyecto:

    def __init__(self, idProyecto, nombre, descripcion, fechaInicio):
        self.__idProyecto = idProyecto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fechaInicio = fechaInicio
        self.__empleados = []

    def asignarEmpleado(self, empleado):
        if not isinstance(empleado, Empleado):
            print("Error: debe ingresar un empleado válido")
            return

        if empleado not in self.__empleados:
            self.__empleados.append(empleado)
            print("Empleado asignado al proyecto")
        else:
            print("El empleado ya está asignado")

    def desasignarEmpleado(self, empleado):
        if empleado in self.__empleados:
            self.__empleados.remove(empleado)
            print("Empleado desasignado del proyecto")
        else:
            print("El empleado no pertenece al proyecto")

    def listarEmpleados(self):
        print("Proyecto:", self.__nombre)
        print("Descripción:", self.__descripcion)
        print("Fecha de inicio:", self.__fechaInicio)
        print("Cantidad de empleados:", len(self.__empleados))

        for empleado in self.__empleados:
            empleado.mostrarDatos()
            print("--------------------")

    def tieneEmpleado(self, empleado):
        return empleado in self.__empleados
