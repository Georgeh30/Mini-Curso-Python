from datetime import *
import locale

# INDICAMOS QUE NUESTRA IDIAMA ES ESPAÑOL PARA QUE MUESTRA LOS DATOS EN ESPAÑOL Y NO EN INGLES
locale.setlocale(locale.LC_ALL, "es-ES")
fecha = datetime.now()  # GUARDA LA FECHA DE HOY

print(fecha.strftime("%A"))  # IMPRIME EL DIA
print(fecha.strftime("%H"))  # LA HORA
print(fecha.strftime("%M"))  # LOS MINUTOS

