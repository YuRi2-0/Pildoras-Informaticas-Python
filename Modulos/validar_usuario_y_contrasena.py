def validarUsuario(nombre):
    validacion_usuario = False
    if len(nombre)<5:
        return 'El usuario no puede tener menos de 5 caracteres'
    elif len(nombre) > 15:
        return 'El usuario no puede tener mas de 15 caracteres'
    
    if not nombre.isalnum():
        return 'El usuario solo puede contener letras y numeros'
    
    validacion_usuario = True
    
    return validacion_usuario


def validarContrasena(contraseña):
    validacion_contraseña = False
    conversion_string = str(contraseña)
    if len(conversion_string) < 10:
        return "La contraseña debe tener mas de 10 caracteres"
    
    if conversion_string.isalnum():
        return 'La contraseña debe contener un caracter que no sea ni letra ni numero'
    
    tiene_mayuscula = any(c.isupper() for c in conversion_string)
    tiene_minuscula = any(c.islower() for c in conversion_string)
    
    if(not tiene_mayuscula or not tiene_minuscula):
        return "La contraseña debe contener al menos una letra mayúscula y una minúscula"
    
    for i in conversion_string:
        if i == " ":
            return "La contraseña no puede contener espacios en blanco"
    
    validacion_contraseña = True
    
    return validacion_contraseña
# print(validarContrasena("12345678fff@fggG"))




