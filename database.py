import sqlite3
from tkinter import messagebox

def create_table():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS user(system_name text primary key, name text, password text)")

    connection.commit()
    connection.close()

def add(system_name, name, password):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    try:
        cursor.execute(f'INSERT INTO user VALUES(?, ?, ?)', (system_name, name, password))
    except sqlite3.IntegrityError:
       messagebox.showerror("שגיאה","לא ניתן להרשם עם השם משתמש הזה זה כבר תפוס!!!")


    connection.commit()
    connection.close()


def login(system_name, password):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM user WHERE system_name=? AND password=?", (system_name,password))

    user = cursor.fetchall()

    connection.close()

    return user


