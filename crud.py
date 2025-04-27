import sqlite3


def get_all_users():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        users = cursor.execute('''SELECT * FROM users''').fetchall()
        cursor.close()

    return users


if __name__ == "__main__":
    with sqlite3.connect("users.db") as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS users '
                           '(id INTEGER PRIMARY KEY, username TEXT, email TEXT)')
        conn.commit()
