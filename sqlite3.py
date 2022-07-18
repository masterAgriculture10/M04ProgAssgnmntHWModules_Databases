#16.4 Use the sqlite3 module to create a SQLite database called books.db 
#and a table called books with these fields: title (text), author 
#(text), and year (integer)

#16.6 Select and print the title column from the book table in 
#alphabetical order.

#16.8 Use the sqlalchemy module to connect to the sqlite3 database 
#books.db that you just made in exercise 16.4. As in 16.6, select 
#and print the title column from the book table in alphabetical order.

import sqlite3 
  
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.books('''CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)''')
#<sqlite3.Cursor object at 0x1006a22d0> #message to imply anobject has been created

('SELECT title FROM books ORDER BY title;')

conn =sqlite3.connect('books.db')
curs.books ('SELECT title FROM books ORDER BY title;')
curs.fetchall()

