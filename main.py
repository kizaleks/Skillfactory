
import random

#Создаем поле
maps=["-","-","-","-","-","-","-","-","-"]
#Создаем пустой список доступных ходов
motion_f=[]
#Функция вывода поля
def print_maps ():
    print("   0 1 2")
    print("0 ", maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])
    print("1 ", maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])
    print("2 ",maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])
#Функция проверки выигрыша
def winner (sumbol):
    #Проверка горизонтальных линий
    if maps[0]==sumbol and maps[1]==sumbol and maps[2]==sumbol:
        return True
    elif maps[3]==sumbol and maps[4]==sumbol and maps[5]==sumbol:
        return True
    elif maps[6]==sumbol and maps[7]==sumbol and maps[8]==sumbol :
        return True
    elif maps[0]==sumbol and maps[3]==sumbol and maps[6]==sumbol :
        return True
    elif maps[1]==sumbol and maps[4]==sumbol and maps[7]==sumbol :
        return True
    elif maps[2]==sumbol and maps[5]==sumbol and maps[8]==sumbol :
        return True
    elif maps[0]==sumbol and maps[4]==sumbol and maps[8]==sumbol:
        return True
    elif maps[2]==sumbol and maps[4]==sumbol and maps[6]==sumbol:
        return True
    else:
        return False
#Функция проверки обязательного хода
def mandatory_motion (sumbol):
    resultat=True
    if maps[0:3] == ["-", sumbol, sumbol] or maps[0::3] == ["-", sumbol, sumbol] or maps[0::4] == ["-", sumbol, sumbol]:
        return [resultat, 0]
    elif maps[0:3] == [sumbol, "-", sumbol] or maps[1::3] == ["-", sumbol, sumbol]:
        return [resultat, 1]
    elif maps[0:3] == [sumbol,sumbol,"-"] or maps[2::3] == ["-", sumbol, sumbol] or maps[2:7:2] == ["-", sumbol, sumbol]:
        return [resultat, 2]
    elif maps[3:6] == ["-", sumbol, sumbol] or maps[0::3] == [sumbol, "-", sumbol]:
        return [resultat, 3]
    elif maps[3:6] == [sumbol, "-", sumbol] or maps[1::3] == [sumbol, "-", sumbol] or maps[0::4] == [sumbol, "-", sumbol] or maps[2:7:2] == [sumbol, "-", sumbol]:
        return [resultat, 4]
    elif maps[3:6] == [sumbol, sumbol,"-"] or maps[2::3] == [sumbol, "-", sumbol]:
        return [resultat, 5]
    elif maps[6:9]==["-", sumbol, sumbol] or maps[0::3] == [sumbol, sumbol, "-"] or maps[2:7:2] == [sumbol, sumbol, "-"]:
        return [resultat, 6]
    elif maps[6:9]==[ sumbol,"-", sumbol] or maps[1::3] == [sumbol, sumbol, "-"]:
        return [resultat, 7]
    elif maps[6:9] == [sumbol, sumbol, "-"] or maps[2::3] == [sumbol, sumbol, "-"] or maps[0::4] == [sumbol, sumbol, "-"]:
        return [resultat, 8]
    else:
        return [False, 0]
#Функция построения списка доступных ходов
def motion_free():
    motion_f[:]=[]
    for n in range(9):
        if maps[n]=="-":
            motion_f.append(n)
    return motion_f
#Функция выбора хода
def motion(sumbol_pl):
    if len(motion_f)==9:
        return [True, 0]
    elif len(motion_f)==8:
       if maps[0]==sumbol_pl or maps[2]==sumbol_pl or maps[6]==sumbol_pl or maps[8] ==sumbol_pl:
            return [True, 4]
       else:
           return [True, 0]
    elif len(motion_f)==7:
        if maps[4]==sumbol_pl:
            return [True, 8]
        elif maps[2]==sumbol_pl or maps[6]==sumbol_pl :
            return [True, 8]
        elif maps[8] ==sumbol_pl:
            return [True, 2]
        elif maps[1] =="-" and maps[2] =="-" :
            return [True, 2]
        elif maps[3] =="-" and maps[6] =="-" :
            return [True, 6]
        else:
            return [True, 4]
    elif len(motion_f)==6:
        random.shuffle(motion_free())
        return [True, motion_f[0]]
    elif len(motion_f)==5:
        if maps[4] =="-":
            return [True, 4]
        else:
            return [True, 6]

    else:
        random.shuffle(motion_free())
        return [True, motion_f[0]]

sumbol_pl="0"
sumbol_pk="X"
#Выбор уровня сложности
while True:
    print("Выберите уровень сложности:")
    print("1 Легко")
    print("2 Сложно")
    print("3 Непобедимый")
    level=int(input("Введите число"))
    if level==1 or level==2 or level==3:
        break
    else: print("Неправильный выбор")
#Случайный выбор кто ходит первым
first=random.randint(1,2)%2
if first:print("Компьютер ходит первым")
else:print("Игрок ходит первым")

#Основной код программы
while True:
    if first:
        motion_free()
        temp_list=mandatory_motion(sumbol_pk)
        if temp_list[0] and level>1 :
            maps[temp_list[1]]=sumbol_pk
            print_maps()
        else:
            temp_list[:]=[]
            temp_list=mandatory_motion(sumbol_pl)
            if temp_list[0] and level>1:
                maps[temp_list[1]] = sumbol_pk
                print_maps()
            else:
                if level==3:
                    temp_list[:] = []
                    temp_list = motion(sumbol_pl)
                    maps[temp_list[1]] = sumbol_pk
                elif level==2:
                    random.shuffle(motion_free())
                    maps[motion_f[0]] = sumbol_pk
        if level==1:
            random.shuffle(motion_free())
            maps[motion_f[0]] = sumbol_pk
    first=1

    if winner(sumbol_pk):
        print("Компьютер победил")
        break
    elif len(motion_free())==0:
        print("Ничья")
        break
    print_maps()
    while True:
        i, j=int(input("Введите номер столбца")), int(input("Введите номер строки"))
        if i<=2 or j<=2:
            if maps[i+3*j]!="-":
                print("Поле уже занято")
            else:
                maps[int(i+3*j)] = sumbol_pl
                break
        else:  print("Введено недопустимое значение")
    if winner(sumbol_pl):
        print("Игрок победил")
        break
    elif len(motion_free()) == 0:
        print_maps()
        print("Ничья")
        break

