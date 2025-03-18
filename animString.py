import time

string = 'OLÁ EU SOU O JAPA'
num = 0
newString = ''

for ch in string:
    while num <= 9:
        print(f"{newString}" +  f"{num}")
        num += 1
        time.sleep(0.02)
    num = 0
    newString += ch
    print(newString)
print('\n')