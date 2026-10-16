
from base_datos import BaseDatos
from repositorio import (
    EmpleadoRepositorio,
    RegistroTiempoRepositorio,
    EmpleadoDepartamentoRepositorio
)

from empleado import Empleado
from departamento import Departamento
from proyecto import Proyecto
from registro_tiempo import RegistroTiempo


def main():

    print("=== SISTEMA ECOTECH SOLUTIONS ===")

    # 1. Verificar base de datos
    print("\n--- CONEXIÓN A BASE DE DATOS ---")

    bd = BaseDatos()

    if not bd.crearTablas():
        print("No se pudo iniciar el sistema")
        return

    # 2. Crear objetos del modelo UML
    print("\n--- CREACIÓN DE OBJETOS ---")

    empleado = Empleado(
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

    departamento = Departamento(
        "DEP-01",
        "Desarrollo Sostenible",
        "María González"
    )

    proyecto = Proyecto(
        "PROJ-10",
        "Optimización Energética",
        "Reducción de consumo en plantas",
        "2026-01-15"
    )

    # 3. Probar herencia
    print("\n--- HERENCIA ---")

    print("Autenticación:", empleado.autenticar("hash123"))
    print("Autorización:", empleado.verificarAutorizacion("empleado"))

    # 4. Probar asociaciones
    print("\n--- ASOCIACIONES ---")

    departamento.agregarEmpleado(empleado)
    proyecto.asignarEmpleado(empleado)

    departamento.listarPersonal()

    # 5. Crear registro de tiempo
    print("\n--- REGISTRO DE TIEMPO ---")

    registro = RegistroTiempo(
        "REG-501",
        "2026-06-10",
        4.5,
        "Desarrollo de módulos de cifrado",
        empleado,
        proyecto
    )

    if registro.crearRegistro():
        registro.mostrarRegistro()
        
        print("\n--- GUARDAR NUEVO REGISTRO EN SQLITE ---")

        registroRepoNuevo = RegistroTiempoRepositorio()

        guardado = registroRepoNuevo.guardarRegistro(
            "REG-501",
            "2026-06-10",
            4.5,
            "Desarrollo de módulos de cifrado",
            "EMP-001",
            "PROJ-10"
        )

        print("Guardado exitoso:", guardado)


    # 6. Consultar datos persistidos
    print("\n--- EMPLEADOS EN SQLITE ---")

    empleadoRepo = EmpleadoRepositorio()

    for fila in empleadoRepo.listarEmpleados():
        print(fila)

    print("\n--- PERSONAL DEL DEPARTAMENTO EN SQLITE ---")

    asignacionRepo = EmpleadoDepartamentoRepositorio()

    for fila in asignacionRepo.listarPersonal("DEP-01"):
        print(fila)

    print("\n--- REGISTROS EN SQLITE ---")

    registroRepo = RegistroTiempoRepositorio()

    for fila in registroRepo.listarRegistros():
        print(fila)

    print("\n=== PRUEBA FINALIZADA ===")


if __name__ == "__main__":
    main()
