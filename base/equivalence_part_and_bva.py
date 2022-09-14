import allure

def bonus():
    with allure.step("Bonus"):

        # задаем список значений (эквивалентное разделение и граничные значения)
        values = [0, 1, 15, 98, 99, 100, 101, 138, 198, 199, 200, 201, 376, 498, 499, 500, 501, 732]
        for points in values:
            print("Количество баллов " + str(points))

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
