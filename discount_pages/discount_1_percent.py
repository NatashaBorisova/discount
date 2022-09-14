import random
import allure


def discount_1_percent():
    with allure.step("discount_1_percent"):
        # задаем выбор рандомного значения в указанных пределах
        bonus_points = random.randint(0, 99)
        print("Количество баллов: " + str(bonus_points))

        # задаем условие применения скидки 1%
        if bonus_points >= 0 and bonus_points < 100:
            discount = 0.01
            print("Скидка составляет: " + str(discount*100) + " %")
