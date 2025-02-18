Este pequeño bloque de código se encarga de ejecutar una aplicación que guarda un checkpoint en el paso que el usuario desee, para que al vovler a cargar,
la aplicación sea capaz de restaurar su estado desde el paso que se guardó.


La primera vez que se corre el programa, esté será incapaz de encontrar un checkpoint, por lo que inicia en el paso 0, cada que avanza un paso se le pregunta al usuario si desea crear el checkpoint
![image](https://github.com/user-attachments/assets/888f43c7-ef7d-44a7-ab3a-480471b24581)



Cuando el usuario escribe 's', el programa crea el archivo checkpoint.pkl para guardar el proceso y prosigue con los demás pasos (10 pasos para terminar el programa)
Notesé que en el paso 6 el usuario guardó su proceso, por lo que es posible leer "Checkpoint guardado en 'checkpoint.pkl'"

![image](https://github.com/user-attachments/assets/94cc29b2-bdfa-49fa-a725-6d7e0f732c9a)



Después de guardar un checkpoint y terminar la ejecución, la proxima vez el proceso iniciara desde el checkpoint guardado:

![image](https://github.com/user-attachments/assets/9e1f52ff-9c5b-4ff9-8700-3794318b13ae)


