import json

filename = "stars.json"

# Инициализация файла с 5 записями, если файла нет или он пустой
def init_data():
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            if len(data) < 5:
                raise Exception
    except:
        data = [
            {"id": 1, "name": "Сириус", "constellation": "Малый Пес", "is_visible": True, "radius": 1.71},
            {"id": 2, "name": "Бетельгейзе", "constellation": "Орёл", "is_visible": True, "radius": 887},
            {"id": 3, "name": "Полярная звезда", "constellation": "Малая Медведица", "is_visible": True, "radius": 35},
            {"id": 4, "name": "Альтаир", "constellation": "Пегас", "is_visible": True, "radius": 2.37},
            {"id": 5, "name": "Проксима Центавра", "constellation": "Центавра", "is_visible": False, "radius": 0.14}
        ]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    return data

# Функция для сохранения данных
def save_data(data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Функция для вывода всех записей
def print_all_records(data):
    if len(data) == 0:
        print("Записи отсутствуют.")
    else:
        for record in data:
            print(json.dumps(record, ensure_ascii=False, indent=4))

# Функция для поиска записи по id
def find_record_by_id(data, search_id):
    for index, record in enumerate(data):
        if str(record["id"]) == str(search_id):
            return index, record
    return -1, None

# Функция для добавления записи
def add_record(data):
    # Находим новый id
    new_id = max([r["id"] for r in data], default=0) + 1
    name = input("Название звезды: ").strip()
    constellation = input("Созвездие: ").strip()

    # Проверка публичных данных (простая)
    is_visible_input = input("Видима без телескопа? (да/нет): ").strip().lower()
    while is_visible_input not in ("да", "д", "нет", "н"):
        print("Некорректный ввод. Введите 'да' или 'нет'.")
        is_visible_input = input("Видима без телескопа? (да/нет): ").strip().lower()
    is_visible = True if is_visible_input in ("да", "д") else False

    radius_input = input("Радиус (в солнечных радиусах): ").strip()
    while True:
        try:
            radius = float(radius_input)
            break
        except:
            print("Некорректное число. Попробуйте снова.")
            radius_input = input("Радиус (в солнечных радиусах): ").strip()

    new_record = {
        "id": new_id,
        "name": name,
        "constellation": constellation,
        "is_visible": is_visible,
        "radius": radius
    }
    data.append(new_record)
    save_data(data)
    print("Запись добавлена.")

# Функция для удаления записи по id
def delete_record(data):
    del_id = input("Введите id для удаления: ").strip()
    index, record = find_record_by_id(data, del_id)
    if index == -1:
        print("Запись не найдена, удаление невозможно.")
    else:
        del data[index]
        save_data(data)
        print("Запись удалена.")

# Функция для вывода записи по id
def print_record_by_id(data):
    search_id = input("Введите id записи: ").strip()
    index, record = find_record_by_id(data, search_id)
    if index == -1:
        print("Запись не найдена.")
    else:
        print(f"Позиция записи: {index}")
        print(json.dumps(record, ensure_ascii=False, indent=4))

# Главное меню
def main():
    data = init_data()
    operations_count = 0

    while True:
        print("\nМеню:")
        print("1. Вывести все записи")
        print("2. Вывести запись по полю (id)")
        print("3. Добавить запись")
        print("4. Удалить запись по полю (id)")
        print("5. Выйти из программы")
        choice = input("Введите номер пункта: ").strip()

        if choice == "1":
            print_all_records(data)
            continue
        elif choice == "2":
            print_record_by_id(data)
            operations_count += 1
            continue
        elif choice == "3":
            add_record(data)
            operations_count += 1
            continue
        elif choice == "4":
            delete_record(data)
            operations_count += 1
            continue
        elif choice == "5":
            print(f"Выход. Выполнено операций с записями: {operations_count}")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
