from flask import Flask, render_template, request, redirect, url_for
from model import Cliente

app = Flask(__name__)

@app.route('/')
def index():
    # Obtener parámetros de búsqueda y paginación de la URL
    search_query = request.args.get('search', '').lower()
    _page = int(request.args.get('_page', 1))

    # Filtrar clientes según la consulta de búsqueda o mostrar todos
    if search_query:
        clientes = Cliente.filtrar(nombre=search_query)
    else:
        clientes = Cliente.todos()

    # Configuración de paginación
    PAGE_SIZE = 15
    start_idx = (_page - 1) * PAGE_SIZE

    # Obtener clientes paginados usando el generador
    clientes_paginados = []
    for _ in range(start_idx):
        next(clientes, None)  # Consumir elementos hasta llegar al índice de inicio
    for _ in range(PAGE_SIZE):
        cliente = next(clientes, None)
        if cliente is None:
            break
        clientes_paginados.append(cliente)

    num_clientes = start_idx + len(clientes_paginados)
    num_pages = (num_clientes + PAGE_SIZE - 1) // PAGE_SIZE
    start_page = max(1, (_page - 1) // 3 * 3 + 1)
    end_page = min(num_pages, (_page - 1) // 3 * 3 + 4)
    pages = range(start_page, end_page)

    # Renderizar la plantilla HTML con los datos y la paginación
    return render_template('clientes.html', clientes=clientes_paginados, pages=pages, _page=_page, num_pages=num_pages, search_query=search_query)

@app.route('/clientes/<int:id>')
def detalle_cliente(id):
    # Obtener los detalles del cliente por su ID
    cliente = Cliente.buscar(id)
    return render_template('detalle_cliente.html', cliente=cliente)

@app.route('/editar_cliente/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    # Obtener los detalles del cliente a editar
    cliente = Cliente.buscar(id)
    if cliente:
        if request.method == 'POST':
            # Obtener los valores del formulario y actualizar el cliente
            nombre = request.form['nombre']
            apellidos = request.form['apellidos']
            sexo = request.form['sexo']
            email = request.form['email'] 
            telefono = request.form['telefono'] 
            direccion = request.form['direccion'] 
            ciudad = request.form['ciudad']   
            pais = request.form['pais']   
            Cliente.editar(id, nombre=nombre, apellidos=apellidos, sexo=sexo, email=email, telefono=telefono, direccion=direccion, ciudad=ciudad, pais=pais)
            return redirect(url_for('index'))
        return render_template('editar_cliente.html', cliente=cliente)
    else:
        return "Cliente no encontrado"

@app.route('/nuevo_cliente', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        # Crear un nuevo cliente con los datos del formulario
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        sexo = request.form['sexo']
        email = request.form['email']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        pais = request.form['pais']
        Cliente.nuevo(nombre=nombre, apellidos=apellidos, sexo=sexo, email=email, telefono=telefono, direccion=direccion, ciudad=ciudad, pais=pais)
        return redirect(url_for('index'))
    return render_template('nuevo_cliente.html')

@app.route('/eliminar_cliente/<int:id>')
def eliminar_cliente(id):
    # Eliminar un cliente por su ID
    if Cliente.eliminar(id):
        return redirect(url_for('index'))
    else:
        return "Cliente no encontrado"

if __name__ == '__main__':
    app.run(debug=True)
