from biblioteca.libros import Libro
from biblioteca.usuarios import Usuario
from biblioteca.transacciones import Transaccion

def main():
    # Crear algunos libros
    libro1 = Libro("1234567890", "Python Programming", "Guido van Rossum")
    libro2 = Libro("0987654321", "Clean Code", "Robert C. Martin")

    # Crear algunos usuarios
    usuario1 = Usuario("1001", "Alice")
    usuario2 = Usuario("1002", "Bob")

    # Fecha de préstamo
    fecha_prestamo = "2024-03-10"  # Por ejemplo, fecha actual

    # Realizar algunas transacciones
    transaccion1 = Transaccion(usuario1, libro1, fecha_prestamo)
    transaccion1.prestar()
    transaccion2 = Transaccion(usuario2, libro2, fecha_prestamo)
    transaccion2.prestar()

    #ingresar manualmente los datos de las transacciones
    codigo_libro = input("Ingresa el Codigo de Libro: ")
    nombre_libro = input("Ingresa el Nombre del Libro: ")
    autor_libro = input("Ingresa el Autor del Libro: ")
    usuario_presta = input("Ingresa el Codigo de Usuario: ")
    nombre_usuario = input("Ingresa el Nombre del Usuario: ")

    libro3 = Libro(codigo_libro, nombre_libro, autor_libro)
    usuario3 = Usuario(usuario_presta, nombre_usuario)
    transaccion3 = Transaccion(usuario3, libro3, fecha_prestamo)
    transaccion3.prestar()

    # Mostrar detalles de las transacciones
    print("Transacciones realizadas:")
    for transaccion in [transaccion1, transaccion2, transaccion3]:
        print(transaccion)

if __name__ == "__main__":
    main()
