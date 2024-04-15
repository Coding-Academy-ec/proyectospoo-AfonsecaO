# Archivo: gestion_tareas/__main__.py
from gestion_tareas.tareas.tarea_personal import TareaPersonal
from gestion_tareas.tareas.tarea_proyecto import TareaProyecto

def main():
    # Crear algunas tareas personales
    tarea_personal1 = TareaPersonal("Comprar víveres", "Ir al supermercado y comprar los víveres para la semana", "2024-03-10", "Alta")
    tarea_personal2 = TareaPersonal("Hacer ejercicio", "Ir al gimnasio y hacer ejercicio durante una hora", "2024-03-08", "Media")

    # Crear algunas tareas de proyecto
    tarea_proyecto1 = TareaProyecto("Diseñar interfaz de usuario", "Diseñar la interfaz de usuario para la nueva aplicación móvil", "2024-03-15", "Equipo de diseño")
    tarea_proyecto2 = TareaProyecto("Implementar backend", "Implementar la lógica del backend utilizando Django", "2024-03-20", "Equipo de desarrollo")


    tarea_nombre = input("Ingresa el nombre de la tarea: ")
    tarea_descripcion = input("Ingresa la descripción de la tarea: ")
    tarea_limite = input("Ingresa la fecha limite de la tarea: ")
    tarea_urgencia = input("Ingresa la prioridad de la tarea: ")

    proyecto_nombre = input("Ingresa el nombre del proyecto: ")
    proyecto_descripcion = input("Ingresa la descripción del proyecto: ")
    proyecto_inicio = input("Ingresa la fecha de inicio del proyecto: ")
    proyecto_responsable = input("Ingresa el responsable del proyecto: ")

    tarea_personal3 = TareaPersonal(tarea_nombre, tarea_descripcion, tarea_limite, tarea_urgencia)
    tarea_proyecto3 = TareaProyecto(proyecto_nombre, proyecto_descripcion, proyecto_inicio, proyecto_responsable)

    # Mostrar detalles de las tareas
    print("Tareas personales:")
    print(tarea_personal1)
    print(tarea_personal2)
    print(tarea_personal3)

    print("\nTareas de proyecto:")
    print(tarea_proyecto1)
    print(tarea_proyecto2)
    print(tarea_proyecto3)

if __name__ == "__main__":
    main()
