import pickle
import os

# Clase que representa el estado de la aplicación
class EstadoAplicacion:
    def __init__(self, paso, datos):
        self.paso = paso  # Paso actual de la ejecución
        self.datos = datos  # Datos de la aplicación

    def __str__(self):
        return f"Paso: {self.paso}, Datos: {self.datos}"

def guardar_checkpoint(estado, archivo="checkpoint.pkl"):
    with open(archivo, "wb") as f:
        pickle.dump(estado, f)
    print(f"Checkpoint guardado en '{archivo}'")

def cargar_checkpoint(archivo="checkpoint.pkl"):
    if os.path.exists(archivo):
        with open(archivo, "rb") as f:
            estado = pickle.load(f)
        print(f"Checkpoint cargado desde '{archivo}'")
        return estado
    else:
        print(f"No se encontró el archivo de checkpoint '{archivo}'")
        return None

def ejecutar_aplicacion():
    # Intentar cargar un checkpoint existente
    estado = cargar_checkpoint()

    if estado is None:
        # Si no hay checkpoint, empezar desde el principio
        estado = EstadoAplicacion(paso=0, datos=[])
        print("Comenzando desde el paso 0...")
    else:
        print(f"Restaurando desde el paso {estado.paso}...")


    for i in range(estado.paso, 10):
        estado.paso = i
        estado.datos.append(f"Dato del paso {i}")
        print(f"Ejecutando paso {i}...")

        respuesta = input("¿Deseas guardar un checkpoint? (s/n): ").strip().lower()
        if respuesta == "s":
            guardar_checkpoint(estado)

    print("Aplicación completada.")

ejecutar_aplicacion()