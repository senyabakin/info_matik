# TODO решите задачу
import json#импортируем модуль json
def task() -> float:#задаем функцию без аргументов
    FILENAME = "input.json"
    with open(FILENAME) as f:
        json_data = json.load(f)#задаем функцию, читающую json файл
    sum_ = sum([item["score"] * item["weight"] for item in json_data])#вычисляем сумму произведений для переменной по ключам "score" и "weight" и помещаем их в новый список
    return round(sum_, 3)#округляем до 3ех знаков после запятой
print(task())#распечатываем полученную сумму
