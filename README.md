Sistema de Gestión de Clientes
Este proyecto es una aplicación web de Sistema de Gestión de Clientes construida con Flask. Permite administrar información de clientes, como su nombre, apellidos, género, correo electrónico, teléfono, dirección, ciudad y país. La aplicación incluye funcionalidades de búsqueda, paginación y edición de clientes.

Características
Listar todos los clientes con opciones de búsqueda y paginación.
Ver los detalles de un cliente específico.
Editar la información de un cliente existente.
Agregar nuevos clientes al sistema.
Eliminar clientes de la base de datos.
Requisitos
Python 3.x
Flask
Plantillas HTML (se utilizan para renderizar las páginas web)
Instalación
Clona este repositorio en tu máquina local:
git clone https://github.com/tu_usuario/tu_repositorio.git
Instala las dependencias necesarias. Abre una terminal y navega hasta la carpeta del proyecto. Luego, ejecuta el siguiente comando:
pip install -r requirements.txt
Uso
Navega a la carpeta del proyecto en tu terminal:
cd ruta/hacia/la/carpeta/proyecto
Ejecuta la aplicación Flask:
python app.py
Abre tu navegador web y visita http://localhost:5000 para acceder a la aplicación.

Estructura del Proyecto
app.py: Contiene la lógica principal de la aplicación Flask.
model.py: Define la clase Cliente utilizada para manejar los datos de los clientes.
templates/: Carpeta que contiene las plantillas HTML utilizadas para renderizar las páginas web.
static/: Carpeta para almacenar archivos estáticos, como hojas de estilo CSS, imágenes, etc.