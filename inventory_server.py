from flask import Flask, request, jsonify, send_from_directory
from inventorydao import ProductDAO  # Assuming this contains all the data access methods
import os

app = Flask(__name__)

# Serve the HTML file for the frontend
@app.route('/')
def serve_index():
    return send_from_directory('static', 'inventory.html')

# Get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    products = ProductDAO.get_all()
    return jsonify(products)

# Search products by ID
@app.route('/api/products/search/id', methods=['GET'])
def search_by_id():
    product_id = request.args.get('id')
    if not product_id:
        return jsonify({'error': 'Missing id parameter'}), 400
    try:
        product_id = int(product_id)
    except ValueError:
        return jsonify({'error': 'ID must be an integer'}), 400
    product = ProductDAO.get_by_id(product_id)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

# Search products by name
@app.route('/api/products/search/name', methods=['GET'])
def search_by_name():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Missing name parameter'}), 400
    return jsonify(ProductDAO.get_by_name(name))

# Search products by description
@app.route('/api/products/search/description', methods=['GET'])
def search_by_description():
    desc = request.args.get('description')
    if not desc:
        return jsonify({'error': 'Missing description parameter'}), 400
    return jsonify(ProductDAO.get_by_description(desc))

# Search products by category
@app.route('/api/products/search/category', methods=['GET'])
def search_by_category():
    cat = request.args.get('category')
    if not cat:
        return jsonify({'error': 'Missing category parameter'}), 400
    return jsonify(ProductDAO.get_by_category(cat))

# Search products by supplier
@app.route('/api/products/search/supplier', methods=['GET'])
def search_by_supplier():
    supplier = request.args.get('supplier')
    if not supplier:
        return jsonify({'error': 'Missing supplier parameter'}), 400
    return jsonify(ProductDAO.get_by_supplier(supplier))

# Search products by quantity
@app.route('/api/products/search/quantity', methods=['GET'])
def search_by_quantity():
    qty = request.args.get('quantity')
    if qty is None:
        return jsonify({'error': 'Missing quantity parameter'}), 400
    try:
        quantity = int(qty)
    except ValueError:
        return jsonify({'error': 'Quantity must be an integer'}), 400
    return jsonify(ProductDAO.get_by_quantity(quantity))

# Add a new product
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing product name'}), 400
    
    existing_product = ProductDAO.get_by_name(data['name'])
    if existing_product:
        return jsonify({'error': 'Product with this name already exists.'}), 400

    product_id = ProductDAO.insert(data)
    return jsonify({'message': 'Product added', 'product_id': product_id}), 201

# Get product by ID for editing
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductDAO.get_by_id(product_id)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

# Update product details
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    updated = ProductDAO.update(product_id, data)
    if updated:
        return jsonify({'message': 'Product updated'})
    return jsonify({'error': 'Product not found'}), 404

# Delete a product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    deleted = ProductDAO.delete(product_id)
    if deleted:
        return jsonify({'message': 'Product deleted'})
    return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

