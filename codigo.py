# ESTRUCTURA PRINCIPAL
# ------------------------------
agenda = []   # Cada elemento será: {"id": int, "nombre": str, "telefono": str}

# FUNCIONES
# ------------------------------

def insertar_elemento(agenda):
    """
    Pide datos al usuario, valida y agrega un nuevo contacto a la agenda.
    """
    print("\n--- Insertar contacto ---")

    # Validar ID como entero
    try:
        id_contacto = int(input("Ingrese ID del contacto: "))
    except ValueError:
        print("Error: el ID debe ser un número entero.")
        return

    # Validar nombre no vacío
    nombre = input("Ingrese nombre: ").strip()
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return

    # Validar teléfono no vacío
    telefono = input("Ingrese teléfono: ").strip()
    if telefono == "":
        print("Error: el teléfono no puede estar vacío.")
        return

    # Crear el nuevo elemento
    contacto = {
        "id": id_contacto,
        "nombre": nombre,
        "telefono": telefono
    }

    agenda.append(contacto)
    print("✔ Contacto agregado correctamente.")


def buscar_elemento(agenda):
    """
    Busca un contacto por ID y lo muestra si existe.
    """
    print("\n--- Buscar contacto ---")
    try:
        id_buscar = int(input("Ingrese ID del contacto a buscar: "))
    except ValueError:
        print("Error: el ID debe ser un número.")
        return

    for contacto in agenda:
        if contacto["id"] == id_buscar:
            print("✔ Contacto encontrado:")
            print(contacto)
            return contacto

    print("No se encontró un contacto con ese ID.")
    return None


def modificar_elemento(agenda):
    """
    Permite modificar un contacto existente manejando errores.
    """
    print("\n--- Modificar contacto ---")
    try:
        id_modificar = int(input("Ingrese ID del contacto a modificar: "))
    except ValueError:
        print("Error: el ID debe ser un número.")
        return

    for contacto in agenda:
        if contacto["id"] == id_modificar:
            print(f"Contacto encontrado: {contacto}")
            nuevo_nombre = input("Nuevo nombre (enter para no cambiar): ").strip()
            nuevo_telefono = input("Nuevo teléfono (enter para no cambiar): ").strip()

            # Actualización solo si el usuario ingresa valores
            if nuevo_nombre != "":
                contacto["nombre"] = nuevo_nombre
            if nuevo_telefono != "":
                contacto["telefono"] = nuevo_telefono

            print("✔ Contacto modificado correctamente.")
            return

    print("No existe un contacto con ese ID.")


def eliminar_elemento(agenda):
    """
    Elimina un contacto por ID si existe.
    Maneja errores si el ID no se encuentra.
    """
    print("\n--- Eliminar contacto ---")
    try:
        id_eliminar = int(input("Ingrese ID del contacto a eliminar: "))
    except ValueError:
        print("Error: el ID debe ser un número.")
        return

    for i, contacto in enumerate(agenda):
        if contacto["id"] == id_eliminar:
            agenda.pop(i)
            print("✔ Contacto eliminado correctamente.")
            return

    print("No se encontró un contacto con ese ID.")


def mostrar_todos(agenda):
    """
    Muestra todos los contactos de la agenda formateados.
    """
    print("\n--- Agenda completa ---")
    if not agenda:
        print("La agenda está vacía.")
        return

    for contacto in agenda:
        print(f"ID: {contacto['id']} | Nombre: {contacto['nombre']} | Teléfono: {contacto['telefono']}")

# MENÚ INTERACTIVO
# ------------------------------

def menu():
    """
    Menú interactivo principal del programa.
    """
    while True:
        print("""\n===== AGENDA DE CONTACTOS =====
1. Añade un contacto
2. Busca un contacto
3. Modifica un contacto
4. Elimina un contacto
5. Muestra a todos los contactos
6. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertar_elemento(agenda)
        elif opcion == "2":
            buscar_elemento(agenda)
        elif opcion == "3":
            modificar_elemento(agenda)
        elif opcion == "4":
            eliminar_elemento(agenda)
        elif opcion == "5":
            mostrar_todos(agenda)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar el menú si se abre el archivo directamente
if __name__ == "__main__":
    menu()
