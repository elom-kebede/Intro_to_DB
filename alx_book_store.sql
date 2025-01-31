CREATE DATABASE IF NOT EXISTS alx_book_store;

SHOW DATABASEs;

use alx_book_store;

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id),
    price DOUBLE,
    publication_date DATE
)

CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
)

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
)

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    Foreign Key (customer_id ) REFERENCES Customers(customer_id),
    order_date DATE

)

CREATE TABLE Order_Details (
    orderdetailid INT PRIMARY KEY,
    customer_id INT,
    Foreign Key (customer_id) REFERENCES Customers(customer_id),
    quantity DOUBLE
)

DROP TABLE order_details;

CREATE TABLE Order_Details (
    orderdetailid INT PRIMARY KEY,
    order_id INT,
    Foreign Key (order_id) REFERENCES Orders(order_id),
    book_id INT,
    Foreign Key (book_id) REFERENCES Books(book_id)
)

ALTER TABLE Order_Details
ADD quantity DOUBLE
