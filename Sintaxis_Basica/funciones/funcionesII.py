# def imprimeMensaje():
    
#     return "Este es el mensaje de la funcion"

# def imprimeMensajePersonalizado(mensaje, num1, num2):
    
#     return f"{mensaje} {num1 + num2}"


# print(imprimeMensajePersonalizado("La suma es:",4,8))

# def sumarValores(*num):
#     print(type(num))
#     acumulador = 0
#     for x in num:
#         acumulador+=x
#     return acumulador


# print(sumarValores(1,2,3,4,5))


# def suma(**kwargs):
#     suma = 0
#     for key, value in kwargs.items():
#         print(key, value)
#         suma += value
#     return suma

# print(suma(a=5, b=20, c=23))  # 48


def mi_funcion_suma(a, b):
    """
    Descripción de la función. Como debe ser usada,
    que parámetros acepta y que devuelve
    """
    return a+b

help(mi_funcion_suma)