print("Hola, bienvenido al parque de atracciones. Compre sus entradas!")
edad = int(input("Ingrese su edad: "))
dia = input("Para que día desea adquirir su entrada?: ")

if dia=="miercoles" and (edad<=18) or (edad>=60) :
    print("Entrada gratis!")
elif (dia=="sabado") or (dia=="domingo"):
    if (edad<18):
        print("La entrada vale $400")
    else:
        print("La entrada vale $500")
else:
    print("La entrada vale $800")