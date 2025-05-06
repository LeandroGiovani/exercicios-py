vetor = []


for i in range(10):
    user_value = int(input("Digite o numero"))
    vetor.append(user_value)
    

for i in vetor:
    if vetor[i] > i:
        menor_valor = i
        posicao_maior = i
    if i > vetor[i]:
        maior_valor = i
        posicao_menor = i



# for j in vetor:
#     if j == menor_valor:
#         print(vetor[i])
#     if j == maior_valor:
#         print(vetor[i])

print(menor_valor)
print(posicao_maior)
print(maior_valor)
print(posicao_menor)