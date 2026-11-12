def es_codigo_valido(codigo):

    return isinstance(codigo, str) and len(codigo.strip()) > 0


def es_porcentaje_valido(porcentaje):

    return 0.0 <= porcentaje <= 100.0


def validar_descuento():

    codigo = input("Código de descuento: ")
    
    if not es_codigo_valido(codigo):
        print("Error: El código de descuento está vacío o compuesto solo por espacios.")
        return

    try:

        porcentaje_ingresado = input("Porcentaje (0.0 - 100.0): ")
        porcentaje = float(porcentaje_ingresado)
        
        if not es_porcentaje_valido(porcentaje):
            print("Error: El porcentaje debe estar entre 0.0 y 100.0 inclusive.")
            return
            
        print("Descuento válido.")

    except ValueError:
        print("Error: Debe ingresar un número decimal válido para el porcentaje.")



if __name__ == "__main__":
    validar_descuento()
