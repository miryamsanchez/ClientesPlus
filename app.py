from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from model import Cliente
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def index():
    search_query = request.args.get('search', '').lower()
    _page = int(request.args.get('_page', 1))

    if search_query:
        clientes = [cliente for cliente in Cliente.todos() if search_query in cliente.nombre.lower()]
    else:
        clientes = list(Cliente.todos())

    PAGE_SIZE = 15

    num_clientes = len(clientes)
    num_pages = (num_clientes + PAGE_SIZE - 1) // PAGE_SIZE
    clientes_paginados = clientes[(_page - 1) * PAGE_SIZE:_page * PAGE_SIZE]

    start_page = max(1, (_page - 1) // 3 * 3 + 1)
    end_page = min(num_pages, (_page - 1) // 3 * 3 + 4)
    pages = range(start_page, end_page)

    return render_template('clientes.html', clientes=clientes_paginados, pages=pages, _page=_page, num_pages=num_pages, search_query=search_query)

@app.route('/clientes/<int:id>')
def detalle_cliente(id):
    cliente = Cliente.buscar(id)
    return render_template('detalle_cliente.html', cliente=cliente)

@app.route('/editar_cliente/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = Cliente.buscar(id)
    if cliente:
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellidos = request.form['apellidos']
            # Obtiene más datos del formulario y actualiza el cliente
            Cliente.editar(id, nombre=nombre, apellidos=apellidos)
            return redirect(url_for('index'))
        return render_template('editar_cliente.html', cliente=cliente)
    else:
        return "Cliente no encontrado"  # Puedes personalizar este mensaje según tu necesidad

@app.route('/nuevo_cliente', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'GET':
        return render_template('nuevo_cliente.html')  # Mostrar el formulario de creación
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        sexo = request.form['sexo']
        email = request.form['email']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        pais = request.form['pais']
        
        # Llama a la función nuevo en la clase Cliente para crear un nuevo cliente
        Cliente.nuevo(nombre=nombre, apellidos=apellidos, sexo=sexo, email=email,
                      telefono=telefono, direccion=direccion, ciudad=ciudad, pais=pais)
        
        return redirect(url_for('index'))  # Redirigir a la página de inicio """
        
@app.route('/eliminar_cliente/<int:id>')
def eliminar_cliente(id):
    if Cliente.eliminar(id):
        return redirect(url_for('index'))
    else:
        return "Cliente no encontrado"  # Puedes personalizar este mensaje según tu necesidad


if __name__ == '__main__':
    app.run(debug=True)