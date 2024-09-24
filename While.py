Dias=15
while Dias > 0:
    if input("Ingrese el numero de tareas pendientes para dentro de 15 dias: ") == "0":
        print("Felicidades has acabado tus deberes!!!")
        break
    Dias=Dias-1
    print("falta poco tu puedes!")
else:
    print("oh no!, no lograste acabar en el tiempo estipulado")