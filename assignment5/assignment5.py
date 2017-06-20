# import sqlite3

# #Task-1: Check the version.

# connection = sqlite3.connect('test.db')
# print "opened database successfully."

# with connection:
#     cursor = connection.cursor()
#     # cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#     #   VALUES (1, 'Paul', 32, 'California', 20000.00 )");
#     query = ".tables"
#     cursor.execute(query)
#     data = cursor.fetchone()
#     print "SQLite version: %s" % data


# Task 2:
import sqlite3
con = sqlite3.connect('new_db')
with con:
    cur = con.cursor()
    # cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    # cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    # cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
    # cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    # cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
    # data = cur.execute("SELECT Id FROM Friends ORDER BY Id DESC")
    # for x in data:
    #     id = x
    #     break
    print cur.rowcount
    print cur.fetchall()
    # curs = cur.execute('SELECT max(id) FROM table_name')
    # print "The last Id of the inserted row is %d" % curs.fe