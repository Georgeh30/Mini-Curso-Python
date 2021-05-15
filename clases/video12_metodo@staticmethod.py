# 1. METODO CON DATOS INDEPENDIENTES --> CLASSMETHOD
# 2. METODO STATIC --> STATICMETHOD
# NINGUNO DE LOS DOS METODOS NECESITAN CREAR UNA INSTANCIA
import math


class Pastel:
    def __init__(self, ingredientes1, tamano):
        self.ingredientes1 = ingredientes1
        self.tamano = tamano

    def __repr__(self):
        return f'pastel({self.ingredientes1}, 'f'{self.tamano})'

    def area(self):
        return self.tamano_area(self.tamano)

    @staticmethod
    def tamano_area(A):
        return A ** 2 * math.pi


nuevo_pastel = Pastel(["harina", "azucar", "leche", "crema"], 4)
print(nuevo_pastel.ingredientes1)
print(nuevo_pastel.tamano)

# LLAMAMOS EL METODO ESTATICO
print(nuevo_pastel.tamano_area(12))
