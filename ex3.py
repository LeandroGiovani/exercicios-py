#nome ra idade
alunos = []
#ra prova nota
notas = []

for i in range(1, 4):
    ra = int(input(f"RA do aluno {i}: "))
    nome = input(f"Nome do aluno {i}: ")
    idade = int(input(f"Idade do aluno {i}: "))
    aluno = [nome, ra, idade]
    alunos.append(aluno)
    print(f"Aluno {i} adicionado!\n")

print(f"Tabela alunos\n{alunos}")

for a in alunos:
    print(f"\nAdicione as notas do aluno RA {a[1]}")
    for i in range(1, 5):
        n = float(input(f"Nota prova {i}: "))
        prova = f"p{i}"
        nota = [a[1], prova, n]
        notas.append(nota)

print(f"Tabela notas\n{notas}")

print(f"\nMédia alunos")
for a in alunos:
    qtd_notas = 0
    soma = 0
    for n in notas:

        if a[1] == n[0]:
            qtd_notas += 1
            soma += n[2]

    media = soma / qtd_notas
    print(f"Média do aluno {a[1]}: {media}")