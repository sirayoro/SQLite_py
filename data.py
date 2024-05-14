import sqlite3
import random
from faker import Faker

connection = sqlite3.connect("hotel_test.db")
cursor = connection.cursor()

fake = Faker()

# Случайные данные для rooms
for i in range(10): 
    room_number = i + 1
    room_type = random.choice(['Single', 'Double', 'Suite'])
    price = round(random.uniform(50, 300), 2)  # случайная цена от 50 до 300
    cursor.execute('''INSERT INTO rooms (room_number, type, price) VALUES (?, ?, ?)''', (room_number, room_type, price))

# Случайные данные для guests
for i in range(10):  
    name = fake.name()
    email = fake.email()
    cursor.execute('''INSERT INTO guests (name, email) VALUES (?, ?)''', (name, email))

# Случаыйные данные для bookings
for i in range(20):  #бронирований сделаем чуть больше
    guest_id = random.randint(1, 10)  # случайный идентификатор гостя
    room_id = random.randint(1, 10)  # случайный идентификатор номера
    check_in_date = fake.date_this_year().strftime('%Y-%m-%d')
    check_out_date = fake.date_this_year().strftime('%Y-%m-%d')
    cursor.execute('''INSERT INTO bookings (
                   guest_id, room_id, check_in_date, check_out_date) 
                   VALUES (?, ?, ?, ?)''', 
                   (guest_id, room_id, check_in_date, check_out_date))

connection.commit()
connection.close()