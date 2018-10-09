#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      KELS
#
# Created:     07/10/2018
# Copyright:   (c) KELS 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/python


import mysql.connector as mariadb

"""
mariadb_connection = mariadb.connect(
    host='localhost',
    user='root',
    password='shyzay2007'
)

cursor = mariadb_connection.cursor()

cursor.execute("CREATE DATABASE nytimestopstories")

mariadb_connection.commit()
After creation of the database, comment out the above code"""


mariadb_connection = mariadb.connect(host='localhost', user='root', password='shyzay2007', database='nytimestopstories')
cursor = mariadb_connection.cursor()

#Creation of Table
cursor.execute("CREATE TABLE articles (ArticleID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, Title VARCHAR(100) NOT NULL, Link VARCHAR(255) NOT NULL, Byline VARCHAR(100) NOT NULL, Date DATE NOT NULL)")


#Insertion of information, into the tables
sql = "INSERT INTO articles (Title,Link,Byline,Date) VALUES (%s, %s, %s, %s)"
val = [
  ('As Tokyo Fish Market Closes, Sellers and Customers Honor an Era of Grime', 'https://www.nytimes.com/2018/10/06/world/asia/tokyo-fish-market-tsukiji.html?rref=collection%2Fsectioncollection%2Ffood', 'MOTOKO RICH', '2018:10:06'),
  ('Ireland Bill Aims to Crack Down on Excessive Drinking With Health Warning Labels', 'https://www.nytimes.com/2018/10/06/world/europe/ireland-drinking-bill.html?rref=collection%2Fsectioncollection%2Ffood', 'ED OLOUGHLIN', '2018:10:06'),
  ('Real Madrid Offense Hasn’t Been This Futile in More Than 30 Years', 'https://www.nytimes.com/2018/10/06/sports/soccer/real-madrid-alaves-la-liga.html?rref=collection%2Fsectioncollection%2Fsports', 'THE ASSOCIATED PRESS', '2018:10:06'),
  ('Fightback Relieves Pressure on Mourinho', 'https://www.bbc.com/sport/football/45689298', 'Mike Henson', '2018:10:06')
]

cursor.executemany(sql, val)
mariadb_connection.commit()
print(cursor.rowcount, "was inserted.")
