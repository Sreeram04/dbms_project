CREATE DATABASE IF NOT EXISTS HotelDB;
USE HotelDB;

DROP TABLE IF EXISTS hotel;
DROP TABLE IF EXISTS room;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS password_hotel;

CREATE TABLE hotel(
room_id INT NOT NULL,
room_type VARCHAR(30) NOT NULL,
cost INT NOT NULL,
room_remaining INT NOT NULL,
PRIMARY KEY(room_id));

CREATE TABLE room(
room_no INT NOT NULL,
room_id INT NOT NULL,
room_status VARCHAR(30) NOT NULL,
PRIMARY KEY(room_no),
FOREIGN KEY(room_id) REFERENCES hotel(room_id));

CREATE TABLE customer(
customer_id INT NOT NULL,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
room_no INT NOT NULL,
phone INT NOT NULL,
cust_status VARCHAR(30) NOT NULL,
PRIMARY KEY(sl_no),
FOREIGN KEY(room_no) REFERENCES room(room_no));

CREATE TABLE staff(
staff_id INT NOT NULL,
staff_name VARCHAR(30) NOT NULL,
salary INT NOT NULL,
designation VARCHAR(30) NOT NULL,
PRIMARY KEY(staff_id));

CREATE TABLE password_hotel(
password_staff INT NOT NULL,
staff_id INT NOT NULL,
FOREIGN KEY(staff_id) REFERENCES staff(staff_id));


INSERT INTO hotel
VALUES
  (101,'Single Non-AC',2100,9),
  (102,'Single AC',2500,7),
  (103,'Double Non-AC',3200,8),
  (104,'Double AC',3700,3),
  (105,'Deluxe Non-AC',4200,2),
  (106,'Deluxe AC',4600,4),
  (107,'Suite',8000,1);
