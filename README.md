# Proyecto Urban Grocers 

### Nombre: José Luis Pacheco Santamaría
### Chort: 32

###### Pruebas para el funcionamiento de crear kit en Urban Grocers

###### El objetivo del proyecto es *automatizar* la búsqueda de errores al momento de crear un usuario y un kit para el usuario el cual está basado en la correcta captura del nombre del kit.

###### Para este fin se utilizó el programa *Python* el cual nos ayudó a crear las funciones e instrucciones necesarias para la correcta automatización de las pruebas, de igual manera se trabajó con los repositorios en Github para la correcta actualización de los cambios implementados en el código y así poder guardarlos.

### Se utilizaron diferentes archivos los cuales albergan la siguiente información:

####    * configuration.py: La cual contiene el vínculo y end points necesarios para la creación tanto del usuario como del kit.
    
####    * sender_stand_request.py: Contiene las funciones que se definieron para la creación del usuario y del kit de usuario, en el caso del kit de usuario también se solicitó una autorización para la creación del token único para cada usuario.
    
####    * data.py: Contiene los encabezados y cuerpos utilizados para las pruebas.
    
####    * create_kit_name_kit_test: Aquí se definen las pruebas que se automatizarán para encontrar errores en su funcionamiento.
    
## Las pruebas que se realizan en este test son las siguientes:

#### 1. Que el programa arroje un resultado 201 al crear un kit utilizando un nombre mínimo de 1 caracter.

#### 2. Que el programa arroje un resultado 201 al crear un kit un kit utilizando un nombre máximo de 511 caracteres.

#### 3. Que el programa arroje un resultado de error 400 al intentar crear un usuario dejando un espacio en blanco en apartado nombre.

#### 4. Que el programa arroje un resultado de error 400 al intentar crear un usuario utilizando 512 caracteres.

#### 5. Que el programa arroje un resultado 201 al utilizar caracteres especiales en el apartado de nombre.

#### 6. Que el programa arroje un resultado 201 al existir espacios en blanco entre caracteres.

#### 7. Que el programa arroje un resultado 201 al utilizar un string con caracteres numéricos en el apartado de nombre.

#### 8. Que el programa arroje un resultado 400 al no poner ningún caracter en el apartado nombre.

#### 9. Que el programa arroje un resultado 400 al utilizar valores numéricos en el apartado nombre.     

 




