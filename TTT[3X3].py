def value(x):
    if x == -1:
        return "1️⃣"
    if x == -2:
        return "2️⃣"
    if x == -3:
        return "3️⃣"
    if x == -4:
        return "4️⃣"
    if x == -5:
        return "5️⃣"
    if x == -6:
        return "6️⃣"
    if x == -7:
        return "7️⃣"
    if x == -8:
        return "8️⃣"
    if x == -9:
        return "9️⃣"
    if x == 2:
        return "⭕️"
    if x == 3:
        return "❌"

sec = []
def result(sec):
    if ((sec[0] == sec[1] == sec[2] == 2) or
            (sec[3] == sec[4] == sec[5] == 2) or
            (sec[6] == sec[7] == sec[8] == 2) or
            (sec[0] == sec[3] == sec[6] == 2) or
            (sec[1] == sec[4] == sec[7] == 2) or
            (sec[2] == sec[5] == sec[8] == 2) or
            (sec[0] == sec[4] == sec[8] == 2) or
            (sec[2] == sec[4] == sec[6] == 2)):
        return ("Вы проиграли!")
    elif((sec[0] == sec[1] == sec[2] == 3) or
            (sec[3] == sec[4] == sec[5] == 3) or
            (sec[6] == sec[7] == sec[8] == 3) or
            (sec[0] == sec[3] == sec[6] == 3) or
            (sec[1] == sec[4] == sec[7] == 3) or
            (sec[2] == sec[5] == sec[8] == 3) or
            (sec[0] == sec[4] == sec[8] == 3) or
            (sec[2] == sec[4] == sec[6] == 3)):
        return ("Вы победили!")
    else:
        return ("Ничья!")


key = 0
sec = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
choice = [0, 0, 0, 0, 0, 0, 0, 0, 0]
priority_move = []
priority_summ = []
w_key = 0


def nous(x):
    nous_xod = sec[x]
    sec[x] = 3
    if ((sec[0] == sec[1] == sec[2]) == True or
            (sec[3] == sec[4] == sec[5]) == True or
            (sec[6] == sec[7] == sec[8]) == True or
            (sec[0] == sec[3] == sec[6]) == True or
            (sec[1] == sec[4] == sec[7]) == True or
            (sec[2] == sec[5] == sec[8]) == True or
            (sec[0] == sec[4] == sec[8]) == True or
            (sec[2] == sec[4] == sec[6]) == True):
        sec[x] = nous_xod
        priority_move.append(x)
        priority_summ.append(4)
        return 2
    sec[x] = 2
    if ((sec[0] == sec[1] == sec[2]) == True or
            (sec[3] == sec[4] == sec[5]) == True or
            (sec[6] == sec[7] == sec[8]) == True or
            (sec[0] == sec[3] == sec[6]) == True or
            (sec[1] == sec[4] == sec[7]) == True or
            (sec[2] == sec[5] == sec[8]) == True or
            (sec[0] == sec[4] == sec[8]) == True or
            (sec[2] == sec[4] == sec[6]) == True):
        sec[x] = nous_xod
        priority_move.append(x)
        priority_summ.append(5)
        return 2
    sec[x] = nous_xod
    if x == 4 and sec[4] < 0:
        priority_move.append(x)
        priority_summ.append(3)
        return 2
    if x % 2 == 0 and sec[x] < 0:
        priority_move.append(x)
        priority_summ.append(2)
        return 2


print("||||||||||||||||||||||||||\n||\t||\t||\t||\n||",
      value(sec[0]), "\t||", value(sec[1]),"\t||", value(sec[2]),
      "\t||\n||\t" "||\t" "||\t" "||\n||||||||||||||||||||||||||\n||\t" "||\t" "||\t" "||\n||",
      value(sec[3]), "\t||", value(sec[4]), "\t||", value(sec[5]),
      "\t||\n||" "\t||" "\t||" "\t||\n||||||||||||||||||||||||||\n||" "\t||" "\t||" "\t||\n||",
      value(sec[6]), "\t||", value(sec[7]), "\t||", value(sec[8]),
      "\t||\n||" "\t||" "\t||" "\t||\n||||||||||||||||||||||||||")

while (((sec[0] != sec[1]) or (sec[1] != sec[2])) and ((sec[3] != sec[4]) or (sec[4] != sec[5])) and
       ((sec[6] != sec[7]) or (sec[7] != sec[8])) and
       ((sec[0] != sec[3]) or (sec[3] != sec[6])) and ((sec[1] != sec[4]) or (sec[4] != sec[7])) and
       ((sec[2] != sec[5]) or (sec[5] != sec[8])) and
       ((sec[0] != sec[4]) or (sec[4] != sec[8])) and ((sec[2] != sec[4]) or (sec[4] != sec[6]))) and key == 0:
    while w_key == 0:
        print("Введите номер ячейки для хода: ")
        move = int(input()) - 1
        if move in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            if choice[move] == 0:
                sec[move] = 3
                choice[move] = 1
                w_key = 1
    i = -1
    key = 0
    w_key = 0

    while key == 0 and i < 8:
        i += 1
        if choice[i] == 0:
            nous(i)
    if 0 in choice:
        max_value = max(priority_summ)
        max_index = priority_summ.index(max_value)
        sec[priority_move[max_index]] = 2
        choice[priority_move[max_index]] = 1
        priority_move.clear()
        priority_summ.clear()
    else:
        key = 1
    print("||||||||||||||||||||||||||\n||\t||\t||\t||\n||",
      value(sec[0]), "\t||", value(sec[1]),"\t||", value(sec[2]),
      "\t||\n||\t" "||\t" "||\t" "||\n||||||||||||||||||||||||||\n||\t" "||\t" "||\t" "||\n||",
      value(sec[3]), "\t||", value(sec[4]), "\t||", value(sec[5]),
      "\t||\n||" "\t||" "\t||" "\t||\n||||||||||||||||||||||||||\n||" "\t||" "\t||" "\t||\n||",
      value(sec[6]), "\t||", value(sec[7]), "\t||", value(sec[8]),
      "\t||\n||" "\t||" "\t||" "\t||\n||||||||||||||||||||||||||")
print(result(sec))
