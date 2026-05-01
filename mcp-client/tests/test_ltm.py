from app.memory.long_term_memory import LongTermMemory

if __name__ == "__main__":
    ltm = LongTermMemory()
    print("Agregando mensaje de prueba...")
    ltm.add("user", "Hola, este es un mensaje de prueba.")
    print("Mensajes almacenados:")
    for msg in ltm.get_all():
        print(msg)
    print("Limpiando memoria...")
    ltm.clear()
    print("Mensajes después de limpiar:")
    print(ltm.get_all())
