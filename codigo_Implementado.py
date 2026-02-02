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
# CLASE CONTACTO
# ------------------------------

class Contacto:
    def __init__(self, id_contacto, nombre, telefono):
        self.id = id_contacto
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.telefono}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono
        }

# ------------------------------
# CLASE AGENDA
# ------------------------------

class Agenda:
    def __init__(self, archivo):
        self.archivo = archivo
        self.contactos = []
        self.cargar()

    def cargar(self):
        if not os.path.exists(self.archivo):
            logging.warning("Archivo JSON no encontrado. Agenda vacía creada.")
            return

        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.contactos = [
                    Contacto(c["id"], c["nombre"], c["telefono"])
                    for c in datos
                ]
                logging.info("Agenda cargada desde fichero.")
        except Exception:
            logging.error("Error al leer el archivo JSON.")

    def guardar(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(
                    [c.to_dict() for c in self.contactos],
                    f,
                    indent=4,
                    ensure_ascii=False
                )
                logging.info("Agenda guardada correctamente.")
        except Exception:
            logging.critical("Error al guardar la agenda.")

    def buscar_por_id(self, id_contacto):
        for contacto in self.contactos:
            if contacto.id == id_contacto:
                return contacto
        return None

    def agregar_contacto(self, contacto):
        if self.buscar_por_id(contacto.id):
            raise ValueError("ID duplicado")

        self.contactos.append(contacto)
        self.guardar()
        logging.info(f"Contacto añadido: {contacto.id}")

    def eliminar_contacto(self, id_contacto):
        contacto = self.buscar_por_id(id_contacto)
        if not contacto:
            raise ValueError("Contacto no encontrado")

        self.contactos.remove(contacto)
        self.guardar()
        logging.info(f"Contacto eliminado: {id_contacto}")

    def mostrar_contactos(self):
        if not self.contactos:
            print("Agenda vacía.")
            return

        for contacto in self.contactos:
            print(contacto)

# ------------------------------
# MENÚ
# ------------------------------

def menu():
    agenda = Agenda(ARCHIVO)

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

        try:
            if opcion == "1":
                id_c = int(input("ID: "))
                nombre = input("Nombre: ").strip()
                telefono = input("Teléfono: ").strip()

                contacto = Contacto(id_c, nombre, telefono)
                agenda.agregar_contacto(contacto)
                print("Contacto agregado.")

            elif opcion == "2":
                id_c = int(input("ID a buscar: "))
                contacto = agenda.buscar_por_id(id_c)
                print(contacto if contacto else "Contacto no encontrado.")

            elif opcion == "3":
                id_c = int(input("ID a modificar: "))
                contacto = agenda.buscar_por_id(id_c)

                if not contacto:
                    print("Contacto no encontrado.")
                    continue

                nuevo_nombre = input("Nuevo nombre (enter para mantener): ").strip()
                nuevo_telefono = input("Nuevo teléfono (enter para mantener): ").strip()

                if nuevo_nombre:
                    contacto.nombre = nuevo_nombre
                if nuevo_telefono:
                    contacto.telefono = nuevo_telefono

                agenda.guardar()
                logging.info(f"Contacto modificado: {id_c}")
                print("Contacto modificado.")

            elif opcion == "4":
                id_c = int(input("ID a eliminar: "))
                agenda.eliminar_contacto(id_c)
                print("Contacto eliminado.")

            elif opcion == "5":
                agenda.mostrar_contactos()

            elif opcion == "6":
                logging.info("Programa cerrado por el usuario.")
                print("Saliendo...")
                break

            else:
                print("Opción incorrecta.")

        except ValueError as e:
            print(e)
            logging.warning(str(e))

# ------------------------------
# EJECUCIÓN
# ------------------------------

if __name__ == "__main__":
    menu()
