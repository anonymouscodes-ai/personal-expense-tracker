import sqlite3

def create_table():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()


def add_expense(name, amount, category):
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO expenses (name, amount, category) VALUES (?, ?, ?)",
        (name, amount, category)
    )

    connection.commit()
    connection.close()
    
def view_expenses():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    connection.close()

    return expenses

create_table()

print("Database ready!")