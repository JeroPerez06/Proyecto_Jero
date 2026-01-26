import json
import logging
import os

# ------------------------------
# CONFIGURACIÓN
# ------------------------------

ARCHIVO = "agenda_datos.json"

logging.basicConfig(
    filename="agenda.log",
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

# ------------------------------
# GESTIÓN DE FICHEROS
# ------------------------------

def cargar_agenda():
    if not os.path.exists(ARCHIVO):
        logging.warning("Archivo JSON no encontrado. Agenda vacía creada.")
        return []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            logging.info("Agenda cargada desde fichero.")
            return json.load(f)
    except Exception:
        logging.error("Error al leer el archivo JSON.")
        return []


def guardar_agenda(agenda):
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(agenda, f, indent=4, ensure_ascii=False)
            logging.info("Agenda guardada correctamente.")
    except Exception:
        logging.critical("Error al guardar la agenda.")

# ------------------------------
# FUNCIONES PRINCIPALES
# ------------------------------

def agregar_contacto(agenda):
    print("\n--- Añadir contacto ---")

    try:
        id_contacto = int(input("ID: "))
    except ValueError:
        print("ID incorrecto.")
        logging.error("ID no numérico al añadir.")
        return

    if any(c["id"] == id_contacto for c in agenda):
        print("Ese ID ya existe.")
        logging.warning("Intento de insertar ID duplicado.")
        return

    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()

    if not nombre or not telefono:
        print("Los campos no pueden estar vacíos.")
        logging.warning("Campos vacíos al añadir contacto.")
        return

    agenda.append({
        "id": id_contacto,
        "nombre": nombre,
        "telefono": telefono
    })

    guardar_agenda(agenda)
    logging.info(f"Contacto añadido: {id_contacto}")
    print("Contacto agregado correctamente.")


def buscar_contacto(agenda):
    print("\n--- Buscar contacto ---")

    try:
        id_buscar = int(input("ID a buscar: "))
    except ValueError:
        print("ID inválido.")
        logging.error("ID no válido en búsqueda.")
        return

    for contacto in agenda:
        if contacto["id"] == id_buscar:
            print(contacto)
            logging.info(f"Contacto encontrado: {id_buscar}")
            return

    print("Contacto no encontrado.")
    logging.warning(f"Contacto no encontrado: {id_buscar}")


def modificar_contacto(agenda):
    print("\n--- Modificar contacto ---")

    try:
        id_modificar = int(input("ID a modificar: "))
    except ValueError:
        print("ID inválido.")
        logging.error("ID incorrecto al modificar.")
        return

    for contacto in agenda:
        if contacto["id"] == id_modificar:
            nuevo_nombre = input("Nuevo nombre (enter para mantener): ").strip()
            nuevo_telefono = input("Nuevo teléfono (enter para mantener): ").strip()

            if nuevo_nombre:
                contacto["nombre"] = nuevo_nombre
            if nuevo_telefono:
                contacto["telefono"] = nuevo_telefono

            guardar_agenda(agenda)
            logging.info(f"Contacto modificado: {id_modificar}")
            print("Contacto modificado.")
            return

    print("Contacto no existe.")
    logging.warning(f"Intento de modificar ID inexistente: {id_modificar}")


def eliminar_contacto(agenda):
    print("\n--- Eliminar contacto ---")

    try:
        id_eliminar = int(input("ID a eliminar: "))
    except ValueError:
        print("ID inválido.")
        logging.error("ID incorrecto al eliminar.")
        return

    for i, contacto in enumerate(agenda):
        if contacto["id"] == id_eliminar:
            agenda.pop(i)
            guardar_agenda(agenda)
            logging.info(f"Contacto eliminado: {id_eliminar}")
            print("Contacto eliminado.")
            return

    print("Contacto no encontrado.")
    logging.warning(f"Intento de eliminar ID inexistente: {id_eliminar}")


def mostrar_contactos(agenda):
    print("\n--- Agenda ---")

    if not agenda:
        print("Agenda vacía.")
        return

    for c in agenda:
        print(f"{c['id']} | {c['nombre']} | {c['telefono']}")

# ------------------------------
# MENÚ
# ------------------------------

def menu():
    agenda = cargar_agenda()

    while True:
        print("""
===== AGENDA =====
1. Añadir contacto
2. Buscar contacto
3. Modificar contacto
4. Eliminar contacto
5. Mostrar contactos
6. Salir
""")

        opcion = input("Opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            modificar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            mostrar_contactos(agenda)
        elif opcion == "6":
            logging.info("Programa cerrado por el usuario.")
            print("Saliendo del programa...")
            break
        else:
            print("Opción incorrecta.")
            logging.warning("Opción de menú inválida.")

# ------------------------------
# EJECUCIÓN
# ------------------------------

if __name__ == "__main__":
    menu()


