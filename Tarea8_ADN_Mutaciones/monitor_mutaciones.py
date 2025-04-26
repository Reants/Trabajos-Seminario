# Secuencia de referencia
referencia = "ATGCTAGCTAAT"

# Función para detectar mutaciones
def detectar_mutaciones(ref, muestra):
    mutaciones = []
    for i, (r, m) in enumerate(zip(ref, muestra)):
        if r != m:
            mutaciones.append(i)
    return mutaciones

# Leer las secuencias del archivo
def leer_secuencias(nombre_archivo):
    secuencias = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            secuencia = linea.strip()
            if secuencia:
                secuencias.append(secuencia)
    return secuencias

# Monitorear en tiempo real (simulado)
def monitorear_mutaciones(referencia, archivo_sensor):
    secuencias = leer_secuencias(archivo_sensor)
    for idx, secuencia in enumerate(secuencias):
        mutaciones = detectar_mutaciones(referencia, secuencia)
        print(f"Lectura {idx+1}: {secuencia}")
        if mutaciones:
            print(f" -> Mutaciones detectadas en posiciones: {mutaciones}")
        else:
            print(" -> Sin mutaciones detectadas.")

# Ejecutar el monitoreo
if __name__ == "__main__":
    monitorear_mutaciones(referencia, "sensor_data.txt")
