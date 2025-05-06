matriz = []
linha_matriz = []

for i in range(1, 10):
    num = int(input(f"Número {i} da matriz 3x3: "))
    linha_matriz.append(num)

    if len(linha_matriz) == 3:
        matriz.append(linha_matriz)
        linha_matriz = []

print('\nMatriz 3x3')
for l in matriz:
    print(l)