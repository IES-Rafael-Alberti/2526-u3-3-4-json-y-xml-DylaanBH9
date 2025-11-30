[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MNhzxJmi)
# Práctica 3.4: JSON y XML

Apoyate en los siguientes recursos para realizar la práctica:

[U3: JSON](https://revilofe.github.io/section1/u03/practica/PROG-U3.-Practica004/)
[U3: XML](https://revilofe.github.io/section1/u03/practica/PROG-U3.-Practica005/)


## Ejercicios. 
Cada ejercicio en un archivo diferente.

## Entrega
1. Agregar en la carpeta `src` los programas (`json.py` renombrado a `gestion_usuarios_json.py`, `xml.py` renombrado a `gestion_usuarios_xml.py`, etc.)
2. Las pruebas unitarias en la carpeta `tests`
3. Mas abajo tienes un ejemplo de como entregar la práctica.
4. Recuerda que debes subir el enlace al repositorio en la tarea correspondiente del aula virtual.


---

# 3.4: XML y JSON

## Identificación de la Actividad
- **ID de la Actividad:** 3.4: XML y JSON
- **Módulo:** PROG
- **Unidad de Trabajo:** U3: Estructuras de datos
- **Fecha de Creación:** 29/11/25
- **Fecha de Entrega:** 30/11/25
- **Alumno(s):** 
  - **Nombre y Apellidos:** Dylan Bauti Huelva
  - **Correo electrónico:** dbauhue1708@g.educaand.es
  - **Iniciales del Alumno/Grupo:** DBH

## Descripción de la Actividad
Esta actividad consiste en el desarrollo de scripts en Python para manipular y transformar datos almacenados en formatos **JSON** y **XML**. El objetivo es comprender cómo procesar estas estructuras de datos comunes, realizar conversiones entre ambos formatos y aplicar operaciones (Crear, Leer, Actualizar, Borrar) sobre archivos persistentes.

Se han desarrollado cuatro programas principales:
1. **Conversión JSON a XML:** Lee un archivo JSON de usuarios y genera su equivalente en XML.
2. **Conversión XML a JSON:** Lee un archivo XML de usuarios y genera su equivalente en JSON.
3. **Gestión de Usuarios (JSON):** Realiza operaciones de actualización, inserción y borrado sobre un archivo JSON.
4. **Gestión de Usuarios (XML):** Realiza las mismas operaciones CRUD sobre un archivo XML.

## Instrucciones de Compilación y Ejecución
1. **Requisitos Previos:**
   - Tener instalado **Python 3.x**.
   - Disponer de la carpeta `otros` con los archivos de datos iniciales (`datos_usuarios_orig.json` y `datos_usuarios_orig.xml`).

2. **Pasos para Compilar el Código:**
   Python es un lenguaje interpretado, por lo que no requiere compilación explícita. Asegúrate de que la estructura de carpetas sea correcta (código fuente en la raíz o `src`, y datos en `otros`).

3. **Pasos para Ejecutar el Código:**
   Ejecuta los scripts desde la terminal en el directorio donde se encuentran los archivos `.py`:

   - **Conversión JSON a XML:**
     ```bash
     python convertir_json_xml.py
     ```
   - **Conversión XML a JSON:**
     ```bash
     python convertir_xml_json.py
     ```
   - **Gestión de Usuarios (JSON):**
     ```bash
     python gestion_usuarios_json.py
     ```
   - **Gestión de Usuarios (XML):**
     ```bash
     python gestion_usuarios_xml.py
     ```

4. **Ejecución de Pruebas:**
   Si se han implementado pruebas unitarias en la carpeta `tests`, se pueden ejecutar con:
   ```bash
   python -m unittest discover tests
   ```

## Desarrollo de la Actividad
### Descripción del Desarrollo
Para el desarrollo se han utilizado las librerías estándar de Python:
- `json`: Para la serialización y deserialización de objetos Python a formato JSON. Se manejan excepciones como `JSONDecodeError` para asegurar la robustez.
- `xml.etree.ElementTree`: Para el parseo y construcción de árboles XML. Se navega por los nodos para extraer información y se utilizan métodos como `SubElement` para construir nuevas estructuras.

**Estructura del código:**
- Cada script cuenta con una función `main()` que orquesta el flujo.
- Se han separado las responsabilidades en funciones auxiliares (`cargar_json`, `guardar_xml`, `actualizar_usuario`, etc.) para mejorar la legibilidad y reutilización.
- Se ha implementado un manejo de errores robusto (`try-except`) para gestionar archivos inexistentes o formatos corruptos.

### Código Fuente
Aquí se encuentran los enlaces a los archivos de código fuente en el repositorio:

- **Conversión:**
  - [convertir_json_xml.py](convertir_json_xml.py)
  - [convertir_xml_json.py](convertir_xml_json.py)
  
- **Gestión:**
  - [gestion_usuarios_json.py](gestion_usuarios_json.py)
  - [gestion_usuarios_xml.py](gestion_usuarios_xml.py)

### Ejemplos de Ejecución

#### 1. Conversión JSON a XML
- **Entrada:** `datos_usuarios_orig.json`
  ```json
  {"usuarios": [{"id": 1, "nombre": "Juan", "edad": 30}, ...]}
  ```
- **Salida Esperada:** Se genera el archivo `otros/datos_usuarios_convertido.xml` con la estructura `<usuarios><usuario><id>1</id>...</usuario>...</usuarios>`.

#### 2. Gestión de Usuarios (JSON)
Al ejecutar `gestion_usuarios_json.py`, el programa realiza secuencialmente:
1. **Lectura inicial:** Muestra a Juan (30) y Ana (25).
2. **Actualización:** Cambia la edad del usuario con ID 1 a 31.
3. **Inserción:** Añade al usuario Pedro (ID 3, Edad 40).
4. **Eliminación:** Borra al usuario con ID 2 (Ana).
5. **Guardado:** Sobrescribe el archivo original con los cambios finales.

- **Salida en consola:**
  ```text
  --- Contenido Actual del Json ---
  ID: 1, Nombre: Juan, Edad: 30
  ...
  Usuario con ID 1 actualizado.
  Usuario Pedro añadido con éxito.
  Usuario con ID 2 eliminado.
  ```

## Conclusiones
La práctica permite mejorar el conocimiento sobre la manipulación de archivos de texto estructurados en Python. Se ha comprobado la facilidad de uso de la librería `json` frente a la estructura más verbosa necesaria para manipular `XML` con `ElementTree`. La implementación de funciones modulares y el manejo de excepciones son claves para crear herramientas de conversión de datos fiables.

## Referencias y Fuentes
- [Documentación oficial Python (JSON)](https://docs.python.org/3/library/json.html)
- [Documentación oficial Python (xml.etree.ElementTree)](https://docs.python.org/3/library/xml.etree.elementtree.html)