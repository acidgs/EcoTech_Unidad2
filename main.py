
from empleado import Empleado
from departamento import Departamento
from proyecto import Proyecto
from registro_tiempo import RegistroTiempo

from base_datos import BaseDatos

from repositorio import (
    EmpleadoRepositorio,
    ProyectoRepositorio,
    RegistroTiempoRepositorio,
    DepartamentoRepositorio,
    EmpleadoDepartamentoRepositorio
)


print("=== SISTEMA ECOTECH SOLUTIONS ===")

# CONEXION A LA BASE DE DATOS

bd = BaseDatos()

if bd.crearTablas():

    # CREAR EMPLEADO

    empleado1 = Empleado(
        "EMP-001",
        "ana@ecotech.cl",
        "hash123",
        "empleado",
        "Ana Pérez",
        "Av. Libertador 123",
        "+56912345678",
        "2024-03-01",
        1200000
    )

    print("\n--- PRUEBA DE HERENCIA ---")
    print("Autenticación:", empleado1.autenticar("hash123"))
    print("Autorización:", empleado1.verificarAutorizacion("empleado"))

    # CREAR DEPARTAMENTO

    departamento1 = Departamento(
        "DEP-01",
        "Desarrollo Sostenible",
        "María González"
    )

    departamento1.agregarEmpleado(empleado1)

    # CREAR PROYECTO

    proyecto1 = Proyecto(
        "PROJ-10",
        "Optimización Energética",
        "Reducción de consumo en plantas",
        "2026-01-15"
    )

    proyecto1.asignarEmpleado(empleado1)

    # REGISTRO DE HORAS

    registro1 = RegistroTiempo(
        "REG-501",
        "2026-06-10",
        4.5,
        "Desarrollo de módulos de cifrado",
        empleado1,
        proyecto1
    )

    print("\n--- REGISTRO DE TIEMPO ---")

    registroValido = registro1.crearRegistro()

    if registroValido:
        registro1.mostrarRegistro()

    # REPOSITORIOS

    empleadoRepo = EmpleadoRepositorio()
    departamentoRepo = DepartamentoRepositorio()
    proyectoRepo = ProyectoRepositorio()
    registroRepo = RegistroTiempoRepositorio()
    asignacionRepo = EmpleadoDepartamentoRepositorio()

    # GUARDAR DATOS EN SQLITE

    print("\n--- GUARDAR DATOS ---")

    empleadoRepo.guardarEmpleado(
        "EMP-001", "Ana Pérez", "ana@ecotech.cl"
    )

    departamentoRepo.guardarDepartamento(
        "DEP-01", "Desarrollo Sostenible", "María González"
    )

    proyectoRepo.guardarProyecto(
        "PROJ-10",
        "Optimización Energética",
        "Reducción de consumo en plantas"
    )

    asignacionRepo.asignarEmpleadoDepartamento(
        "EMP-001", "DEP-01"
    )

    if registroValido:
        registroRepo.guardarRegistro(
            "REG-501",
            "2026-06-10",
            4.5,
            "Desarrollo de módulos de cifrado",
            "EMP-001",
            "PROJ-10"
        )

    # CONSULTAR DATOS

    print("\n--- EMPLEADOS REGISTRADOS ---")

    empleados = empleadoRepo.listarEmpleados()

    if empleados is not None:
        for empleado in empleados:
            print(empleado)

    print("\n--- PERSONAL DEL DEPARTAMENTO ---")

    personal = asignacionRepo.listarPersonal("DEP-01")

    if personal is not None:
        for empleado in personal:
            print(empleado)

    print("\n--- REGISTROS DE TIEMPO ---")

    registros = registroRepo.listarRegistros()

    if registros is not None:
        for registro in registros:
            print(registro)

    print("\n=== PRUEBA FINALIZADA ===")

else:
    print("No se pudo conectar a la base de datos")
