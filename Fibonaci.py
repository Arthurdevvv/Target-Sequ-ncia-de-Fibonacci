res = int(input("Digite um número> "))
sequencia = [0,1]
j=1
i=0

while i < res:
    i = sequencia [j] + sequencia[j-1]
    j=j+1
    sequencia.append(i)

print(sequencia)
if sequencia[j] == res:
    print("Este Número está na sequência!")
else:
    print ("Este Número não está na sequência.")
    