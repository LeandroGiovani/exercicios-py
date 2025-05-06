
class ListaDeOnibus:
    def __init__(self):
        self.menu = print("""
        Seja bem vindo a lista de onibus
        --------------------------------
        [1]Adicionar Aluno
        [2]Remover Aluno
        [3]Mostrar todos os alunos
        [4]Quantidade de alunos
        [5]Sair

    """)
        
        self.lista = []

    def __add_aluno(self, input: str):
        self.input = input
        for i in self.lista:
            if i == self.input:
                print("Aluno Existente")
                break
            else:
                self.lista.append(self.input)
                print("Aluno adicionado")
                break

    def __remove_aluno(self, input:str):
        self.input = input
        for i in self.lista:
            if i == self.input:
                print("Aluno Existente, removendo")
                self.lista.remove(self.input)
            else:
                print("Aluno Não encontrado")
                break
    

    def __quantidade_alunos(self):
        index = 0
        for i in self.lista:
            index = index+1
        print(f"Quantidade de alunos {index}")

    def __print_alunos(self):
        for i in self.lista:
            print(i)

    def main(self, input:int)40:
        match(self.input):
            case 1:
                

            case 2:
                user_second_input = str(input("Digite o nome do aluno para remover"))
                for i in alunos:
                    if i == user_input:
                        alunos.remove(user_second_input)
                        print("Aluno encontrado e removido")
                        break
                    else:
                        print("Aluno Não encontrado")
                        break
    
            case 3:
                for i in alunos:
                    print(i)
             
            case 4:
                index_list = 0
                for i in alunos:
                    index_list = index_list+1
                print(f"Tem {i} pessoas")

            case 5:
                pass
            case _:
                pass
        

    


def menu():
    print("""
        Seja bem vindo a lista de onibus
        --------------------------------
        [1]Adicionar Aluno
        [2]Remover Aluno
        [3]Mostrar todos os alunos
        [4]Quantidade de alunos
        [5]Sair

    """)

alunos = []



while(True):
    menu()
    user_input = int(input("Digite sua seleção"))
    match(user_input):
        case 1:
            user_second_input = str(input("Digite o nome do aluno para adicionar"))
            # alunos.append(user_second_input)
            for i in alunos:
                        if i == user_input:
                            print("Aluno Existente")
                            break
                        else:
                            alunos.append(alunos)
                            print("Aluno adicionado")
                            break

        case 2:
            user_second_input = str(input("Digite o nome do aluno para remover"))
            for i in alunos:
                if i == user_input:
                    alunos.remove(user_second_input)
                    print("Aluno encontrado e removido")
                    break
                else:
                    print("Aluno Não encontrado")
                    break
    
        case 3:
            for i in alunos:
                 print(i)
             
        case 4:
            index_list = 0
            for i in alunos:
                 index_list = index_list+1
            print(f"Tem {i} pessoas")

        case 5:
             break
        case _:
             break
         
        
        
                
                    


