import mysql.connector
from tabulate import tabulate

# " tabulate" is a neet arrangement of database records

conn = mysql.connector.connect(host="localhost", user="root", password="dinesh", database="Python_db")

'''
# database connection confirm :
if conn:
    print("connected")
else:
    print("connection error")
'''


def insert(name, age, city):
    res = conn.cursor()
    sql = "insert into users (name,age,city) values(%s,%s,%s)"
    users = (name, age, city)  # %S - it is a strings. it is stored in here.
    res.execute(sql, users)
    conn.commit()  # 'commit' is used to insert values in db.
    print("Data Insert Sucessfully..!")


def update(name, age, city, id):
    res = conn.cursor()
    sql = "update users set name=%s,age=%s,city=%s where id=%s"
    users = (name, age, city, id)  # %S - it is a strings. it is stored in here. 'id=%s' is mensioned here = id .
    res.execute(sql, users)
    conn.commit()  # 'commit' is used to insert values in db.
    print("Data Update Sucessfully..!")


def select():
    res = conn.cursor()  # cursur is help to connect with python to db.
    sql = "select id,name,age,city from users"
    res.execute(sql)
    # result = res.fetchone() #only one record is print  (fetchone)
    # result = res.fetchmany(2)  # only one record is print  (fetchmany)
    result = res.fetchall()  # only one record is print  (fetchall)
    print(tabulate(result, headers=["ID", "NAME", "AGE", "CITY"]))
    print("-----------------------------------------")


def delete(id):
    res = conn.cursor()
    sql = "delete from users  where id=%s"
    users = (id,)  # %S - it is a strings. it is stored in here. 'id=%s' is mensioned here = id .
    res.execute(sql, users)
    conn.commit()  # 'commit' is used to insert values in db.
    print("Data delete Sucessfully..!")


while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice = int(input("Enter your choice : "))

    # choice comments:
    if choice == 1:  # insert
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        city = input("Enter City : ")
        insert(name, age, city)

    elif choice == 2:  # update
        id = int(input("Enter the Id : "))
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        city = input("Enter City : ")
        update(name, age, city, id)

    elif choice == 3:  # select
        select()

    elif choice == 4:  # delete
        id = input("Enter the ID to Delete : ")
        delete(id)

    elif choice == 5:  # exit
        print("Thank You...!")
        quit()

    else:
        print("Invalid selection... Please try again...!")
