import random
import allure

def discount_3_percent():
    with allure.step("discount_3_percent"):
        # задаем выбор рандомного значения в указанных пределах
        bonus_points = random.randint(100, 199)
        print("Количество баллов: " + str(bonus_points))

        # задаем условие применения скидки 3%
        if bonus_points >= 100 and bonus_points < 200:
            discount = 0.03
            print("Скидка составляет: " + str(discount*100) + " %")
