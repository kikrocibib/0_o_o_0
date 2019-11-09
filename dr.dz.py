answer = input("Введите колличество элементов: ")
ggg = 0
answer = int(answer)
l = []
while answer > ggg:
    bbb = input("Введите цифру: ")
    bbb = int(bbb)
    l.append(bbb)
    ggg = ggg + 1
l = sorted(l)
print(l) # [1, 2, 3]
