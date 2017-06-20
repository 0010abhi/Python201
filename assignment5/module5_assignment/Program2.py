import sqlite3
con = sqlite3.connect('new_db')
with con:
 cur = con.cursor()
 cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
 cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
 cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
 cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
 cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
 print "The last Id of the inserted row is %d" %(cur.lastrowid)