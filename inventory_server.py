from flask import Flask, render_template, request, jsonify
from inventorydao import ProductDAO  # your data access layer

app = Flask(__name__)

# ---- Frontend page ----
@app.route("/")
def inventory_page():
    # templates/inventory.html will link CSS via url_for('static', filename='style.css')
    return render_template("inventory.html")

# ---- API ----
@app.route("/api/products", methods=["GET"])
def get_products():
    products = ProductDAO.get_all()
    return jsonify(products), 200

@app.route("/api/products/search/id", methods=["GET"])
def search_by_id():
    product_id = request.args.get("id")
    if not product_id:
        return jsonify({"error": "Missing id parameter"}), 400
    try:
        product_id = int(product_id)
    except ValueError:
        return jsonify({"error": "ID must be an integer"}), 400

    product = ProductDAO.get_by_id(product_id)
    return jsonify([product] if product else []), 200

@app.route("/api/products/search/name", methods=["GET"])
def search_by_name():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "Missing name parameter"}), 400
    return jsonify(ProductDAO.get_by_name(name)), 200

@app.route("/api/products/search/description", methods=["GET"])
def search_by_description():
    desc = request.args.get("description")
    if not desc:
        return jsonify({"error": "Missing description parameter"}), 400
    return jsonify(ProductDAO.get_by_description(desc)), 200

@app.route("/api/products/search/category", methods=["GET"])
def search_by_category():
    cat = request.args.get("category")
    if not cat:
        return jsonify({"error": "Missing category parameter"}), 400
    return jsonify(ProductDAO.get_by_category(cat)), 200

@app.route("/api/products/search/supplier", methods=["GET"])
def search_by_supplier():
    supplier = request.args.get("supplier")
    if not supplier:
        return jsonify({"error": "Missing supplier parameter"}), 400
    return jsonify(ProductDAO.get_by_supplier(supplier) or []), 200

@app.route("/api/products/search/quantity", methods=["GET"])
def search_by_quantity():
    qty = request.args.get("quantity")
    if qty is None:
        return jsonify({"error": "Missing quantity parameter"}), 400
    try:
        quantity = int(qty)
    except ValueError:
        return jsonify({"error": "Quantity must be an integer"}), 400
    return jsonify(ProductDAO.get_by_quantity(quantity)), 200

@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    if not name:
        return jsonify({"error": "Missing product name"}), 400

    existing = ProductDAO.get_by_name(name)
    # handle either list or single dict return shapes
    exists = (isinstance(existing, list) and len(existing) > 0) or (isinstance(existing, dict) and existing)
    if exists:
        return jsonify({"error": "Product with this name already exists."}), 400

    product_id = ProductDAO.insert(data)
    return jsonify({"message": "Product added", "product_id": product_id}), 201

@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = ProductDAO.get_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json(silent=True) or {}
    updated = ProductDAO.update(product_id, data)
    if not updated:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"message": "Product updated"}), 200

@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    deleted = ProductDAO.delete(product_id)
    if not deleted:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"message": "Product deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)


