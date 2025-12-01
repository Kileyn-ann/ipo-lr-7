import json

filename = "stars.json"

try:
    with open(filename, "r", encoding="utf-8") as f:# Инициализация файла с 5 записями
        data = json.load(f)
        if len(data) < 5:
            raise Exception
except:
    data = [#Создаём список
        {"id": 1, "name": "Сириус", "constellation": "Малый Пес", "is_visible": True, "radius": 1.71},
        {"id": 2, "name": "Бетельгейзе", "constellation": "Орёл", "is_visible": True, "radius": 887},
        {"id": 3, "name": "Полярная звезда", "constellation": "Малая Медведица", "is_visible": True, "radius": 35},
        {"id": 4, "name": "Альтаир", "constellation": "Пегас", "is_visible": True, "radius": 2.37},
        {"id": 5, "name": "Проксима Центавра", "constellation": "Центавра", "is_visible": False, "radius": 0.14}
    ]
    with open(filename, "w", encoding="utf-8") as f:#Открываем файл
        json.dump(data, f, ensure_ascii=False, indent=4)


operations_count = 0# Переменные для подсчёта операций

while True:#
    print("\nМеню:")#Выводим на экран меню и его пункты
    print("1. Вывести все записи")
    print("2. Вывести запись по полю (id)")
    print("3. Добавить запись")
    print("4. Удалить запись по полю (id)")
    print("5. Выйти из программы")
    choice = input("Введите номер пункта: ")

    if choice == "1":#Если вводим 1
        # Выводим все записи
        if len(data) == 0:
            print("Записи отсутствуют.")
        else:
            for record in data:#
                print(json.dumps(record, ensure_ascii=False, indent=4))
        continue

    elif choice == "2":#Если вводим 2
     
        search_id = input("Введите id записи: ")   # Вывод по id
        found = False
        for index, record in enumerate(data):#
            if str(record["id"]) == search_id:#
                print(f"Позиция записи: {index}")
                print(json.dumps(record, ensure_ascii=False, indent=4))
                found = True
                break
        if not found:#
            print("Запись не найдена.")#
        continue

    elif choice == "3":       # Если вводим 3
      
        new_id = max([r["id"] for r in data], default=0) + 1 # Добавление записи 
        name = input("Название звезды: ")#ВВодим название звезды
        constellation = input("Созвездие: ")#Вводим созвездие
        is_visible_input = input("Видима без телескопа? (да/нет): ").strip().lower()
        is_visible = True if is_visible_input in ("да", "д") else False
        radius_input = input("Радиус (в солнечных радиусах): ")
        try:
            radius = float(radius_input)
        except:#Записываем новые записи
            radius = 0.0
        new_record = {
            "id": new_id,
            "name": name,
            "constellation": constellation,
            "is_visible": is_visible,
            "radius": radius
        }
        data.append(new_record)
        with open(filename, "w", encoding="utf-8") as f:#
            json.dump(data, f, ensure_ascii=False, indent=4)#
        print("Запись добавлена.")
        continue

    elif choice == "4":       # Если вводим 4
        del_id = input("Введите id для удаления: ")#Просим ввести айди для удаления
        index_to_delete = -1
        for index, record in enumerate(data):
            if str(record["id"]) == del_id:
                index_to_delete = index
                break
        if index_to_delete == -1:#Если запись не найдена
            print("Запись не найдена, удаление невозможно.")
        else:
            del data[index_to_delete]#
            with open(filename, "w", encoding="utf-8") as f:#Открывам файл
                json.dump(data, f, ensure_ascii=False, indent=4)#удаляем запись
            print("Запись удалена.")
        continue

    elif choice == "5":#Если вводим 5
       
        print(f"Выход. Выполнено операций с записями: {operations_count}") # Выход из программы
        break

    else:#или
        print("Некорректный выбор. Попробуйте снова.")#Если возникла ошибка просим попробовать снова
        continue
