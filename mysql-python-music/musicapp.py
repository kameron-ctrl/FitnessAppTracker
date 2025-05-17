import mysql.connector

# Execute:
# python3 musicapp.py
#

def findbyinst():
  inst = input("Instrument: ")

  mycursor = mydb.cursor()

  sql = "SELECT firstname, lastname, instrument " \
      "FROM musicians join instrumentsplayed " \
      "ON musicians.Id = instrumentsplayed.Musician " \
      "WHERE instrument = %s"
    
  arg = (inst, )

  mycursor.execute(sql, arg)

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)

def insert():
  fn = input("First Name: ")
  ln = input("Last Name: ")
  bornyear = input("Birth Year: ")

  mycursor = mydb.cursor()

  sql = "INSERT INTO musicians (firstname, lastname, born) " \
                                   "VALUES(%s,%s,%s)"
  arg = (fn, ln, bornyear, )

  mycursor.execute(sql, arg)

def showall():
     
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM musicians")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
    
  return;

def findbyid():
    
    id = input("Id: ")

    mycursor = mydb.cursor()

    sql = "SELECT * FROM musicians WHERE id = %s"
    arg = (id, )

    mycursor.execute(sql, arg)

    myresult = mycursor.fetchall()

    for x in myresult:
       print(x)
    
    return;

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="music"
)

option = 0;

while option != 5: 
    
    print("")
    print("1. Add a musician")
    print("2. Find a musician by id")
    print("3. Find a musician by instrument")
    print("4. Show all musicians")
    print("5. Exit")
    
    option = int(input("Choice: "))
    print (option)
    if option == 1:
        insert()
    elif option == 4:
        showall()
    elif option == 2:
        findbyid()
    elif option == 3:
        findbyinst()


