# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные
# операции — функции. Дополнительно сохраняйте все операции поступления
# и снятия средств в список.

s = 10000
count = 0
RICHLIMIT = 5_000_000
RICHTAX = 0.9
THREEOPERATIONS = 3
BONUSTHREE = 1.03
FREENDERING = 50
COMMISSIONOUTDROW = 0.015
MINLIMIT = 30
MAXLIMIT = 600


def replenishment_card(withdrow):
    if withdrow % FREENDERING == 0:
        count += 1
        s += withdrow
    return s


def withdrawal_card(withdrow):
    if withdrow % FREENDERING == 0:
        comission = withdrow * COMMISSIONOUTDROW
        if comission < MINLIMIT:
            comission = MINLIMIT
        elif comission > MAXLIMIT:
            comission = MAXLIMIT
        if (comission + withdrow) < s:
            s -= (withdrow + comission)
            count += 1
    return s


def coun_card(s):
    if s >= RICHLIMIT:
        s *= RICHTAX
    if count % THREEOPERATIONS == 0 and count != 0:
        s *= BONUSTHREE
        count = 0
    return count


while True:
    action = input(
        'Введите операцию\n 1 - Пополнение \n 2 - Снятие \n 3 - Выйти:\n ')
    coun_card (s)
    if action == '1':
        withdrow = int(input('введиет сумму: '))
        replenishment_card(withdrow)
    elif action == '2':
        withdrow = int(input('введиет сумму: '))
        withdrawal_card(withdrow)
    else:
        break
print(f'Ваш баланс равен {s}\n Спасибо! Приходите еще!')
