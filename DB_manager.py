import sqlite3


sqlite_file = 'ClesiusCookies_db.sqlite' #name of the database
print("--->creating the database<---")  # for testing
conn_man = sqlite3.connect(sqlite_file)  #wrong way, needs framework

cursor = conn_man.cursor()

def create_db(): #call when start up the server

    with open("schema.sql", "r") as schema:
        create_table = schema.read()
        cursor.executescript(create_table)


