# Jugando con Python - Playing with Python


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

