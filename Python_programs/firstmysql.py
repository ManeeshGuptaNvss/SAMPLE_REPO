import mysql.connector as s
mydb= s.connect(host="localhost",user="root",passwd="maneesh",database="test")

mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS PyDB")
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)
mycursor.execute("use pydb")
mycursor.execute('create table if not exists Students(id int(10) auto_increment primary key,name varchar(25),marks int(5))')
mycursor.execute('insert into Students values(11706038,"Maneesh",36)')

sql=" Insert into Students (name,marks) values (%s,%s)"
val=[('peter',23),('gupta',12)]
mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("select * from Students")
for i in mycursor:
    print(i)
mycursor.execute('drop table Students')

mydb.close()
