wins = [7495938, 1223125, 2128437, 4567890, 2128500, 2741001, 9314543, 4567687]
my_ticket = 2128506


def check_element_in_unordered_list(desired_element, unordered_list):
    """Проверяет наличие заданного элемента в неотсортированном списке."""
    # Итерируемся по списку.
    for item in unordered_list:
        # Каждый элемент сверяем с искомым.
        if item == desired_element:
            # Если элемент найден, то возвращаем значение True.
            return True
    # Если цикл прошёл, а элемент не найден, возвращаем False.
    return False


# Если функция вернула True...
if check_element_in_unordered_list(my_ticket, wins):
    # ...печатаем сообщение:
    print(f'Элемент {my_ticket} найден в списке!')
else:
    # Если функция вернула False - тоже сообщаем об этом.
    print(f'Элемент {my_ticket} не найден в списке.')

#****************************************************************************
# Функция enumerate()
    
def find_element_index_in_unordered_list(desired_element, unordered_list):
    """
    Находит индекс первого вхождения искомого элемента 
    в неотсортированном списке.
    """
    # Применяем к списку функцию enumerate(), итерируемся
    # по полученному объекту enumerate и распаковываем его кортежи:
    # в переменную index сохраняем индекс элемента, в item - его значение.
    for index, item in enumerate(unordered_list):
        # Если значение текущего элемента равно искомому...
        if item == desired_element:
            # ...возвращаем его индекс:
            return index
    # Если цикл пройден, но нужное значение не найдено,
    # то возвращаем None. 
    # Явно возвращать None не обязательно, эту строку можно вообще не писать:
    # если в функции нет оператора return, она возвращает None.
    return None


wins = [7495938, 1223125, 2128437, 4567890, 2128500, 2741001, 9314543, 4567687]
my_ticket = 2128506
result = find_element_index_in_unordered_list(my_ticket, wins)
if result is not None:
    print(f'Индекс элемента {my_ticket} в массиве: {result}')
else:
    print(f'Элемент {my_ticket} не найден в массиве.')



# Эта же задача без enumerate():

def find_element_index_in_unordered_list(desired_element, unordered_list):
    """
    Находит индекс первого вхождения искомого элемента 
    в неотсортированном списке.
    """
    # Формируем цикл с количеством шагов, равным длине списка.
    for index in range(len(unordered_list)):
        # Берём элемент из списка по его индексу.
        if unordered_list[index] == desired_element:
            return index
    return None 
#****************************************************************************
# выполняет линейный поиск по любому массиву

def check_element_in_list(desired_element, ordered_list):
    """Проверяет наличие искомого элемента в отсортированном списке."""
    for item in ordered_list:
        if item == desired_element:
            return f'Элемент {desired_element} найден в массиве!'
        elif item < desired_element:
            continue
        elif item > desired_element:
            break
    return f'Элемент {desired_element} не найден в массиве.'


# Вызываем функцию с тестовыми данными.
# Первый аргумент - целое число.
# Второй аргумент - отсортированный по возрастанию список целых чисел.
result = check_element_in_list(5, [1, 3, 5, 7, 10])
# Распечатываем результат.
print(result)