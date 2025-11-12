def validar_cedula_ecuatoriana(cedula):
    """
    Función para validar el formato y el dígito verificador de una cédula ecuatoriana.
    Retorna True si la cédula es válida, False en caso contrario.
    """
    # 1. Verifica que tenga 10 dígitos y que sean numéricos
    if not isinstance(cedula, str) or len(cedula) != 10 or not cedula.isdigit():
        return False

    # 2. Verifica el código de la provincia (primeros dos dígitos)
    provincia = int(cedula[0:2])
    if provincia < 1 or provincia > 24:
        return False

    # 3. Cálculo del dígito verificador (algoritmo de módulo 10)
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    suma = 0

    for i in range(9):
        digito = int(cedula[i])
        coeficiente = coeficientes[i]

        valor = digito * coeficiente
        if valor >= 10:
            valor -= 9

        suma += valor

    residuo = suma % 10
    digito_verificador_calculado = 0
    if residuo != 0:
        digito_verificador_calculado = 10 - residuo

    # 4. Compara el dígito calculado con el dígito de la cédula
    digito_verificador_real = int(cedula[9])

    return digito_verificador_calculado == digito_verificador_real