  #!/usr/bin/python

 #This part will create the database to be used in the storage of the URLs of the websited that were checked
import sqlite3

connection = sqlite3.connect("url.db")

cursor = connection.cursor()

#TO delete TABLE
#cursor.execute("DROP TABLE urls")

sql_command = """ CREATE TABLE urls (
                sno INTEGER PRIMARY KEY,
                url VARCHAR[1000],
                
)"""

cursor.execute(sql_command)

cursor.execute("""INSERT INTO urls(sno, url) VALUES (1, "test")""")

cursor.execute("SELECT * FROM urls")
result = cursor.fetchall()
print(result)
for r in result:
    print(r)


 #To read the URL from the file.
#with open ('URL.txt','r') as myfile:
#     data = myfile.read()

#print data
