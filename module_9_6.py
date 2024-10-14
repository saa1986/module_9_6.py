"""Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
Пример результата выполнения программы:
Пример работы функции:
a = all_variants("abc")
for i in a:
print(i)
Вывод на консоль:
a
b
c
ab
bc
abc

Примечания:
Для функции генератора используйте оператор yield."""
"""def all_variants(text):
    for i in range(1, len(text) + 1):
        for j in range(len(text) - i + 1):
            yield text[j:j+i]

a = all_variants("abc")
for i in a:
    print(i)"""
def all_variants(text):
    # Проходим по всем возможным начальным индексам
    for start in range(len(text)):
        # Проходим по всем возможным конечным индексам
        for end in range(start + 1, len(text) + 1):
            # Возвращаем подпоследовательность с помощью yield
            yield text[start:end]

# Пример использования
a = all_variants("abc")  # Создаем генератор

# Итерация по всем подпоследовательностям
for i in a:
    print(i)  # Печатаем каждую подпоследовательность