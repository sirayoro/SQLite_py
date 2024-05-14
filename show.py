import sqlite3

# Создаем подключение к базе данных
connection = sqlite3.connect("hotel_test.db")
cursor = connection.cursor()

# Функция для вывода содержимого таблицы на экран
def display_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    print(f"Содержимое таблицы {table_name}:")
    for row in rows:
        print(row)
    print()

# Выводим содержимое каждой таблицы
display_table("rooms")
display_table("guests")
display_table("bookings")

connection.close()
