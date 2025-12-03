import json
list = "S:/students/GR_88/Данильчик Елизавета/ПО/lr7/task_2/book.json"
with open (list, 'r' , encoding='utf-8') as file:
    book = json.load(file)

for i in range(len(book)):
    print(f"---------------------- Книга", i+1, " -----------------------")# вывожу информацию
    print(f"Название: {book[i]['title']}, Автор: {book[i]['author']},")
    print(f"-------------------------{book[i]['year']}-------------------------\n")
