from util.DB_util import DBUtil

class VenueDAO:
    def create_venue(self, venue_name, address):
        conn = DBUtil.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Venue (venue_name, address) VALUES (?, ?)"
        cursor.execute(query, (venue_name, address))
        conn.commit()
        cursor.close()
        conn.close()

    def get_venue_by_id(self, venue_id):
        conn = DBUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Venue WHERE venue_id = ?"
        cursor.execute(query, (venue_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result
