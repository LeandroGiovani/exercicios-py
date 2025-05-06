def calcular_matriz(matriz):
    ordem_matriz = len(matriz)

    match ordem_matriz:
        case 1:
            print(matriz[0][0])
        case 2:
            print(
                matriz[0][0] * matriz[1][1]
                - matriz[0][1] * matriz[1][0]
            )
        case 3:
            print(
                  matriz[0][0] * matriz[1][1] * matriz[2][2]
                + matriz[0][1] * matriz[1][2] * matriz[2][0] 
                + matriz[0][2] * matriz[1][0] * matriz[2][1] 
                - matriz[0][2] * matriz[1][1] * matriz[2][0] 
                - matriz[0][0] * matriz[1][2] * matriz[2][1] 
                - matriz[0][1] * matriz[1][0] * matriz[2][2]
            )
        case _:
            print('Erro')

matriz1 = [[1]]
matriz2 = [[1, 2], [4, 3]]
matriz3 = [[7, 2, 1], [4, 3, 9], [8, 2, 1]]

calcular_matriz(matriz1)
calcular_matriz(matriz2)
calcular_matriz(matriz3)