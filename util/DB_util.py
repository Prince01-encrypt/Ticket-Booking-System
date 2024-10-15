import pyodbc

class DBUtil:
    @staticmethod
    def get_connection():
        try:
            connection = pyodbc.connect(
                'Driver={SQL Server};'
                'Server=PRINCE\\SQLEXPRESS;'  
                'Database=TicketBookingSystem;'
                'Trusted_Connection=yes;'
            )
            return connection
        except pyodbc.Error as e:
            print("Error while connecting to the database:", e)
            return None
