num1 = 10
num2 = 0



try:
    res = num1/num2
except ZeroDivisionError:
    #ZeroDivisionError: es para cuando intentas dividir un numero entre 0
    print("Error en el programa siu")
finally:
    pass


print("Fin del programa")