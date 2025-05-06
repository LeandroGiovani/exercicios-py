import random


vetor = []

aux1 = 0
for i in range(100000):
    add = random.randint(a=1, b=1000000)
    vetor.append(add)

# for i in range(10):
#     value = int(input(f"Digite o {i}º valor: "))
#     vetor.append(value)
    
for j in vetor:
    aux1 += j

# vetor[9] = "Ola"


print(vetor)
index = vetor.count
print(index)
print(f"valor total digitado percorrendo com for:{aux1}")