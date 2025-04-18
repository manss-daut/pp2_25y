from connect import connect      #моя функция подключения к базе
from config import load_config   #загружаю конфиг из .ini файла
import csv                       #для чтения CSV

#создаю таблицу в базе, если её ещё нет
def create_table(config):
    conn = connect(config)
    if conn:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS PhoneBook (
                        id SERIAL PRIMARY KEY,             -- автоинкрементный ID
                        name VARCHAR(100) NOT NULL,        -- имя (обязательное поле)
                        phone VARCHAR(20) NOT NULL UNIQUE  -- номер телефона (уникальный)
                    );
                """)
                print("Table created or already exists.")
        conn.close()

#добавляю нового человека вручную через консоль
def insert_from_console(config):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect(config)
    if conn:
        with conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
                print("Inserted:", name, phone)
        conn.close()

#читаю и вставляю данные из CSV файла
def insert_from_csv(filename, config):
    conn = connect(config)
    if conn:
        with conn:
            with conn.cursor() as cur:
                with open(filename, 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        try:
                            #каждая строка [имя, номер]
                            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
                        except Exception as e:
                            print(f"Error inserting {row}: {e}") #иф ошибки
        conn.close()
        print("CSV data inserted.")

#обновляю имя или номер по второму полю типо найди по имени — поменяй номер
def update_entry(identifier, new_value, update_field, config):
    conn = connect(config)
    if conn:
        with conn:
            with conn.cursor() as cur:
                #если обновляем имя — ищем по номеру
                if update_field == 'name':
                    cur.execute("UPDATE PhoneBook SET name = %s WHERE phone = %s", (new_value, identifier))
                #если обновляем номер — ищем по имени
                elif update_field == 'phone':
                    cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_value, identifier))
                print("Updated", update_field)  #уведомление об успехе
        conn.close()

#вывожу всех или только нужных по фильтру
def query_data(config, filter_by=None, value=None):
    conn = connect(config)
    if conn:
        with conn:
            with conn.cursor() as cur:
                #фильтр если задано поле и значение
                if filter_by and value:
                    cur.execute(f"SELECT * FROM PhoneBook WHERE {filter_by} = %s", (value,))
                else:
                    cur.execute("SELECT * FROM PhoneBook")
                rows = cur.fetchall()
                for row in rows:
                    print(row)  #печатаю каждую строку таблицы
        conn.close()

#удаляю запись по имени или номеру
def delete_entry(filter_by, value, config):
    conn = connect(config)
    if conn:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM PhoneBook WHERE {filter_by} = %s", (value,))
                print("Deleted where", filter_by, "=", value)
        conn.close()

#главное меню
def menu():
    config = load_config()  # зфгружаю конфиг один раз
    while True:
        print("\n PhoneBook Menu ")
        print("1. Create table")
        print("2. Insert from console")
        print("3. Insert from CSV")
        print("4. Update entry")
        print("5. Query data")
        print("6. Delete entry")
        print("7. Exit")
        
        choice = input("Choose an option: ")  #выбор пользователя
        
        if choice == "1":
            create_table(config)  #создаю таблицу
        elif choice == "2":
            insert_from_console(config)  #ручной ввод
        elif choice == "3":
            filename = input("Enter CSV file name: ")
            insert_from_csv(filename, config)  #загрузка из csv
        elif choice == "4":
            # если обновляешь имя — указывай номер, если обновляешь номер — указывай имя
            field = input("What to update? (name/phone): ").strip()
            identifier = input("Current value (fro phone enter name. Or for name enter phone): ").strip()
            new_value = input("New value: ").strip()
            update_entry(identifier, new_value, field, config)
        elif choice == "5":
            f = input("Filter by (name/phone) or leave blank: ").strip()
            v = input("Value or leave blank: ").strip()
            query_data(config, f if f else None, v if v else None)  #вывод данных
        elif choice == "6":
            field = input("Delete by name or phone: ")
            val = input(f"Enter {field}: ")
            delete_entry(field, val, config)  #удаление
        elif choice == "7":
            print("GGsWP")  #выход
            break

#Старт
if __name__ == '__main__':
    menu()