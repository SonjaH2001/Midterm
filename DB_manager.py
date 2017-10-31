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
        [101, "Seasonal Sensations", '$5'],
         [205, "Suger Hill Gang", '$5'],
        [307, "Chocolate Pinky Delights", '$5'],
        [500, "Chocolate Chip Peanut Butter Dream", '$5']
    ]

def getQuantity():
    return [
        [1, "1 box", '$5'],
        [2, "2 boxes", "$10"],
        [3, "3 boxes", "$15"],
        [4, "4 boxes", "$20"],
        [5, "5 boxes", "$25"],
        [6, "6 boxes", "$30"],
        [7, "7 boxes", "$35"],
        [8, "8 boxes", "$40"],
        [9, "9 boxes", "$45"],
        [10, "10 boxes", "$50"]
        ]

def showOrderDetails():
    return getQuantity() # for testing