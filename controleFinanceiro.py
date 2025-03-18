gastos = [{
        "index": 1,
        "nome": "Gasolina",
        "gasto": "20.00",
    }]

def init():
    print(f"""
{"=" * 35}
{"CONTROLE FINANCEIRO":^35}
{"=" * 35}
[1] - Gasto
[2] - Receita
[3] - Sair
{"=" * 35}
""")
    escolha = int(input("Digite o valor correspondente: "))
    match escolha:
        case 1:
            gastoMenu()
        case 2:
            receitaMenu()
        case 3:
            print("\nSaindo...\n")
        case _:
            print("\n❌ Valor inserido inválido. Tente novamente")

def gastoMenu():
    print(f"""
{"=" * 35}
{"GASTOS":^35}
{"=" * 35}
[1] - Visualizar Gasto
[2] - Adicionar Gasto
[3] - Remover Gasto
[4] - Atualizar Gasto
[5] - Voltar
{"=" * 35}
""")
    escolha = int(input("Digite o valor correspondente: "))

    match escolha:
        case 1:
            viewGastos()
            gastoMenu()

        case 2:
                proximoId = len(gastos) + 1
                nomeG = input("Nome do gasto: ")
                valorG = float(input("Valor do gasto: "))

                novo_item = {
                    "index": proximoId,
                    "nome": nomeG,
                    "gasto": f"{valorG:.2f}",
                }

                gastos.append(novo_item)
                print("\n✅ Gasto adicionado!")
                gastoMenu()
        case 3:
            viewGastos()

            idDel = int(input("Id do item que deseja remover: "))

            for g in gastos:
                gastos.pop(g["index"] == (idDel - 1))
            
            print("Gasto removido")
            gastoMenu()
        case 4:
            viewGastos()

            idAtt = int(input("Id do item que deseja remover: "))
            newNome = input("Novo nome do gasto: ")
            newGasto = float(input("Novo valor do gasto: "))

            for g in gastos:
                if g["index"] == idAtt:
                    g["nome"] = newNome
                    g["gasto"] = f"{newGasto:.2f}"

            print("Atualização feita!")
            gastoMenu()
        case 5:
            init()
        case _:
            print("\n❌ Valor inserido inválido. Tente novamente")
            gastoMenu()

def receitaMenu():
    print(f"""
{"=" * 35}
{"RECEITAS":^35}
{"=" * 35}
[1] - Visualizar Receita
[2] - Adicionar Receita
[3] - Remover Receita
[4] - Atualizar Receita
[5] - Voltar
{"=" * 35}
""")
    escolha = int(input("Digite o valor correspondente: "))
    match escolha:
        case 1:
            print("Teste")
        case 2:
            print("Teste")
        case 3:
            print("Teste")
        case 4:
            print("Teste")
        case 5:
            init()
        case _:
            print("\n❌ Valor inserido inválido. Tente novamente")
            receitaMenu()

def viewGastos():
    print(f"""
{"=" * 35}
{"GASTOS TABELA":^35}
{"=" * 35}
""")
    for g in gastos:
        print(f"{g['index']}. {g['nome']}: {g['gasto']}")
    print("=" * 35 + "\n")

init()