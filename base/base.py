
def bonus():

    # для проверки с помощью ручного ввода значения

    print("Считываю количество баллов")
    points = int(input())
    # points = random.randint(0, 5000)
    print("Количество баллов : " + str(points))

    # задаем условия применения скидки

    if points >= 0 and points <= 99:
        discount = 0.01
        print("Ваша скидка составляет " + str(discount*100) + " %")

    if points >= 100 and points <= 199:
        discount = 0.03
        print("Ваша скидка составляет " + str(discount*100) + " %")

    if points >= 200 and points <= 499:
        discount = 0.05
        print("Ваша скидка составляет " + str(discount*100) + " %")

    if points >= 500:
        discount = 0.1
        print("Ваша скидка составляет " + str(discount*100) + " %")


bonus()