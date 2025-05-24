from inventory_config import get_conn
from datetime import datetime

class ProductDAO:
    
    def get_all():
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM product")
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

    def insert(data):
        conn = get_conn()
        try:
            with conn.cursor() as cursor:
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
                return cursor.lastrowid
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


