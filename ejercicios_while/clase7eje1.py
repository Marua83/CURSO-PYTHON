# ejercicio 1 Listas
numeros=[]
mayor=99999999
menor=99999999
suma=0
for i in range (5):
    num= input("ingrese un numero:")
    numeros.append(int(num))
    if num < menor: 
        menor = num
    if num > mayor: 
        mayor = num
    suma += num

print(numeros)
print("Mayor: ", max(numeros))
print("Menor: ", min(numeros))
print("suma: ", sum(num))   