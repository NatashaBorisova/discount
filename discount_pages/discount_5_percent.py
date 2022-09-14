import random
import allure

def discount_5_percent():
    with allure.step("discount_5_percent"):
        # задаем выбор рандомного значения в указанных пределах
        bonus_points = random.randint(200, 499)
        print("Количество баллов: " + str(bonus_points))

        # задаем условие применения скидки 5%
        if bonus_points >= 200 and bonus_points < 500:
            discount = 0.05
            print("Скидка составляет: " + str(discount*100) + " %")
