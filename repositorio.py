
from base_datos import BaseDatos


class EmpleadoRepositorio:

    def __init__(self):
        self.__bd = BaseDatos()

    def guardarEmpleado(self, idEmpleado, nombre, email):
        consulta = """
            INSERT OR IGNORE INTO empleados
            (idEmpleado, nombre, email)
            VALUES (?, ?, ?)
        """

        return self.__bd.ejecutarConsulta(
            consulta, (idEmpleado, nombre, email)
        )

    def listarEmpleados(self):
        consulta = """
            SELECT idEmpleado, nombre, email
            FROM empleados
        """

        return self.__bd.ejecutarConsulta(
            consulta, obtener=True
        )


class ProyectoRepositorio:

    def __init__(self):
        self.__bd = BaseDatos()

    def guardarProyecto(self, idProyecto, nombre, descripcion):
        consulta = """
            INSERT OR IGNORE INTO proyectos
            (idProyecto, nombre, descripcion)
            VALUES (?, ?, ?)
        """

        return self.__bd.ejecutarConsulta(
            consulta, (idProyecto, nombre, descripcion)
        )


class RegistroTiempoRepositorio:

    def __init__(self):
        self.__bd = BaseDatos()

    def guardarRegistro(self, idRegistro, fecha, cantidadHoras,
                        descripcionTareas, idEmpleado, idProyecto):

        consulta = """
            INSERT OR IGNORE INTO registros_tiempo
            (idRegistro, fecha, cantidadHoras,
             descripcionTareas, idEmpleado, idProyecto)
            VALUES (?, ?, ?, ?, ?, ?)
        """

        return self.__bd.ejecutarConsulta(
            consulta,
            (
                idRegistro,
                fecha,
                cantidadHoras,
                descripcionTareas,
                idEmpleado,
                idProyecto
            )
        )

    def listarRegistros(self):
        consulta = """
            SELECT idRegistro, fecha, cantidadHoras,
                   descripcionTareas, idEmpleado, idProyecto
            FROM registros_tiempo
        """

        return self.__bd.ejecutarConsulta(
            consulta, obtener=True
        )


class DepartamentoRepositorio:

    def __init__(self):
        self.__bd = BaseDatos()

    def guardarDepartamento(self, idDepartamento, nombre, gerente):
        consulta = """
            INSERT OR IGNORE INTO departamentos
            (idDepartamento, nombre, gerente)
            VALUES (?, ?, ?)
        """

        return self.__bd.ejecutarConsulta(
            consulta, (idDepartamento, nombre, gerente)
        )


class EmpleadoDepartamentoRepositorio:

    def __init__(self):
        self.__bd = BaseDatos()

    def asignarEmpleadoDepartamento(self, idEmpleado, idDepartamento):
        consulta = """
            INSERT OR IGNORE INTO empleados_departamentos
            (idEmpleado, idDepartamento)
            VALUES (?, ?)
        """

        return self.__bd.ejecutarConsulta(
            consulta, (idEmpleado, idDepartamento)
        )

    def listarPersonal(self, idDepartamento):
        consulta = """
            SELECT e.idEmpleado, e.nombre, e.email
            FROM empleados e
            INNER JOIN empleados_departamentos ed
                ON e.idEmpleado = ed.idEmpleado
            WHERE ed.idDepartamento = ?
        """

        return self.__bd.ejecutarConsulta(
            consulta, (idDepartamento,), obtener=True
        )
