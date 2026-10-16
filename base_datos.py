
import sqlite3


class BaseDatos:

    def __init__(self, nombre_bd="ecotech.db"):
        self.__nombre_bd = nombre_bd

    def conectar(self):
        try:
            conexion = sqlite3.connect(self.__nombre_bd)
            conexion.execute("PRAGMA foreign_keys = ON")
            print("Conexión exitosa a SQLite")
            return conexion

        except sqlite3.Error as error:
            print("Error al conectar:", error)
            return None

    def crearTablas(self):
        conexion = self.conectar()

        if conexion is None:
            return False

        try:
            cursor = conexion.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departamentos (
                    idDepartamento TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    gerente TEXT NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleados (
                    idEmpleado TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleados_departamentos (
                    idEmpleado TEXT PRIMARY KEY,
                    idDepartamento TEXT NOT NULL,
                    FOREIGN KEY (idEmpleado)
                        REFERENCES empleados(idEmpleado),
                    FOREIGN KEY (idDepartamento)
                        REFERENCES departamentos(idDepartamento)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyectos (
                    idProyecto TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    descripcion TEXT
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS registros_tiempo (
                    idRegistro TEXT PRIMARY KEY,
                    fecha TEXT NOT NULL,
                    cantidadHoras REAL NOT NULL
                        CHECK(cantidadHoras > 0 AND cantidadHoras <= 24),
                    descripcionTareas TEXT,
                    idEmpleado TEXT NOT NULL,
                    idProyecto TEXT NOT NULL,
                    FOREIGN KEY (idEmpleado)
                        REFERENCES empleados(idEmpleado),
                    FOREIGN KEY (idProyecto)
                        REFERENCES proyectos(idProyecto)
                )
            """)

            conexion.commit()
            print("Tablas creadas correctamente")
            return True

        except sqlite3.Error as error:
            conexion.rollback()
            print("Error al crear tablas:", error)
            return False

        finally:
            conexion.close()

    def ejecutarConsulta(self, consulta, parametros=(), obtener=False):
        conexion = self.conectar()

        if conexion is None:
            return None

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta, parametros)

            if obtener:
                return cursor.fetchall()

            conexion.commit()
            return True

        except sqlite3.Error as error:
            conexion.rollback()
            print("Error en la consulta:", error)
            return None

        finally:
            conexion.close()
