import pymssql  

conn = pymssql.connect(server='DAVINCI_DAEMOND\SAURON', 
                       user='sa', 
                       password='paulina', 
                       database='PEGAXUS_DB_MASTER')  
cursor = conn.cursor()  
cursor.execute("SELECT ID_COMUNA, REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(UPPER(DESCRIPCION),'ñ','&Ntilde;'),'á','&Aacute;'),'é','&Eacute;'),'í','&Iacute;'),'ó','&Oacute;'),'ú','&Uacute;') FROM PEGAXUS_COMUNAS_PROVINCIAS ORDER BY DESCRIPCION;")  
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

