# TODO Напишите функцию для поиска индекса товара
def z(items_list, find_item):#зададим функцию и ее аргументы
    for index in range(len(items_list)):#перебираем все возможные индексы до длины списка
        if items_list[index] == find_item:#условие если товар присутствует в списке
            return index#возвращаем индекс
    return None#если товар не найден в списке возвращаем None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = z(items_list, find_item)  # вызовем функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
