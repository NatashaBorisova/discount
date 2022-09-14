import random
import allure

def discount_10_percent():
    with allure.step("discount_10_percent"):
        # задаем выбор рандомного значения в указанных пределах
        bonus_points = random.randint(500, 10000)
        print("Количество баллов: " + str(bonus_points))

        # задаем условие применения скидки 10%
        if bonus_points >= 500:
            discount = 0.10
            print("Скидка составляет: " + str(discount*100) + " %")
