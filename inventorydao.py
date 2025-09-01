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
            with conn.cursor() as cur:
                # Duplicate check (alias the count to a stable name)
                cur.execute("SELECT COUNT(*) AS cnt FROM product WHERE name=%s", (data['name'],))
                row = cur.fetchone()
                if row is None:
                    raise RuntimeError("Duplicate check failed (no row)")

                # Row can be a dict (DictCursor) or a tuple (regular cursor)
                cnt = row['cnt'] if isinstance(row, dict) else row[0]
                if cnt > 0:
                    raise ValueError("DUPLICATE_NAME")

                # Insert
                sql = """
                    INSERT INTO product (name, description, quantity, category, price, supplier)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                vals = (
                    data.get('name'),
                    data.get('description'),
                    int(data.get('quantity') or 0),
                    data.get('category'),
                    float(data.get('price') or 0),
                    data.get('supplier')
                )
                cur.execute(sql, vals)

                if cur.rowcount != 1:
                    raise RuntimeError(f"INSERT affected {cur.rowcount} rows")

                conn.commit()
                new_id = getattr(cur, "lastrowid", None)
                if new_id is None:
                    # Some drivers keep lastrowid on the connection
                    new_id = getattr(conn, "insert_id", None)
                return new_id
        except Exception:
            conn.rollback()
            raise
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


