def leer_registros(ruta_archivo):
    """
    Lee el archivo de registros y devuelve una lista con los registros de usuarios.
    """
    registros = []
    with open(ruta_archivo, 'r') as archivo:
        # Leer línea por línea
        while True:
            linea = archivo.readline().strip()
            if not linea:
                break
            # Extraer nombre de usuario, hora de entrada y salida
            nombre, entrada, salida = linea.split(',')
            registros.append([nombre, entrada, salida])
    return registros

def contar_accesos(registros):
    """
    Cuenta el número de accesos por cada usuario.
    """
    accesos = {}
    # Usamos un bucle for para contar accesos por usuario
    for registro in registros:
        nombre_usuario = registro[0]
        if nombre_usuario in accesos:
            accesos[nombre_usuario] += 1
        else:
            accesos[nombre_usuario] = 1
    # Convertimos el diccionario en una lista de listas
    resultados = [[usuario, accesos[usuario]] for usuario in accesos]
    return resultados

def mostrar_resultados(resultados):
    """
    Muestra los resultados de accesos por usuario.
    """
    for resultado in resultados:
        print(f"Usuario: {resultado[0]} - Accesos: {resultado[1]}")

def main():
    ruta_archivo = 'registros.txt'  # Cambiar por la ruta de tu archivo
    registros = leer_registros(ruta_archivo)
    resultados = contar_accesos(registros)
    mostrar_resultados(resultados)

