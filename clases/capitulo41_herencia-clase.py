# CLASE PADRE
class Usuarios:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def muestra_datos(self):
        print("El nombre de usuario es: " + self.nombre, "y tiene", self.edad)


usuario1 = Usuarios("Enrique", 28)
usuario1.muestra_datos()

# CLASE HIJO QUE HERADA TODAS LAS CARACTERISTICAS DEL PADRE
class Usuarios_premium(Usuarios):
    pass


usuario2 = Usuarios_premium("Jorge", 29)
usuario2.muestra_datos()
