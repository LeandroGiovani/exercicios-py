gastos = [{
        "index": 1,
        "nome": "Gasolina",
        "gasto": "20.00",
    }]

receitas = [{
        "index": 1,
        "nome": "Salário",
        "receita": "2000.00",
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
            viewReceitas()
            receitaMenu()
        case 2:
            proximoId = len(receitas) + 1
            nomeR = input("Nome da receita: ")
            valorR = float(input("Valor da receita: "))

            novo_item = {
                "index": proximoId,
                "nome": nomeR,
                "receita": f"{valorR:.2f}",
            }

            receitas.append(novo_item)
            print("\n✅ Receita adicionada!")
            receitaMenu()
        case 3:
            viewReceitas()

            idDel = int(input("Id do item que deseja remover: "))

            for r in receitas:
                receitas.pop(r["index"] == (idDel - 1))
            
            print("Receita removida")
            receitaMenu()
        case 4:
            viewReceitas()

            idAtt = int(input("Id do item que deseja remover: "))
            newNome = input("Novo nome da receita: ")
            newReceita = float(input("Novo valor da receita: "))

            for r in receitas:
                if r["index"] == idAtt:
                    r["nome"] = newNome
                    r["receita"] = f"{newReceita:.2f}"

            print("Atualização feita!")
            receitaMenu()
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

def viewReceitas():
    print(f"""
{"=" * 35}
{"RECEITAS TABELA":^35}
{"=" * 35}
""")
    for r in receitas:
        print(f"{r['index']}. {r['nome']}: {r['receita']}")
    print("=" * 35 + "\n")

init()