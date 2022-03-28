import mysql.connector

# a function that makes the connection with the database and sets the cursor
def make_connection():
    Private_School=mysql.connector.connect(host='localhost',
                                            user='root',
                                            passwd='kostas')
    myCursor=Private_School.cursor()
    return Private_School, myCursor                                        