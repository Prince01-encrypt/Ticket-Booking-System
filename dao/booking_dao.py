from util.DB_util import DBUtil

class BookingDAO:
    def create_booking(self, event_id, customer_id, num_tickets, total_cost):
        conn = DBUtil.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Booking (event_id, customer_id, num_tickets, total_cost) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (event_id, customer_id, num_tickets, total_cost))
        conn.commit()
        cursor.close()
        conn.close()

    def get_booking_by_id(self, booking_id):
        conn = DBUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Booking WHERE booking_id = ?"
        cursor.execute(query, (booking_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    def cancel_booking(self, booking_id):
        conn = DBUtil.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Booking WHERE booking_id = ?"
        cursor.execute(query, (booking_id,))
        conn.commit()
        cursor.close()
        conn.close()
