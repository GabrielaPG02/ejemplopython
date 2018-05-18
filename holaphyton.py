num= int(input("Número:"))
lista = []
while num>0:
	lista.append(num)
	num= int(input("Número:"))

print ("Máximo: %d" % max(lista))

for elemento in lista:
	if elemento %2 ==0: 
		print(elemento)