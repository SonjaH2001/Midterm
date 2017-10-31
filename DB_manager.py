import sqlite3
# this will be the DB handler

sqlite_file = 'ClesiusCookies_db.sqlite' #name of the database
print("--->creating the database<---")  # for testing
# conn_man = sqlite3.connect(sqlite_file)  #wrong way, needs framework


def create_db(): #call when start up the server

    conn_man = sqlite3.connect(sqlite_file)  # wrong way, needs framework
    cursor = conn_man.cursor()
    with open("schema.sql", "r") as schema:
        create_table = schema.read()
        cursor.executescript(create_table)

    cursor.commit()
    conn_man.close()
def getAllCookies():
    return [
        [101, "Seasonal Sensations", 8],
         [205, "Suger Hill Gang", 8],
        [307, "Chocolate Pinky Delights", 10],
        [500, "Chocolate Chip Peanut Butter Dream", 7]
    ]



