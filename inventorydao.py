from inventory_config import get_conn
from datetime import datetime

class ProductDAO:
    
    def get_all():
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM product ORDER BY name ASC ")
                return cursor.fetchall()
        finally:
            conn.close()

    def get_by_id(product_id):
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM product WHERE id = %s", (product_id,))
                return cursor.fetchone()
        finally:
            conn.close()

    
    def get_by_name(name):
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
                query = "SELECT * FROM product WHERE name LIKE %s ORDER BY name ASC"
                like_pattern = f"%{name}%"
                cursor.execute(query, (like_pattern,))
                return cursor.fetchall()
        finally:
            conn.close()

    def get_by_description(description):
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
                query = "SELECT * FROM product WHERE description LIKE %s ORDER BY name ASC"
                like_pattern = f"%{description}%"
                cursor.execute(query, (like_pattern,))
                return cursor.fetchall()
        finally:
            conn.close() 

    
    def get_by_category(category):
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
                query = "SELECT * FROM product WHERE category LIKE %s ORDER BY name ASC"
                like_pattern = f"%{category}%"
                cursor.execute(query, (like_pattern,))
                return cursor.fetchall()
        finally:
            conn.close()  

    def get_by_supplier(supplier):
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
                query = "SELECT * FROM product WHERE supplier LIKE %s ORDER BY name ASC"
                like_pattern = f"%{supplier}%"
                cursor.execute(query, (like_pattern,))
                return cursor.fetchall()
        finally:
            conn.close()           

    def get_by_quantity(quantity):
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM product WHERE quantity <= %s ORDER BY name ASC", (quantity,))
                return cursor.fetchall()
        finally:
            conn.close()




    def insert(data):
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
                # First, check if a product with the same name already exists
                sql_check = "SELECT COUNT(*) FROM product WHERE name = %s"
                cursor.execute(sql_check, (data['name'],))
                result = cursor.fetchone()
                if result[0] > 0:
                    return {"error": "Product with this name already exists."}, 400  # Handle duplicate product name
                
                # If no duplicate, proceed with inserting the new product
                sql = """
                    INSERT INTO product (name, description, quantity, category, price, supplier)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                values = (
                    data['name'],
                    data.get('description'),
                    data.get('quantity', 0),
                    data.get('category'),
                    data.get('price'),
                    data.get('supplier')
                )
                cursor.execute(sql, values)
                conn.commit()
                return {"message": "Product added", "product_id": cursor.lastrowid}, 201  # Return success with product ID

        finally:
            conn.close()

    def update(product_id, data):
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
                sql = """
                    UPDATE product
                    SET name=%s, description=%s, quantity=%s, category=%s, price=%s, supplier=%s, updated_at=%s
                    WHERE id=%s
                """
                values = (
                    data['name'],
                    data.get('description'),
                    data['quantity'],
                    data.get('category'),
                    data.get('price'),
                    data.get('supplier'),
                    datetime.now(),
                    product_id
                )
                cursor.execute(sql, values)
                conn.commit()
                return cursor.rowcount
        finally:
            conn.close()

    
    def delete(product_id):
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
                conn.commit()
                return cursor.rowcount
        finally:
            conn.close()


