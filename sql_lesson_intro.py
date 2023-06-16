import sqlite3

# connection = sqlite3.connect(':memory:')
with sqlite3.connect('test.db') as connection:
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    # cursor.execute("PRAGMA foreign_keys = OFF")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS country(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            population INTEGER
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            address TEXT,
            email TEXT,
            country_id INTEGER NOT NULL DEFAULT 0,
            balance REAL NOT NULL DEFAULT 0,
            FOREIGN KEY (country_id) REFERENCES country(id)
        );
    """)

    cursor.execute("""
        INSERT INTO customer (name, country_id, balance)
        VALUES ('Marta', 3, 50);
    """)

    # cursor.execute("""
    #     INSERT INTO customer (name, address, country_id, balance)
    #     VALUES
    #           ('Marta', 'Obolon, 15', 3, 50),
    #           ('Alex', 'Obolon, 16', 3, 50),
    #           ('Max', 'Obolon, 17', 3, 50),
    #           ('George', 'Obolon, 18', 3, 50);
    # """)

    # DO NOT ACT LIKE THAT !!!!!!!!!!!!!!!
    # name = 'FFF'
    # country = 1
    # balance = 6
    #
    # cursor.execute(f"""
    #     INSERT INTO customer (name, country_id, balance)
    #     VALUES ('{name}', {country}, {balance});
    # """)

    #  USE THIS APPROACH
    values = [
        ('Max222', 'Kyiv 18', 1, 100.5),
        ('Max333', 'Kyiv 19', 2, 2200.5),
    ]

    cursor.executemany(
        """
        INSERT INTO customer (name, address, country_id, balance)
        VALUES (?, ?, ?, ?)
        """,
        values,
    )

    #     SELECT DATA
    # data = cursor.execute("""
    #     SELECT *
    #     FROM customer
    # """)
    #
    # # print(data.fetchone())
    # print(data.__next__())
    # print(data.__next__())
    # print(data.__next__())
    # print(8888888888888888)
    #
    # print(data.fetchall())
    # # print(data.fetchmany(4))

    # sorting = ASC increase, DESC - decrease
    # data = cursor.execute("""
    #     SELECT name, balance, id
    #     FROM customer
    #     WHERE
    #         balance > 100 AND id IN (10, 12, 6) OR
    #         balance BETWEEN 10 AND 49 OR
    #         name = 'Alex'
    #     ORDER BY name ASC
    #     LIMIT 3
    #     OFFSET 1
    #     ;
    # """)
    #
    # print(data.fetchall())

    #     UPDATE

    # cursor.execute("""
    #     UPDATE customer
    #     SET
    #         balance = 15000
    #     WHERE
    #         name LIKE '_Max___';
    # """)

    # cursor.execute("""
    #     UPDATE customer
    #     SET
    #         email = LOWER('mr_' || name || '@gmail.com')
    #     WHERE
    #         id > 5
    #     ;
    # """)

    #     DELETE
    # cursor.execute("""
    #     DELETE FROM customer
    #     WHERE name LIKE '%22';
    # """)

    sqlite_select_query = 'SELECT sqlite_version();'
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print(record)
    print(connection.total_changes)
