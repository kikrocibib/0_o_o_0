import numpy as np
import random
l = [["Эйнштейн", "1879"],["Распутин", "1937"],["Попов","1859"],["Бертолуччи","1941"],["Рассел","1951"],["Вуди","1935"],["Глинка","1913"],["Федосеенко","1934"],["Цвет","1918"],["Жигулин","1930"]]
m = []
ggg = 0
vvv = 0

while 5 > ggg:
    rnum = np.random.randint(len(l))
    m.append(l[rnum])
    del l[rnum]
    ggg = ggg + 1
    print(l)
    print(m)

ggg = 0

while len(m) > ggg:
    answer = input("Когда родился " +m[ggg][0])
    if answer == m[ggg][1]:
        vvv = vvv + 1
        print("True")

    else:
        print(m[ggg][1])
    ggg = ggg + 1

print("Правильные ответы:" + str(vvv))
print("Неправильные ответы:",len(m) - vvv)
print("Процент правельных ответов:", vvv * 100 / len(m))
print("Процент неправельных ответов:", 100 - vvv * 100 / len(m))