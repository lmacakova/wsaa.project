from flask import Flask, request, jsonify, send_from_directory
from inventorydao import ProductDAO
import os

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('static', 'inventory.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    products = ProductDAO.get_all()
    return jsonify(products)



@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductDAO.get_by_id(product_id)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404



@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing product name'}), 400

    product_id = ProductDAO.insert(data)
    return jsonify({'message': 'Product added', 'product_id': product_id}), 201



@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    updated = ProductDAO.update(product_id, data)
    if updated:
        return jsonify({'message': 'Product updated'})
    return jsonify({'error': 'Product not found'}), 404



@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    deleted = ProductDAO.delete(product_id)
    if deleted:
        return jsonify({'message': 'Product deleted'})
    return jsonify({'error': 'Product not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)
