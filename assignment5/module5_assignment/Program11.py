import csv
import sqlite3 as lite
con = lite.connect('test.db')
with con:
    cur=con.cursor()
    csvfile = open('C:\\Users\\SANJEEV KUMAR\\Documents\\Downloads\\sample-storedata\\sample-storedata.csv')
    creader = csv.reader(csvfile)
    cur.execute('DROP TABLE IF EXISTS store')
    cur.execute('CREATE TABLE  store ( lat real(20), lon real(20), phone varchar(20), address varchar(100))')
    for t in creader:
        cur.execute('INSERT INTO  store VALUES (?,?,?,?)', t)
    csvfile.close()
    con.commit()

