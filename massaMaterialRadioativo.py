massa = 10
tempo = 0
segundos = 0
minutos = 0
horas = 0

while True:
    massa /= 2
    tempo += 50
    if massa == 0.3125:
        print(tempo)
        horas = tempo/3600
        minutos = (tempo % 3600)/60
        segundos = tempo % 60
        print(f"horas:{horas},{minutos},{segundos}")

    
    