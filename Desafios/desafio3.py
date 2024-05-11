#Aquí se le pide al usuario sus datos
datos_usuario = { "Nombre":input("Ingrese su nombre: "),
                  "Edad":int(input("Ingrese su edad: ")),
                  "Nacimiento":int(input("En que año nació?: ")),
                  "Altura":float(input("Cual es su altura?: ")),
                  "Nacionalidad":input("Cual es su nacionalidad?: "),
                  "Ciudad":input("En que ciudad vive?: "),
                  }

#Aquí se muestran las claves con sus valores
print("A continuación se le detalla los datos obtenidos:")
for clave, valor in datos_usuario.items():
    print(f"{clave} : {valor}")

#Aquí el usuario calcula mentalmente su edad, para luego corroborar su respuesta
print("Ingrese un año y calcule mentalmente, luego se comprobará el resultado")
año_random=int(input("Ingrese un año aleatorio: "))
año_usuario=int(input("Cuantos años crres que tendras?: "))
respuesta=año_random - datos_usuario["Nacimiento"]
if respuesta==año_usuario:
    print("Has calculado bien!")
else:
    print(f"Incorrecto, la respuesta era: {respuesta}")

#El usuario elige un numero para luego generar una "tabla" de multiplicación del 0 al 10
numero=int(input("Escriba un número: "))
for i in range(0,11):
    resultado= i*numero
    print(numero, "X", i, "=", resultado)
print("Hasta luego!")