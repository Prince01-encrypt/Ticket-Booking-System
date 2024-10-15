from dao.event_dao import EventDAO
from dao.customer_booking import CustomerDAO
from dao.booking_dao import BookingDAO
from dao.venue_dao import VenueDAO
from exception.EventNotFoundException import EventNotFoundException
from exception.InvalidBookingIDException import InvalidBookingIDException

def main():
    event_dao = EventDAO()
    customer_dao = CustomerDAO()
    booking_dao = BookingDAO()
    venue_dao = VenueDAO()

    while True:
        print("\n--- Ticket Booking System ---")
        print("1. Create Venue")
        print("2. Create Event")
        print("3. Register Customer")
        print("4. Book Tickets")
        print("5. Cancel Booking")
        print("6. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            venue_name = input("Enter venue name: ")
            address = input("Enter address: ")
            venue_dao.create_venue(venue_name, address)
            print("Venue created successfully!")

        elif choice == 2:
            event_name = input("Enter event name: ")
            event_date = input("Enter event date (YYYY-MM-DD): ")
            event_time = input("Enter event time (HH:MM:SS): ")
            venue_id = int(input("Enter venue ID: "))
            total_seats = int(input("Enter total seats: "))
            available_seats = total_seats
            ticket_price = float(input("Enter ticket price: "))
            event_type = input("Enter event type (Movie, Sports, Concert): ")
            event_dao.create_event(event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type)
            print("Event created successfully!")

        elif choice == 3:
            customer_name = input("Enter customer name: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            customer_dao.create_customer(customer_name, email, phone_number)
            print("Customer registered successfully!")

        elif choice == 4:
            event_id = int(input("Enter event ID: "))
            customer_id = int(input("Enter customer ID: "))
            num_tickets = int(input("Enter number of tickets: "))
            ticket_price = float(input("Enter ticket price: "))
            total_cost = num_tickets * ticket_price
            booking_dao.create_booking(event_id, customer_id, num_tickets, total_cost)
            print("Booking successful!")

        elif choice == 5:
            booking_id = int(input("Enter booking ID: "))
            try:
                booking_dao.get_booking_by_id(booking_id)
                booking_dao.cancel_booking(booking_id)
                print("Booking canceled successfully!")
            except InvalidBookingIDException:
                print("Invalid Booking ID!")

        elif choice == 6:
            print("Exiting the system...")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
