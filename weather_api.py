import requests
import sys

# Función para obtener temperaturas y horas (no completamente mía)
def obtener_temperaturas():
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': 36.7167,   # Jerez de la Frontera
        'longitude': -6.1333,
        'hourly': 'temperature_2m'
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        sys.exit(f"Error al obtener los datos: {response.status_code}")

    data = response.json()
    horas = data['hourly']['time']
    temperaturas = data['hourly']['temperature_2m']

    return horas, temperaturas

# Pregunta si se quiere media de semana o día
def preguntaRango():
    try:
        respuesta = input('¿Quieres la media de toda la semana o de un día en concreto? ("semana"/"dia") ')
        if respuesta.lower() == 'semana':
            return True
        elif respuesta.lower() == 'dia':
            return False
        else:
            sys.exit('Error: valor inválido, por favor, introduzca la palabra "semana" o la palabra "dia" ')
    except Exception as e:
        sys.exit(f"Ocurrió un error: {e}")

# Calcula la media de un día específico usando for
def siEsDia(horas, temperaturas):
    try:
        diaAMirar = int(input("¿Quieres la media de temperatura de dentro de cuántos dias? (0 para la de hoy) "))
        suma = 0
        for i in range(diaAMirar*24, (diaAMirar+1)*24):
            suma += temperaturas[i]
        media = suma / 24
    except Exception as e:
        sys.exit(f"Ocurrió un error: {e}")
    match diaAMirar:
        case 0:
            print(f"Media de hoy: {media:.2f}°C")
        case 1:
            print(f"Media de mañana: {media:.2f}°C")
        case 2:
            print(f"Media de pasado mañana: {media:.2f}°C")
        case _ if diaAMirar > 2:
            print(f"Media de dentro de {diaAMirar + 1} días: {media:.2f}°C")
    

# Calcula la media de toda la semana usando for
def siEsSemana(horas, temperaturas):
    suma = 0
    for temp in temperaturas:
        suma += temp
    media = suma / len(temperaturas)
    print(f"Media de toda la semana: {media:.2f}°C")

# --- Flujo vaginal digo natural**** ---
horas, temperaturas = obtener_temperaturas()
semanaODia = preguntaRango()

if semanaODia == False:
    siEsDia(horas, temperaturas)
else:
    siEsSemana(horas, temperaturas)
