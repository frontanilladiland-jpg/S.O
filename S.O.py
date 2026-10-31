import threading
import time

def tarea(nombre):
    for i in range(4):  # range requiere números enteros
        print(nombre, "-> paso", i)
        time.sleep(0.4)

# Creación de los hilos (fuera de la función)
hilo_a = threading.Thread(target=tarea, args=("A",))
hilo_b = threading.Thread(target=tarea, args=("B",))

# Iniciar los hilos
hilo_a.start()
hilo_b.start()

# Esperar a que ambos hilos terminen antes de continuar
hilo_a.join()
hilo_b.join()

print("Todas las tareas terminaron")