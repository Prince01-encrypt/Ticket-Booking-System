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
  
## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd TicketBookingSystem
2.Install Required Packages: Make sure you have Python installed. You may need to install additional packages, such as pyodbc, for SQL Server connections:
  pip install pyodbc

3.Configure Database Connection: Update the DBUtil.py file with your SQL Server connection details if necessary.

4.Run the Application:
  python main.py

For questions or feedback, please contact:

PRINCE PATEL: resonance443731@gmail.com
