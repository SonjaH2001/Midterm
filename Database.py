import sqlite3
# This is the practice DB py file
# borrowed from an earlier project, to get it started


sqlite_file = 'ClesiusCookies_db.sqlite'    # name of the db

table_cookie_type = 'Cookie_Type'   #   table name
id_field = 'Cookie_ID'              #   Primary key
name_field = 'Cookie_Name'          #   name column
price_field = 'Cookie_Price'        #   price column

def main():
    show_menu() # call function to show user options

def show_menu():
    while True:
        print()  # intentional blank line
        print("Menu options:    ")  # show user thier options...
        print("1: CREATE a database and table")
        print("2: ADD a row of data to the table") # "a" table? then select the table?
        print("3: UPDATE a row of data from the table") #   """
        print("4: DELETE a row of data from the table") #   """
        print("5: SHOW the data from entire table") #   """
        print("6: DISPLAY a single row of data")    #   """
        # print("7: DROP TABLE-->BE CAREFUL")   hidden, for testing purposes only
        print("9: QUIT program")
        print()  # intentional blank line
        user_input = input("Please enter the number of your selection: ")  # gets the user choice
        # call the function, from user's choice
        if user_input == "1":
            create_database()
        # elif user_input == "2":
        #     add_row()
        # elif user_input == "3":
        #     update_row()
        # elif user_input == "4":
        #     delete_row()
        # elif user_input == "5":
        #     show_all_rows()
        # elif user_input == "6":
        #     show_single_row()
        # elif user_input == "7":  # for testing
        #     drop_table()
        elif user_input == "9":
            print()
            print("Thank you, goodbye")
            break  # ends the program
        else:
            print()  # intentional blank line
            print("Please make a valid selection, jackass.")  # prompts user for valid input
            print()  # intentional blank line
            # show_menu() nope. It loops back up to the top, did a while loop instead.

def create_database():
    print("--->creating the database<---")  # for testing
        # connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # creating table with columns, put in a variable to make debugging easier
    create_table_sql = (
        'CREATE TABLE If NOT EXISTS {tn} ('
        ' {nf} {ft} PRIMARY KEY AUTOINCREMENT ,'
        ' {nf2} {ft_T} NOT NULL , '
        ' {nf3} {ft_T} NOT NULL ,'
        ')  '
    ).format(tn=table_cookie_type, nf=id_field, nf2=name_field, nf3=price_field, ft_T=field_type_txt)

    c.execute(create_table_sql)  # pass the variable instead of putting the code into execute statement

    conn.commit()
    conn.close()

main()
