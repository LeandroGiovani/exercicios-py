idade = int(input("Inisira sua idade: "))
carteira = input("Possui carteira? (y/n): ").lower()

if idade >= 18 and carteira == 'y':
    print("S")
else:
    print("N")