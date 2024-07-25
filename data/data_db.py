import datetime
import sqlite3

db_name = "database_students.db"


def make_read_query(query):
    try:
        with sqlite3.connect(db_name) as conn:
            print(f"База даних {db_name} підключена")
            cursor = conn.cursor()
            cursor.execute(query)
            record = cursor.fetchall()

        data_pizza = []
        if record:
            for row in record:
                data_pizza.append(
                        {"id": row[0],
                       "name": row[1],
                       "ingredients": row[2],
                       "price": row[3] if row[3] else 0,
                        }
                )
        return data_pizza
    except sqlite3.Error as e:
        print("Помилка запиту:", e)




def make_write_query(query, *args):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, *args)
            conn.commit()
            print(f"Зaпит {query.split()[0]} виконаний з параметрами {args}")

        print("Зєднання з SQLite закрите")
    except sqlite3.Error as e:
        print("Помилка запиту", e)


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS pizzas (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        ingredients TEXT DEFAULT NULL,
        price INTEGER DEFAULT NULL,  
        joining_date DATETIME);
    """
    make_write_query(query)


def insert_data(name, ingredients, price):
    joining_date = datetime.datetime.now()
    query = """
    INSERT INTO pizzas (name, ingredients, price, joining_date)
               VALUES (?, ?, ?, ?)
    """

    args = (name, ingredients, price, joining_date)
    make_write_query(query, args)


def get_all():
    query = """SELECT * FROM pizzas"""
    return make_read_query(query)


def update_data_table(name, ingredients, price):
    join_data = datetime.datetime.now()

    update_query = ("""
    UPDATE pizzas GET name = ?, ingredients = ?, price = ?;
    """)

    data_tuple = (name, ingredients, price)
    make_write_query(update_query, data_tuple)

def delete_data_table(price):
    query = ("""
        DELETE FROM pizzas WHERE price = ?;
        """)
    make_write_query(query,(price,))



if __name__ == "__main__":

    create_table()

    data_pizza = [{"name": "Маргаріта", "ingredients": "Помідори, Моцарелла, Базілік", "price": "150"},
                 {"name": "Пеппероні", "ingredients": "Салямі, Сир, Томатний соус", "price": "180"},
                 {"name": "Гавайська", "ingredients": "Ананаси, Куряче філе", "price": "120"},
                 {"name": "Сирна", "ingredients": "Сир моцарелла, сир слугуні, сливочний соус", "price": "130"}
                 ]

    # for d in data_pizza:
    #     insert_data(**d)

