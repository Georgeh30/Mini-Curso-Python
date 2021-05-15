# LAS VARIABLES DECLARADAS A FUERA DE CUALQUIER METODO, CLASE O FUNCION SON VARIABLES GLOBALES
variable1 = "Variable fuera de la función."


def funcion1():
    print(variable1)

    # AL DECLARAR UNA VARIABLE ADENTRO Y QUEREMOS QUE SEA GLOBA SE DEBE PONER global
    global variable2
    variable2 = "Esta es la variable dentro de la funcion pero es global"

    # FUNCION ANIDADA
    def funcion2():
        variable1 = "Hemos cambiado el valor de la variable1."
        print(variable1)

    # LLAMANDO LA FUNCION ANIDADA DENTRO DE LA FUNCION1
    funcion2()


funcion1()
print(variable2)
