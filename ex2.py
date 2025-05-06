matriz = []

for l in range(5):
    linha = []
    for c in range(5):
        num = int(input(f"Número [{l}][{c}] da matriz 5x5: "))
        linha.append(num)
    matriz.append(linha)

print('\nMatriz 5x5')
for l in matriz:
    print(l)

soma = 0
for i in range(len(matriz)):
    soma += matriz[i][i]
print(soma)