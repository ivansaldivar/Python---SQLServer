# Probando Python con SQLServer


Este fue mi primer acercamiento a Python. Y me asombró su versatilidad, en una tarde probé un conjunto de características 
de este lenguaje y entre ellas como conectarlo con SQLServer. Iré agregando código que les simplifique su aprendizaje de
este lenguaje (interprete) y sus potencialidades. Por ahora le dejo esta pequeña referencia para trabajar con la base de datos
de Microsoft:


# Conectando Python a SQLServer
Antes de realizar las pruebas y posibilidades que este interprete nos ofrece para trabajar con SQLServer deberemos instalar 
el módulo Python correspondiente, para ello deberemos ejecutar la línea de comando el scrip instalador de paquetes python PIP, 
o bien desde el IDE de Visual Studio realizar la operación de carga. Para más detalles revisen el siguiente link:
https://docs.microsoft.com/en-us/sql/connect/python/python-driver-for-sql-server.

Los pasos que se deben serguir son:
    - Instalar Python runtime y pip package manager
        * a. Ir a python.org
        * b. hacer clic en el instalador apropiado de Windows (installer msi link).
        * c. Una vez descargado Once downloaded run the msi to install Python runtime

    - Descargar el módulo pymssql desde el siguiente link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
        * Asegúrese de escoger el correcto archivo whl. Por ejemplo: si estas usando Python 3.6 en una máquina de 64 bit, selecciona: pymssql‑2.1.3‑cp36‑cp36m‑win_amd64.whl. 
        * Una vez descargado, déja el archivo .whl en la ruta de .whl de los binarios de Python36.
        * Ejecuta la línea de comando (cmd.exe)
        * Instala el módulo pymssql 
            > pip install pymssql‑2.1.3‑cp36‑cp36m‑win_amd64.whl

![](https://raw.githubusercontent.com/ivansaldivar/Python---SQLServer/master/conectando_python_con_sqlserver.png)


# Prueba de concepto conectando a SQL usando pymssql

Paso 1: conecta
La función pymssql.connect se usa para conectarse a la base de datos SQL.
        
    - PYTHON
        import pymssql  
        conn = pymssql.connect(
                server='DAVINCI_DAEMOND\SAURON', 
                user='sa', 
                password='paulina', 
                database='PEGAXUS_DB_MASTER')  
        

Paso 2: ejecutar la consulta
La función cursor.execute se puede usar para recuperar un conjunto de resultados de una consulta en una base de datos SQL. Esta función acepta esencialmente cualquier consulta y devuelve un conjunto de resultados que puede iterarse con el uso de cursor.fetchone ().

    - PYTHON
        import pymssql  
        conn = pymssql.connect(
                server='DAVINCI_DAEMOND\SAURON', 
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
        
Paso 3: inserta una fila
En este ejemplo, verá cómo ejecutar una instrucción INSERT de forma segura, pasar parámetros que protegen su aplicación del valor de inyección de SQL.

    - PYTHON
        import pymssql  
        conn = pymssql.connect(
                server='DAVINCI_DAEMOND\SAURON', 
                user='sa', 
                password='paulina', 
                database='PEGAXUS_DB_MASTER') 

        cursor = conn.cursor()  
        cursor.execute("INSERT PEGAXUS_DB_MASTER.PEGAXUS_COMUNAS_PROVINCIAS (ID_COMUNA, DESCRIPCION) OUTPUT INSERTED.ID_COMUNA VALUES ('99999', 'MI COMUNA')")  
        
        row = cursor.fetchone()  
        while row:  
                print "Inserted ID_COMUNA : " +str(row[0])  
                row = cursor.fetchone()  
        conn.commit()
        conn.close()
