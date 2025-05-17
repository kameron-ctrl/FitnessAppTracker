-- Drop the database if it exists
DROP DATABASE IF EXISTS fitnessdb;

-- Creating the database
CREATE DATABASE fitnessdb;
USE fitnessdb;


CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100)
);


CREATE TABLE WorkoutTypes (
    WorkoutTypeID INT AUTO_INCREMENT PRIMARY KEY,
    WorkoutTypeName VARCHAR(50),
    Description TEXT,
    IntensityLevel VARCHAR(20),
    DurationRecommendation INT 
);


CREATE TABLE Workouts (
    WorkoutID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    WorkoutTypeID INT,
    Date DATE,
    DurationMinutes INT,
    CaloriesBurned INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (WorkoutTypeID) REFERENCES WorkoutTypes(WorkoutTypeID)
);


CREATE TABLE Exercises (
    ExerciseID INT AUTO_INCREMENT PRIMARY KEY,
    WorkoutID INT,
    ExerciseName VARCHAR(100),
    Reps INT DEFAULT NULL, 
    Sets INT DEFAULT NULL, 
    FOREIGN KEY (WorkoutID) REFERENCES Workouts(WorkoutID)
);


INSERT INTO Users (FirstName, LastName, Email)
VALUES
    ('Alice', 'Johnson', 'alice.johnson@gmail.com'),
    ('Bob', 'Smith', 'bob.smith@gmail.com'),
    ('Charlie', 'Brown', 'charlie.brown@gmail.com'),
    ('Diana', 'White', 'diana.white@gmail.com'),
    ('Eve', 'Black', 'eve.black@gmail.com'),
    ('Kam', 'Benjamin', 'kam.benjamin@gmail.com'),
    ('Josh', 'Omorodion', 'josh.omorodion@gmail.com');


INSERT INTO WorkoutTypes (WorkoutTypeName, Description, IntensityLevel, DurationRecommendation) 
VALUES 
('Cardio', 'Aerobic exercises to improve heart health and endurance.', 'Medium', 30),
('Strength', 'Exercises focused on building muscle strength.', 'High', 45),
('Flexibility', 'Workouts aimed at improving range of motion.', 'Low', 20),
('HIIT', 'High-Intensity Interval Training for quick, intense sessions.', 'High', 15),
('Yoga', 'A mix of stretching, balance, and meditation.', 'Low', 60);


INSERT INTO Workouts (UserID, WorkoutTypeID, Date, DurationMinutes, CaloriesBurned)
VALUES
    (1, 1, '2024-11-20', 60, 500),
    (2, 2, '2024-11-21', 45, 350),
    (3, 4, '2024-11-22', 30, 250),
    (4, 5, '2024-11-23', 90, 200),
    (5, 3, '2024-11-24', 40, 150);



INSERT INTO Exercises (WorkoutID, ExerciseName, Reps, Sets)
VALUES
    (1, 'Running', NULL, NULL),  
    (2, 'Bench Press', 12, 3),
    (3, 'Burpees', 20, 2),
    (4, 'Downward Dog', NULL, NULL),  
    (5, 'Lunges', 15, 4);
