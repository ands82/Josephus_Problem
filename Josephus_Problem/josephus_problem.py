# Задача Иосифа Флавия

n, k = int(input()), int(input())
l_n = [i for i in range(1, n + 1)]
while len(l_n) > 1:
    for _ in range(k - 1):
        l_n.append(l_n[0])
        del l_n[0]
    del l_n[0]
print(*l_n)
