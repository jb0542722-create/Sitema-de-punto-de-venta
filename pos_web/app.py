from flask import Flask, jsonify, render_template, request, session
import os

app = Flask(__name__)
# Es necesario configurar una clave secreta para usar sesiones en Flask
app.secret_key = os.urandom(24)

# Inventario de productos (en un entorno real, esto vendría de una base de datos)
inventario = [
    {"id": 1, "nombre": "Manzana", "precio": 0.5},
    {"id": 2, "nombre": "Pan", "precio": 1.5},
    {"id": 3, "nombre": "Leche", "precio": 2.0},
    {"id": 4, "nombre": "Cereal", "precio": 3.0},
    {"id": 5, "nombre": "Huevo", "precio": 0.25}
]

@app.route('/')
def index():
    """Sirve la página principal de la aplicación."""
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    """Devuelve la lista de productos disponibles."""
    return jsonify(inventario)

@app.route('/api/cart', methods=['GET'])
def get_cart():
    """Devuelve el contenido del carrito de la sesión."""
    return jsonify(session.get('cart', []))

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    """Añade un producto al carrito en la sesión."""
    data = request.json
    product_id = data.get('id')

    if not product_id:
        return jsonify({"error": "Falta el ID del producto"}), 400

    producto_a_anadir = next((p for p in inventario if p['id'] == product_id), None)

    if not producto_a_anadir:
        return jsonify({"error": "Producto no encontrado"}), 404

    # Inicializa el carrito en la sesión si no existe
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(producto_a_anadir)
    session.modified = True  # Marcar la sesión como modificada

    return jsonify(session['cart'])

if __name__ == '__main__':
    app.run(debug=True, port=5001)
