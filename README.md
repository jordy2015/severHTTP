Instrucciones:
posicionese en "cd /home/$(whoami)"
copie en esa direccion la carpeta "paginas"
edite el archivo "MiServiciod" (cambie el valor de la variable "Iam" a su nombre de usuario).
copie el archivo "MiServiciod" a /etc/init.d/
Despues dar permisos al archivo "MiServiciod" con "chmod +x MiServiciod" 
por ultimo inicie servicio con "sudo /etc/init.d/MiServiciod start"

Listo!
