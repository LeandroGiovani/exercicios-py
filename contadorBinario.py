import time

cont = 0

def convertToBin(num):
    if num == 0:
        return "0"
    bin_result = ""
    while num > 0:
        bin_result = str(num % 2) + bin_result
        num = num // 2
    return bin_result

while True:
    time.sleep(0.5)
    print(f"{cont} {convertToBin(cont)}")
    cont += 1
