#!C:/Program Files/Python36/python.exe
import pymssql  

conn = pymssql.connect(server='DAVINCI_DAEMOND\SAURON', 
                       user='sa', 
                       password='paulina', 
                       database='PEGAXUS_DB_MASTER')  
cursor = conn.cursor()  
cursor.execute("EXEC SP_TESTING;")  
row = cursor.fetchone()  
i = 1
salida = ""

while row:
    salida = salida + ( str(i) + " - " + str(row[0]) + " " + str(row[1]) + "<br />" )

    row = cursor.fetchone()  
    i = i + 1

print('Content-type: text/html; charset=utf-8\n\r')
print("")

print(salida)
cursor.close()
conn.close()
