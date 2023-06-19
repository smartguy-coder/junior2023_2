import sqlite3
import hashlib


def encript_password(value: str) -> str:
    result = hashlib.md5(value.encode()).hexdigest()  # to bytes
    print(result)
    return result

# encript_password('9')

with sqlite3.connect('new_db.db') as connection:
    cursor = connection.cursor()
    cursor.execute("""PRAGMA foreign_keys = ON""")

    query_create_tables = """
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            login TEXT NOT NULL CHECK (length(login) > 5) UNIQUE,
            password TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS category(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(16) NOT NULL,
            description TEXT
        );
        CREATE TABLE IF NOT EXISTS device(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL CHECK (length(name) > 1) UNIQUE,
            description TEXT,
            category_id INTEGER,
            manager TEXT,
            whole_price DECIMAL(10, 2) CHECK (whole_price > 0),
            price DECIMAL(10, 2) CHECK (price >= whole_price),
            FOREIGN KEY (category_id) REFERENCES category(id)
        )
    """

    cursor.executescript(query_create_tables)

    # name = input('Enter your name > ')
    # login = input('Enter your login > ')
    # password = input('Enter your password > ')
    # values = [name, login, password]
    #
    # connection.create_function('encode', 1, encript_password)
    #
    # cursor.execute("""
    #     INSERT INTO user(name, login, password)
    #     VALUES (?, ?, encode(?))
    # """,
    # values)

    #     45c48cce2e2d7fbdea1afc51c7c6ad26
    # cursor.execute("""
    #     UPDATE user
    #     SET password = :Pass
    #     WHERE id = 1
    # """,
    # {'Pass': '45c48cce2e2d7fbdea1afc51c7c6ad26'})

    # RENAME TABLE
    # cursor.execute("""
    #     ALTER TABLE device
    #     RENAME TO product;
    # """)

    # RENAME COLUMN
    # cursor.execute("""
    #     ALTER TABLE product
    #     RENAME COLUMN whole_price TO wholeprice;
    # """)

    # ADD COLUMN
    # cursor.execute("""
    #     ALTER TABLE product
    #     ADD COLUMN weight REAL;
    # """)

    # SQL INJECTIONS
    # user_input = input('Enter id of category ')
    # # 2 or true
    # data = cursor.execute(f"""
    #     SELECT *
    #     FROM category
    #     WHERE id = {user_input};
    # """)
    # print(data.fetchall())

    # user_input_id = input('Enter id of category ')
    # user_input_description = input('Enter description ')
    # # 2; INSERT INTO category(name, description) VALUES ('fake_name', 'fake_description');--
    # data = cursor.executescript(f"""
    #     SELECT *
    #     FROM category
    #     WHERE id = {user_input_id} and description LIKE '%{user_input_description}%';
    # """)
    # print(data.fetchall())
    # data = cursor.execute("""
    #     SELECT product.name, category.name, category.description, product.price, product.description
    #     FROM product
    #     JOIN category
    #     ON product.category_id = category.id
    # """)
    # print(data.fetchall())

    # CREATE DUMP
    # with open('new_db.sql', 'w') as dump:
    #     for sql in connection.iterdump():
    #         dump.write(sql)

    # with open('new_db.sql', 'r') as dump:
    #     sql = dump.read()
    #     cursor.executescript(sql)

    # INNER JOIN
    data = cursor.execute("""
        SELECT device.name, device.price, device.category_id, category.name
        FROM device
        JOIN category
        ON device.category_id = category.id
    """)

    print(data.fetchall())
    # LEFT JOIN
    data = cursor.execute("""
        SELECT device.name, device.price, device.category_id, category.name
        FROM device
        LEFT JOIN category
        ON device.category_id = category.id
    """)

    print(data.fetchall())

    trigger_sql_new_category = """
        CREATE TRIGGER IF NOT EXISTS category_premium
        AFTER UPDATE ON device
        WHEN new.price > 1000
        BEGIN
            INSERT INTO category (name, description) VALUES ('new premium category', 'for VIPs only');
        END;
    """
    cursor.execute(trigger_sql_new_category)

    # cursor.execute("""
    #     INSERT INTO device (name, price)
    #     VALUES (?, ?)
    # """,
    #                ('New name', 1200))

    cursor.execute("""
        UPDATE device
        SET price = 1500
        WHERE id = 3
    """)

