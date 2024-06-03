list = []
par = []

for i in range(10):
    num = int(input(f"Insira o número:\n"))

    list.append(num)

for i in list:

    if (i % 2 == 0):
        par.append(i)
    else:
        pass

par = sorted(par)

print(f"A lista de números pares é:\n{par}")