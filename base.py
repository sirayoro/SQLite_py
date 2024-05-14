import sqlite3

connection = sqlite3.connect("hotel_test.db")
cursor = connection.cursor()

# Таблица о номерах
cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                    id INTEGER PRIMARY KEY,
                    room_number INTEGER,
                    type TEXT,
                    price REAL
                )''')

# Таблица о гостях
cursor.execute('''CREATE TABLE IF NOT EXISTS guests (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT UNIQUE
                )''')

# Таблица с бронями
cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY,
                    guest_id INTEGER,
                    room_id INTEGER,
                    check_in_date TEXT,
                    check_out_date TEXT,
                    FOREIGN KEY (guest_id) REFERENCES guests (id),
                    FOREIGN KEY (room_id) REFERENCES rooms (id)
                )''')

connection.commit()
connection.close()