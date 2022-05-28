import time

import mysql.connector
from flask import render_template
from objects import User

mydb = mysql.connector.connect(
  host="localhost",
  user="Martin",
  password="password",
  database="admin"
)

mycursor = mydb.cursor()


def add_user(user):
  mycursor = mydb.cursor()
  mycursor.execute(''' INSERT INTO user VALUES(%s,%s,%s)''', (user.username, user.email, user.password))
  mydb.commit()
  mycursor.close()
  return True

"""
sql = "INSERT INTO user (username, email, password) VALUES (%s, %s, %s)"
val = [
    ('Martin', 'martinjjb@gmail.com', 'test1 '),
    ('Karen', 'karen@btinternet.com', 'test2')
    ]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")


sql = "INSERT INTO post (id, title, date_posted, content, user_id) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('1', 'The First Try', '2022-05-21', 'This is to set some text', '1 '),
    ('2', 'The Next Try', '2022-05-22', 'Thsi is to follow up on text', '2')
    ]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
"""




