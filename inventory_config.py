import pymysql

def get_conn():
    return pymysql.connect(
        host="127.0.0.1",
        port= 3308,
        user="root",           
        password="Lucia",    
        database="inventory",
        cursorclass=pymysql.cursors.DictCursor  # return results as dictionaries
    )
