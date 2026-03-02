while True:
    #Mientras sea true trata:
    try:
        #Escribimos ahora el costo
        costo = float(input('Escribe el precio del material: '))
        #validacion para negativo
        if costo < 0:
            print('Número negativo, ingresa un número válido.')
            #Si es positivo continua con el ciclo
            continue
        #Rompe el bucle
        break
    #while True + break permite repetir hasta validación correcta.
    #Si NO es un numero da error de valor , ValueError ocurre cuando el tipo de dato no es el esperado.
    except ValueError:
        print('Entrada no válida. Ingresa un número entero.')
    #try/except se usa para manejar errores en tiempo de ejecución.
