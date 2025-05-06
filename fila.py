class Execucao:
    def contar_ate_10():
        for i in range(10):
            print(i)


    def contar_ate_20():
        for i in range(10):
            print(i)


    def contar_ate_30():
        for i in range(10):
            print(i) 
    


class Fila:
    def __init__(self):
        self.fila = []

    def adicionar_na_fila(self, elemento:int): 
        self.fila.append(elemento)


    def remover_da_fila(self):
        if self.vazia():
            print("Fila vazia")
        else:
            # ultimo_index = len(self.fila)
            self.fila.pop(0)


    def vazia(self):
        return len(self.fila) == 0

    def mostrar_fila(self):
        for i in self.fila:
            print(i)

    def inverter_fila(self):
        fila_auxiliar = []
        ultimo_index = len(self.fila)-1
        print(f"ultimo index: {ultimo_index}")
        for i in range(ultimo_index, -1, -1): ##começa em 102 e temrna antes do index 0
            print(f"index inicial {ultimo_index}")
            print(f"valor na lista principal: {self.fila[i]}")
            valor = self.fila[i]
            print(f"valor: {valor}")
            fila_auxiliar.append(self.fila[i])
            ultimo_index = ultimo_index-1
            print(f"Proximo index:{ultimo_index}")
            print(fila_auxiliar) 

    def executar_fila(self):
        while not self.vazia():
            func = self.remover_da_fila()  # Retira a função da fila
            return func()  # Executa a função retirada

    
fila = Fila()
execucao = Execucao()
fila.adicionar_na_fila(execucao.contar_ate_10)
fila.adicionar_na_fila(execucao.contar_ate_20)
fila.adicionar_na_fila(102)
# #fila.mostrar_fila()


# #fila.remover_da_fila()
fila.mostrar_fila()
# fila.inverter_fila()
# fila.inverter_fila()

fila.executar_fila()