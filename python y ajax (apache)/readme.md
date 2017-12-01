# Configurando APACHE para ejecutar script Python en Navegador WEB

A continuación verán dos figurás que muestran como configurar APACHE para poder ejecutar script Python en un navegador WEB.
El ejemplo es el mismo que se puede observar en el directorio "python y ajax". La diferencia en los script de Python para 
poder ejecutar en APACHE, con respecto a su versión en IIS, es que a estos se les debe agregar al inicio la ruta del binario
del interprete de Python, por ejemplo en los fuentes que revisen en el repositorio la ruta correspondió a la siguiente línea de 
código:

    #!C:/Program Files/Python36/python.exe
    
Recordar, que en ambos casos estamos implementando en plataforma windows. Para ejecutar APACHE, usamos la instalación que se
obtiene usando WAMPServer (http://www.wampserver.com/en/). Luego en la ruta de wamp que se aprecia en la siguiente imagen creamos
un directorio que contenía los fuentes para probar los script de Python:

![](https://raw.githubusercontent.com/ivansaldivar/Python---SQLServer/master/python%20y%20ajax%20(apache)/Configuracion%20de%20apache%20para%20ejecutar%20Python%20-%203.png)


# Modificaciones a archivo httpd.conf de APACHE
Las líneas que se indican en las siguientes imágenes son las que se deben agregar al archivo de configuración del servidor APACHE
para que los script de Python se ejecuten correctamente en el navegador:

![](https://raw.githubusercontent.com/ivansaldivar/Python---SQLServer/master/python%20y%20ajax%20(apache)/Configuracion%20de%20apache%20para%20ejecutar%20Python%20-%201.png)

![](https://raw.githubusercontent.com/ivansaldivar/Python---SQLServer/master/python%20y%20ajax%20(apache)/Configuracion%20de%20apache%20para%20ejecutar%20Python%20-%202.png)
