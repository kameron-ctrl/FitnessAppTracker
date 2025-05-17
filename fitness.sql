Source SQL file:

-- Drop the database if it exists
DROP DATABASE IF EXISTS fitnessdb;

-- Create the database
CREATE DATABASE fitnessdb;
USE fitnessdb;

-- Create Users table
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Gender VARCHAR(10) NOT NULL
);

-- Create Workouts table
CREATE TABLE Workouts (
    WorkoutID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    Date DATE NOT NULL,
    DurationMinutes INT NOT NULL,
    CaloriesBurned INT NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Sample data into Users table
INSERT INTO Users (FirstName, LastName, Age, Gender) VALUES ('Alice', 'Johnson', 29, 'Female');
INSERT INTO Users (FirstName, LastName, Age, Gender) VALUES ('Bob', 'Smith', 35, 'Male');
INSERT INTO Users (FirstName, LastName, Age, Gender) VALUES ('Charlie', 'Brown', 42, 'Male');

-- Sample data into Workouts table
INSERT INTO Workouts (UserID, Date, DurationMinutes, CaloriesBurned) VALUES (1, '2024-11-20', 60, 500);
INSERT INTO Workouts (UserID, Date, DurationMinutes, CaloriesBurned) VALUES (2, '2024-11-21', 45, 350);
INSERT INTO Workouts (UserID, Date, DurationMinutes, CaloriesBurned) VALUES (3, '2024-11-22', 30, 250);