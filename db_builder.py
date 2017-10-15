import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

# create peeps table
c.execute("CREATE TABLE peeps (name TEXT PRIMARY KEY, age INTEGER, id INTEGER);")
peeps = open("peeps.csv", "r")
peepsReader = csv.DictReader(peeps)
for line in peepsReader: # populate peeps table line by line
    c.execute("INSERT INTO peeps VALUES('" + line['name'] + "', '" + line['age'] + "', '" + line['id'] + "');")
peeps.close() # close peeps file

# create courses table
c.execute("CREATE TABLE courses (code TEXT NOT NULL, mark INTEGER, id INTEGER);")
courses = open("courses.csv", "r")
coursesReader = csv.DictReader(courses)
for line in coursesReader: # populate courses table line by line
    c.execute("INSERT INTO courses VALUES('" + line['code'] + "', '" + line['mark'] + "', '" + line['id'] + "');")
courses.close() # close courses file

command = ""          #put SQL statement in this string
c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database

