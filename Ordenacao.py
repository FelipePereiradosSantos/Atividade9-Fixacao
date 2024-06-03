list = []

for i in range(10):
    num = int(input(f"Insira o número:\n"))

    list.append(num)

list = sorted(list)

print(f"A lista de números ordenada é:\n{list}")