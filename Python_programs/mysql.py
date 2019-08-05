import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="maneesh",database="test" )
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
print("Existing Databases in MySQL")
for x in mycursor:
    print(x)
mycursor.execute("CREATE DATABASE IF NOT EXISTS PyDB ")
myresult=mycursor.execute("Use PyDB")
mycursor.execute("CREATE TABLE IF NOT EXISTS Students (id INT(10) AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(25), Marks INT(5))")
mycursor.execute("SHOW TABLES")

print("\nCurrent Tables in PyDb Database")
for x in mycursor:
        print(x)
sql = "INSERT INTO Students (Name, Marks) VALUES (%s, %s)"
val = [ ('Peter',78),('Alice', 85),('Bob',86), ('Amit', 76),('Ben', 78),('William',73),
        ('William',71),('Zim',79),('Reena',81), ]
        
mycursor.executemany(sql, val)
mydb.commit()
print("\n",mycursor.rowcount,"record(s) were inserted.")
print(mycursor.lastrowid, "is the last row ID\n")
mycursor.execute("SELECT * FROM Students ORDER BY Name DESC")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
sql = "DELETE FROM Students WHERE Name = %s"
nam = ("William",)
mycursor.execute(sql, nam)
mydb.commit()
print(mycursor.rowcount, " record(s) deleted with name -William-")
sql = "DROP TABLE IF EXISTS Students"
print("\nStudents Table Dropped Successfully")
mycursor.execute(sql)
mydb.close()
