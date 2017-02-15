  #!/usr/bin/python

 #This part will create the database to be used in the storage of the URLs of the websited that were checked

# import sqlite3

# connection = sqlite3.connect("url.db")
# sql_command = """ CREATE TABLE urls (
#                    sno INTEGER PRIMARY KEY,
#                    url VARCHAR[65534],
#
# )"""
 #To enter more factors to this table.

 #To read the URL from the file.
with open ('URL.txt','r') as myfile:
     data = myfile.read()

print data
