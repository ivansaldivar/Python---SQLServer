import pymssql  

conn = pymssql.connect(server='DAVINCI_DAEMOND\SAURON', 
                       user='sa', 
                       password='paulina', 
                       database='PEGAXUS_DB_MASTER')  
cursor = conn.cursor()  
cursor.execute('SELECT ID_COMUNA, DESCRIPCION FROM PEGAXUS_COMUNAS_PROVINCIAS ORDER BY DESCRIPCION;')  
row = cursor.fetchone()  
i = 1
while row:  

    print( str(i) + " - " + str(row[0]) + " " + str(row[1])  )
    row = cursor.fetchone()  
    i = i + 1
cursor.close()
conn.close()