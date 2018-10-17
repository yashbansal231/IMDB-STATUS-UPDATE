import mysql.connector

def dbConnect(loc,usr,pas,db):
    mydb = mysql.connector.connect(
		host=loc,
		user=usr,
		passwd=pas,
		database=db
	)
    return mydb.cursor()
