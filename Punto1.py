#ACTIVIDAD 19

#PUNTO 1 INCISO 1
numero = int(input("Digite un numero aleatorio"))

if numero % 2 == 0:
    print("el numero que digitaste es par")
else:
    print("el numero que digitaste es impar")

#PUNTO 1 INCISO 2

numero2 = int(input("Digite otro numero aleatorio"))

if 1 <= numero2 <=9:
    print("el numero tiene un digito")
elif 10 <= numero2 <= 99:
    print("el numero tiene dos digitos")
elif 100 <= numero2 <=999:
    print("el numero tiene 3 digitos")
else:
    print("el numero tiene mas de tres digitos")