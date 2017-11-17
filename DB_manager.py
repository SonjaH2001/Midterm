import sqlite3 as sql


# this will be the DB handler a

sqlite_file = 'ClesiusCookies_db.sqlite' #name of the database
# conn_man = sqlite3.connect(sqlite_file)  #wrong way, needs framework

# def createDB():
#     print("--->creating the database<---")  # for testing
#
#     try:
#         conn = sql.connect(sqlite_file)
#         conn.execute("CREATE TABLE IF NOT EXISTS cookies(id INTEGER PRIMARY KEY Autoincrement, name TEXT NOT NULL , cost FLOAT  NOT NULL)")
#         conn.execute("CREATE TABLE IF NOT EXISTS cart(item_id INTEGER , FOREIGN KEY (item_id)REFERENCES cookies(id) )")
#         print("Database and two tables are created!!")
#     except sql.OperationalError as err :
#         print(err)
#         print("Database already exists!!!")

# def createCookies(cookie):
#     conn = sql.connect(sqlite_file)
#     c = conn.cursor()
#     c.execute("INSERT INTO cookies(id, name, cost) VALUES (?,?,?)",(cookie))
#     conn.commit()
#     conn.close()
# #To show cookies on the browser
# def createCookieList():
#     cookieList = []
#     cookieList.append([1,"Seasonal Sensation", 4.30 ])
#     cookieList.append([2, "Suger Hill Gang", 6.70])
#     cookieList.append([3, "Chocolate Pinky Delights", 3.10])
#     cookieList.append([4, "Chocolate Chip Peanust Butter Dream", 9.60])
#     for cookie in cookieList:
#         createCookies(cookie)
#
#     print("Cookie is added in the table")

# ************************************************************************************
#
def showCookie(type):  #only shows 1 cookie
    conn = sql.connect(sqlite_file)
    c = conn.cursor()
    c.execute("Select id, name, price from cookie_type WHERE id LIKE ?",(type))
    cookies = list(c.fetchall())
    return cookies


def create_db(): #call when start up the server
    print("--->creating the database<---")  # for testing

    conn_man = sql.connect(sqlite_file)  # not a great way to do this, needs framework
    cursor = conn_man.cursor()
    with open("schema.sql", "r") as schema:
        create_table = schema.read()
        cursor.executescript(create_table)
        createCookieList()

    # cursor.commit()
    conn_man.close()

def createCookies(cookie):
    conn = sql.connect(sqlite_file)
    c = conn.cursor()
    c.execute("INSERT INTO cookie_type(id, name, price) VALUES (?,?,?)", cookie)
    conn.commit()
    conn.close()

# To show cookies on the browser
def createCookieList():
    cookieList = []
    cookieList.append([1, "Seasonal Sensation", 4.30])
    cookieList.append([2, "Suger Hill Gang", 6.70])
    cookieList.append([3, "Chocolate Pinky Delights", 3.10])
    cookieList.append([4, "Chocolate Chip Peanust Butter Dream", 9.60])
    for cookie in cookieList:
        createCookies(cookie)

    print("Cookie is added in the table")


# def getAllCookies():
#     return [
#         [101, "Seasonal Sensations", '$5'],
#          [205, "Suger Hill Gang", '$5'],
#         [307, "Chocolate Pinky Delights", '$5'],
#         [500, "Chocolate Chip Peanut Butter Dream", '$5']
#     ]
#
# def getQuantity():
#     return [
#         [1, "1 box", '$5'],
#         [2, "2 boxes", "$10"],
#         [3, "3 boxes", "$15"],
#         [4, "4 boxes", "$20"],
#         [5, "5 boxes", "$25"],
#         [6, "6 boxes", "$30"],
#         [7, "7 boxes", "$35"],
#         [8, "8 boxes", "$40"],
#         [9, "9 boxes", "$45"],
#         [10, "10 boxes", "$50"]
#         ]
#
# def showOrderDetails():
#     return getQuantity() # for testing