
from empleado import Empleado


class Departamento:

    def __init__(self, idDepartamento, nombre, gerente):
        self.__idDepartamento = idDepartamento
        self.__nombre = nombre
        self.__gerente = gerente
        self.__empleados = []

    def agregarEmpleado(self, empleado):
        if not isinstance(empleado, Empleado):
            print("Error: debe ingresar un empleado válido")
            return

        if empleado not in self.__empleados:
            self.__empleados.append(empleado)
            print("Empleado agregado al departamento")
        else:
            print("El empleado ya pertenece al departamento")

    def removerEmpleado(self, empleado):
        if empleado in self.__empleados:
            self.__empleados.remove(empleado)
            print("Empleado removido del departamento")
        else:
            print("El empleado no pertenece al departamento")

    def listarPersonal(self):
        print("Departamento:", self.__nombre)
        print("Gerente:", self.__gerente)
        print("Cantidad de empleados:", len(self.__empleados))

        for empleado in self.__empleados:
            empleado.mostrarDatos()
            print("--------------------")
