CREATE DATABASE TicketBookingSystem;
USE TicketBookingSystem;

CREATE TABLE Venue (
    venue_id INT IDENTITY(1,1) PRIMARY KEY,
    venue_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE Event (
    event_id INT IDENTITY(1,1) PRIMARY KEY,
    event_name VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL,
    event_time TIME NOT NULL,
    venue_id INT FOREIGN KEY REFERENCES Venue(venue_id),
    total_seats INT NOT NULL,
    available_seats INT NOT NULL,
    ticket_price DECIMAL(10, 2) NOT NULL,
    event_type VARCHAR(50) CHECK (event_type IN ('Movie', 'Sports', 'Concert'))
);

CREATE TABLE Customer (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(15) NOT NULL
);

CREATE TABLE Booking (
    booking_id INT IDENTITY(1,1) PRIMARY KEY,
    event_id INT FOREIGN KEY REFERENCES Event(event_id),
    customer_id INT FOREIGN KEY REFERENCES Customer(customer_id),
    num_tickets INT NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL,
    booking_date DATETIME DEFAULT GETDATE()
);
