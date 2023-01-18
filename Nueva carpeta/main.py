
import Tkinter as tk 
def segundos_a_segundos_minutos_y_horas(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    variable_hora_actual = tk.StringVar(raiz, value=obtener_tiempo_transcurrido_formateado())