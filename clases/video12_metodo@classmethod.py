# 1. METODO CON DATOS INDEPENDIENTES --> CLASSMETHOD
# 2. METODO STATIC --> STATICMETHOD
# NINGUNO DE LOS DOS METODOS NECESITAN CREAR UNA INSTANCIA

class Pastel:
    def __init__(self, ingredientes1):
        self.ingredientes1 = ingredientes1

    def __repr__(self):
        return f'pastel({self.ingredientes1 !r})'

    @classmethod
    def Pastel_chocolate(cls):
        return cls(["harina", "leche", "chocolate"])

    @classmethod
    def Pastel_vainilla(cls):
        return cls(["harina", "leche", "vainilla"])


print(Pastel.Pastel_chocolate())  # IMPRIMIMOS EL METODO DE CLASE UNICO

print(Pastel.Pastel_vainilla())  # IMPRIMIMOS EL METODO DE CLASE UNICO
