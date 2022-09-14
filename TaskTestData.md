# Набор тестовых данных для автомата 

набор тестовых данных для автомата, при котором мы гарантированно будем знать, что в соответствии со своими накопленными баллами покупатель получит верную скидку.


## Применяемые техники

- Эквивалентное разделение
- Анализ граничных значений


! Важно установить правильные диапазоны значений

> В задании некорректно указаны значения 
> для применеия скидки (например,
> значение "100" указано как в условии для скидки
> в 1%, так и в условии для скидки 3%).
> При выполнении тестов будем опираться
> на следующие условия:
> 0 - 99 баллов - скидка 1%
> 100 - 199 баллов - скидка 3%
> 200 - 499 баллов - скидка 5%
> 500 и более баллов - скидка 10%

При выполнении тестов будем опираться на следующие условия:
- 0 - 99 баллов - скидка 1%
- 100 - 199 баллов - скидка 3%
- 200 - 499 баллов - скидка 5%
- 500 и более баллов - скидка 10%



| Условие | Значения |
| ------ | ------ |
| Проверка применения скидки в диапазоне 0 - 99 | 0, 1, 15, 98, 99 |
| Проверка применения скидки в диапазоне 100 - 199 | 100, 101, 138, 198, 199 |
| Проверка применения скидки в диапазоне 200 - 499 | 200, 201, 378, 498, 499 |
| Проверка применения скидки от 500 и выше | 500, 501, 732 |
