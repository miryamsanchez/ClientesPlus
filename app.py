from flask import Flask, render_template, request, send_from_directory
from model import Cliente
from pathlib import Path

#app = Flask(__name__, static_url_path='/static', static_folder='fontello-ec2f3e69')


app = Flask(__name__)

# Cargar datos de clientes desde un archivo CSV
Cliente.cargar_datos(Path('data') / 'clientes.csv')

""" #Ruta para servir archivos estáticos de Fontello
@app.route('/static/<path:path>')
def send_fontello(path):
    return send_from_directory('fontello-ec2f3e69', path) """

@app.route('/')
def index():
    # Obtener parámetros de búsqueda de la URL
    search_query = request.args.get('search', '').lower()
    _page = int(request.args.get('_page', 1))

    # Filtrar clientes según la consulta de búsqueda o obtener todos los clientes
    if search_query:
        clientes = [cliente for cliente in Cliente.todos() if search_query in cliente.nombre.lower()]
    else:
        clientes = list(Cliente.todos())

    # Define el tamaño de página deseado
    PAGE_SIZE = 15
    
    # Calcular la paginación
    num_clientes = len(clientes)
    num_pages = (num_clientes + PAGE_SIZE - 1) // PAGE_SIZE
    clientes_paginados = clientes[(_page - 1) * PAGE_SIZE:_page * PAGE_SIZE]

    # Calcular las páginas para la paginación
    start_page = max(1, (_page - 1) // 3 * 3 + 1)
    end_page = min(num_pages, (_page - 1) // 3 * 3 + 4)
    pages = range(start_page, end_page)

    # Renderizar la plantilla 'clientes.html' con los datos necesarios
    return render_template('clientes.html', clientes=clientes_paginados, pages=pages, _page=_page, num_pages=num_pages, search_query=search_query)



@app.route('/clientes/<int:id>')
def detalle_cliente(id):
    # Cargar un cliente específico desde el modelo
    cliente = Cliente.buscar(id)

    # Renderizar la plantilla 'detalle_cliente.html' con los datos del cliente
    return render_template('detalle_cliente.html', cliente=cliente)

#Ruta para eliminar un cliente por ID
@app.route('eliminar_cliente/<int:id>')
def eliminar_cliente(id):
    return redirect(url_for('clientes'))



if __name__ == '__main__':
    app.run(debug=True)