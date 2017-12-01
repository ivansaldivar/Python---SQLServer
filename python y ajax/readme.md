# Configurando asignación de controlador para Python en IIS

A continuación verán una secuencia de figurás que muestran como asignar un controlador en IIS para poder ejecutar script Python 
desde aplicaciones WEB.
El ejemplo que se utilizó está basado en AJAX. Primero ejecutaremos un script Python desde el navegador de acuerdo a la ruta que hayamos creado en el IIS, este cargará una página HTML en la cual se definirán algunas funciones en javascript que cargarán en forma dinámica el contenido de un objeto html LABEL con el retorno que resulte de la ejecución de otro script Python, que se conecta a una base SQLServer y quc consulta una tabla. Veamos los pasos para lograr lo indicado:

# 1. Creando una aplicación virtual en el IIS para nuestra aplicación en Python
![](https://raw.githubusercontent.com/ivansaldivar/Python---SQLServer/master/python%20y%20ajax/IIS%20-%20Administrar%20Python%20-1.png)

# 2. Configurando la asignación de controlador para script Python
![](https://raw.githubusercontent.com/ivansaldivar/Python---SQLServer/master/python%20y%20ajax/IIS%20-%20Administrar%20Python%20-2.png)

# 3. Creando la asignación de script para Python
![](https://raw.githubusercontent.com/ivansaldivar/Python---SQLServer/master/python%20y%20ajax/IIS%20-%20Administrar%20Python%20-3.png)
Noten que se debe asignar el ejecutable del interprete Python y asociarlo a los archivos de extensión *.PY (https://support.microsoft.com/es-es/help/276494/using-python-scripts-with-iis)

# 4. Ejecutando nuestro script Python desde la ruta WEB de nuestra aplicación
![](https://raw.githubusercontent.com/ivansaldivar/Python---SQLServer/master/python%20y%20ajax/IIS%20-%20Administrar%20Python%20-4.png)
Como documento predeterminado asignamos el archivo index.py que esta en la carpeta del proyecto "Python y ajax"

# 5. Ejecutando el llamado AJAX
![](https://raw.githubusercontent.com/ivansaldivar/Python---SQLServer/master/python%20y%20ajax/IIS%20-%20Administrar%20Python%20-5.png)

![](https://raw.githubusercontent.com/ivansaldivar/Python---SQLServer/master/python%20y%20ajax/IIS%20-%20Administrar%20Python%20-6.png)
Como apreciamos al hacer clic en el botón "Clic para cargar datos", se produce el llamado ajax que ejecutará el script Python 
module1.py que implementa una conexión al SQLServer y luego ejecuta una consulta específica, retornándose el listado de los
campos solicitados (listado de comunas). Acá no explicaremos lo que es ajax, ni como se implementa, pues asumiremos que ustedes
ya conocen esta tecnología, pero aquí les dejo un link si no conocían o no han sabían de AJAX: https://www.w3schools.com/js/js_ajax_intro.asp
