import json
import os

file_path = "books.json"  # указываем путь к файлу

# Загружаем данные
try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Файл {file_path} не найден.")# Пишем если файл не найден
    exit()
except json.JSONDecodeError:
    print(f"Ошибка декодирования JSON из файла {file_path}.")# пишем если ошибка в декодировании
    exit()


query = input("Введите номер квалификации: ").strip()# Запрашиваем номера квалификации


skills = [item for item in data if item.get("model") == "data.skill"]# Фильтруем объекты с model == "data.skill"


matches = [skill for skill in skills if skill.get("code") == query]# Ищем совпадение

# Вывод результата
if matches:
    print("=============== Найдено ===============")# Пишем найдено если нашли совпадение
    for skill in matches:
     
        spec = skill.get("specialty", {}) # Получаем информацию о специальности 
        spec_code = spec.get("code", "—") # Получаем информацию о специальности 
        spec_name = spec.get("name", "—") # Получаем информацию о специальности 
        spec_type = spec.get("type", "—") # Получаем информацию о специальности 
       
        print(f"{spec_code} >> Специальность \"{spec_name}\", {spec_type}") # Выводим информацию
        print(f"{skill.get('code', '—')} >> Квалификация \"{skill.get('name', '—')}\"") # Выводим информацию
else:
    print("=============== Не найдено ===============") # Пишем если не нашли совпадений
