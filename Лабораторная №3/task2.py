# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, sep=','):#зададим функцию, где 2 аргумента отвечают за участников, а третий за разделение
    first_group_list = group1.split(sep)#разбиваем строку на списки
    second_group_list = group2.split(sep)#разбиваем строку на списки
    first_group_set = set(first_group_list)#разбиваем список на множество
    second_group_set = set(second_group_list)#разбиваем список на множество
    both_groups_set = first_group_set.intersection(second_group_set)#ищем общее кол-во участников среди 2ух групп
    return sorted(both_groups_set)#сортируем участников в алфавитном порядке

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


