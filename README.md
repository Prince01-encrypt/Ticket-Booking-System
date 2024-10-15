# Ticket Booking System

## Overview

The Ticket Booking System is a Python-based application designed to manage event ticket bookings. It allows users to create events, book tickets, cancel bookings, and check available tickets. The application interacts with a SQL Server database to store and retrieve event and booking data.

## Features

- **Create Events**: Users can create new events with details such as name, date, and total tickets available.
- **Book Tickets**: Users can book tickets for available events.
- **Cancel Tickets**: Users can cancel their bookings using a unique booking ID.
- **Check Available Tickets**: Users can check the number of tickets available for a specific event.

## Technologies Used

- **Python**: Programming language for application development.
- **SQL Server**: Database management system for data storage.
- **Exceptions Handling**: Custom exception classes for better error handling.
  
## Project Structure

TicketBookingSystem/ │ ├── dao/ │ ├── booking_system_repository.py # Data Access Object for managing bookings and events │ ├── entity/ │ ├── event.py # Event entity class │ ├── ticket.py # Ticket entity class │ └── booking.py # Booking entity class │ ├── exception/ │ └── exception.py # Custom exceptions for the application │ ├── util/ │ └── DBUtil.py # Database connection utility │ └── main.py # Main application file with menu-driven interface

For questions or feedback, please contact:

PRINCE PATEL: resonance443731@gmail.com
