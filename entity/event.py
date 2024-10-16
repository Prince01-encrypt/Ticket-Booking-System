class Event:
    def __init__(self, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_id = venue_id
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    def display_event_details(self):
        return (f"Event: {self.event_name}\nDate: {self.event_date}\nTime: {self.event_time}\n"
                f"Venue ID: {self.venue_id}\nAvailable Seats: {self.available_seats}/{self.total_seats}\n"
                f"Price: {self.ticket_price}\nType: {self.event_type}")
