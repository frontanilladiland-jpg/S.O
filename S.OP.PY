import threading
import time
import queue
import random

cola_documentos = queue.Queue()

for i in range(1, 25):
    cola_documentos.put({"id": f"Doc-{i}", "tamano": random.uniform(0.1, 0.3)})

registro_compartido = {}
lock_registro = threading.Lock()

def trabajador(nombre_trabajador):
    while True:
        try:
            doc = cola_documentos.get_nowait()
        except queue.Empty:
            break

        time.sleep(doc["tamano"])

        with lock_registro:
            registro_compartido[nombre_trabajador] = registro_compartido.get(nombre_trabajador, 0) + 1

        cola_documentos.task_done()

hilos = []
nombres_trabajadores = ["Trabajador 1", "Trabajador 2", "Trabajador 3", "Trabajador 4"]

for nombre in nombres_trabajadores:
    hilo = threading.Thread(target=trabajador, args=(nombre,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

total_procesado = sum(registro_compartido.values())

print("=" * 40)
print("RESUMEN DE PROCESAMIENTO")
print("=" * 40)
for trabajador, cantidad in registro_compartido.items():
    print(f"{trabajador}: {cantidad} documentos procesados")

print("-" * 40)
print(f"Total procesado en el sistema: {total_procesado} documentos")
print("=" * 40)