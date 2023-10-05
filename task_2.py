# Напишите функцию принимающую на вход только ключевые параметры и
# возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем, используйте его
# строковое представление. reverse_kwargs(rev=True, acc="YES", stroka=4) ->
# {True: "rev", "YES": 'acc', 4: "stroka"}


def reverse_kwargs(**kwargs) -> dict:
    '''Функция принимающая на вход только ключевые параметры и
# возвращающая словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента'''
    result = {}
    for key, value in kwargs.items():
        if hash(value):
            result[value] = key
        else:
            result[str(value)] = key
    return result


print(reverse_kwargs(rev=True, acc="YES", stroka=4))
