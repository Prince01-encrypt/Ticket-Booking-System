from util.DB_util import DBUtil

class EventDAO:
    def create_event(self, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type):
        conn = DBUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type))
        conn.commit()
        cursor.close()
        conn.close()

    def get_event_by_id(self, event_id):
        conn = DBUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Event WHERE event_id = ?"
        cursor.execute(query, (event_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result
