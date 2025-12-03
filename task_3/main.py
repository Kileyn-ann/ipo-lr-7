import json

filename = "stars.json"

try:
    with open(filename, "r", encoding="utf-8") as f:# Инициализация файла с 5 записями
        data = json.load(f)
        if len(data) < 5:
            raise Exception
except:
    data  =[]
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
    try:
        with open(filename, 'r') as f:  # Открываем файл для чтения
            data = json.load(f)  # Загружаем актуальные данные
            # Проходим по каждой записи в списке
        for record in data:
             # Выводим каждую запись в формате с отступами
            print(json.dumps(record, indent=4))
    except:
            # Обработка ошибок при чтении файла
            print("Ошибка при чтении файла.")
elif choice == "2":#Если вводим 2
     
    search_id_input = input("Введите id записи: ")   # Вывод по id
    if not search_id_input.isdigit():  # Проверка, что ввод — число
        print("Некорректный ввод.")  # Сообщение об ошибке
        continue  # Возврат к началу меню
    search_id = int(search_id_input)  # Преобразование строки в число
    found = False  # Флаг, найден ли запись
    try:
        with open(filename, 'r') as f:
            data = json.load(f)  # Загружаем текущие данные
        for idx, record in enumerate(data):  # Перебираем записи с индексами
            if record.get('id') == search_id:  # Если id совпало
                print(f"Запись найдена на позиции {idx}:")  # Сообщение
                print(json.dumps(record, indent=4))  # Вывод записи
                found = True  # Устанавливаем флаг найдено
                break  # Выходим из цикла
        if not found:  # Если не нашли
                    print("Запись с таким id не найдена.")  # Предупреждение
    except:
                print("Ошибка при чтении файла.")  # Обработка ошибок


elif choice == "3":       # Если вводим 3
      
    try:
        with open(filename, 'r') as f:  # Читаем текущие данные
            data = json.load(f)
    except:
        data = []  # Если файла нет или ошибка, создаём пустой список

    # Находим максимальный id среди существующих
    max_id = max([record['id'] for record in data], default=0)
    new_id = max_id + 1  # Новый id — на единицу больше максимального

    # Запрашиваем у пользователя поля новой записи
    name = input("Введите название модели: ")
    manufacturer = input("Введите производителя: ")

    # Запрос о типе топлива
    is_petrol_input = input("Заправляется ли машина бензином? (да/нет): ").lower()
    is_petrol = True if is_petrol_input == 'да' else False  # Булево значение

    tank_volume_input = input("Введите объем бака (литры): ")
    if not tank_volume_input.isdigit():  # Проверка, что введено число
        print("Некорректный объем бака.")
        continue  # Переходим к следующему циклу
    tank_volume = int(tank_volume_input)

    # Создаём новую запись как словарь
    new_record = {
        "id": new_id,  # Новый уникальный id
        "name": name,
        "manufacturer": manufacturer,
        "is_petrol": is_petrol,
        "tank_volume": tank_volume
    }
    # Добавляем новую запись в список
    data.append(new_record)
    # Записываем обновлённые данные обратно в файл
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print("Запись добавлена.")  # Уведомление
    operation_count += 1  # Увеличиваем счетчик операций
elif choice == "4":       # Если вводим 4
    search_id_input = input("Введите id записи для удаления: ")
    if not search_id_input.isdigit():
        print("Некорректный ввод.")
        continue
    search_id = int(search_id_input)
    try:
        with open(filename, 'r') as f:  # Читаем текущие данные
                data = json.load(f)
        found_index = -1  # Изначально не нашли
        for idx, record in enumerate(data):  # Перебираем с индексами
            if record.get('id') == search_id:  # Если нашли искомый id
                found_index = idx  # Запоминаем позицию
                break
        if found_index == -1:  # Если не нашли
            print("Запись с таким id не найдена.")
        else:
            # Удаляем запись из списка
            del data[found_index]
            # Записываем обновлённые данные
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print("Запись удалена.")  # Уведомление
            operation_count += 1  # Увеличиваем счетчик
    except:
        print("Ошибка при чтении файла.")
elif choice == "5":#Если вводим 5
       
        print(f"Выход. Выполнено операций с записями: {operations_count}") # Выход из программы
        break

else:#или
        print("Некорректный выбор. Попробуйте снова.")#Если возникла ошибка просим попробовать снова
        continue
