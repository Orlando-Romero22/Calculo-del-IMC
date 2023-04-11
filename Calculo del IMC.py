personas = int(input( "personas: "))

while personas > 0 :
       
       nombre = input ("Introduce tu nombre: ")

       edad = int (input("Introduce tu edad: "))

       altura = float(input("Su altura en metros: "))

       est = altura

       masa = float (input("Su masa en Kilogramos: "))

       IMC = masa / est **2

       if (edad < 18):

            print ("Usted es menor de edad")

       else:

             print("Usted es mayor de edad")

       print(f"Soy {nombre} y tengo {edad} años, mido {altura} metros y peso {masa} Kg, siendo mi IMC:" + str (IMC))

       if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
       elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
       elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
       elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
       elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
       elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
       elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
       elif IMC >= 40.00:
        print ("obesidad morbida")

       personas = personas - 1        



