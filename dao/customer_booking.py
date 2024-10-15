from util.DB_util import DBUtil

class CustomerDAO:
    def create_customer(self, customer_name, email, phone_number):
        conn = DBUtil.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Customer (customer_name, email, phone_number) VALUES (?, ?, ?)"
        cursor.execute(query, (customer_name, email, phone_number))
        conn.commit()
        cursor.close()
        conn.close()

    def get_customer_by_id(self, customer_id):
        conn = DBUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Customer WHERE customer_id = ?"
        cursor.execute(query, (customer_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result
