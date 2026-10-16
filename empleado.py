
from usuario import Usuario


class Empleado(Usuario):

    def __init__(self, idUsuario, email, passwordHash, rol,
                 nombre, direccion, telefono,
                 fechaInicioContrato, salario):

        super().__init__(idUsuario, email, passwordHash, rol)

        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__fechaInicioContrato = fechaInicioContrato
        self.__salario = salario

    def registrarHoras(self, horas):
        if isinstance(horas, (int, float)) and not isinstance(horas, bool):
            if 0 < horas <= 24:
                print(self.__nombre, "registró", horas, "horas")
                return True

        print("Error: debe ingresar entre 0 y 24 horas")
        return False

    def actualizarDatos(self, direccion, telefono):
        self.__direccion = direccion
        self.__telefono = telefono
        print("Datos del empleado actualizados")

    def mostrarDatos(self):
        print("Nombre:", self.__nombre)
        print("Dirección:", self.__direccion)
        print("Teléfono:", self.__telefono)
        print("Fecha de contrato:", self.__fechaInicioContrato)
