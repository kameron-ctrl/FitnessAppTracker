import mysql.connector
from datetime import datetime
import re

# Database connection
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="fitnessdb"
    )
except mysql.connector.Error as err:
    print("Error connecting to the database:", err)
    exit(1)


def execute_query(query, args=None, fetch=False):
    try:
        mycursor = mydb.cursor()
        mycursor.execute(query, args)
        if fetch:
            return mycursor.fetchall() or []
        else:
            mydb.commit()
            return True
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return False
    finally:
        if 'mycursor' in locals():
            mycursor.close()


def add_new_user():
    fn = input("First Name: ").strip()
    ln = input("Last Name: ").strip()
    email = input("Email: ").strip()

    if not fn or not ln or not email:
        print("All fields are required.")
        return


    sql = "INSERT INTO Users (FirstName, LastName, Email) VALUES (%s, %s, %s)"
    if execute_query(sql, (fn, ln, email)):
        print("User added successfully.")


def find_workouts_by_user_and_type():
    uid = input("User ID: ").strip()
    wtype = input("Workout Type (e.g., Cardio, Strength): ").strip()

    if not uid.isdigit():
        print("User ID must be a number.")
        return

    sql = """SELECT w.WorkoutID, w.Date, wt.WorkoutTypeName, w.DurationMinutes, w.CaloriesBurned
             FROM Workouts w
             INNER JOIN WorkoutTypes wt ON w.WorkoutTypeID = wt.WorkoutTypeID
             WHERE w.UserID = %s AND wt.WorkoutTypeName = %s"""
    results = execute_query(sql, (int(uid), wtype), fetch=True)

    if not results:
        print("No workouts found for User ID {} with workout type '{}'.".format(uid, wtype))
        return

    print("\nWorkouts for User ID {} with workout type '{}':".format(uid, wtype))
    for x in results:
        print("Workout ID: {} | Date: {} | Type: {} | Duration: {} mins | Calories: {}".format(
            x[0], x[1], x[2], x[3], x[4]))

  
def find_exercises_by_workout_id():
    wid = input("Workout ID: ").strip()

    if not wid.isdigit():
        print("Workout ID must be a number.")
        return

    sql = """SELECT ExerciseID, ExerciseName, Reps, Sets 
             FROM Exercises WHERE WorkoutID = %s"""
    results = execute_query(sql, (int(wid),), fetch=True)

    if not results:
        print("No exercises found for Workout ID {}.".format(wid))
        return

    print("\nExercises for Workout ID {}:".format(wid))
    for x in results:
        print("Exercise ID: {} | Name: {} | Reps: {} | Sets: {}".format(x[0], x[1], x[2], x[3]))


def add_new_workout():
    uid = input("User ID: ").strip()
    date = input("Workout Date (YYYY-MM-DD): ").strip()
    duration = input("Duration in Minutes: ").strip()
    calories = input("Calories Burned: ").strip()

    if not (uid.isdigit() and duration.isdigit() and calories.isdigit()):
        print("User ID, Duration, and Calories must be numbers.")
        return

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    sql = """INSERT INTO Workouts (UserID, Date, DurationMinutes, CaloriesBurned) 
             VALUES (%s, %s, %s, %s)"""
    if execute_query(sql, (int(uid), date, int(duration), int(calories))):
        print("Workout added successfully.")


def update_user_info():
    sql = "SELECT UserID, FirstName, LastName, Email FROM Users"
    results = execute_query(sql, fetch=True)

    if not results:
        print("No users found.")
        return

    print("\nUsers:")
    for x in results:
        print("User ID: {} | First Name: {} | Last Name: {} | Email: {}".format(x[0], x[1], x[2], x[3]))

    user_id = input("User ID to update: ").strip()

    if not user_id.isdigit():
        print("User ID must be a number.")
        return

    print("1. First Name\n2. Last Name\n3. Email")
    choice = input("Choice: ").strip()
    field = {"1": "FirstName", "2": "LastName", "3": "Email"}.get(choice)

    if not field:
        print("Invalid choice.")
        return

    new_val = input("Enter new value: ").strip()

    if not new_val:
        print("Value cannot be empty.")
        return

    sql = "UPDATE Users SET {} = %s WHERE UserID = %s".format(field)
    if execute_query(sql, (new_val, int(user_id))):
        print("User {} updated successfully.".format(field))


def delete_workout_entry():
    sql = "SELECT WorkoutID, Date, DurationMinutes, CaloriesBurned FROM Workouts"
    results = execute_query(sql, fetch=True)

    if not results:
        print("No workouts found.")
        return

    print("\nWorkouts:")
    for x in results:
        print("Workout ID: {} | Date: {} | Duration: {} mins | Calories Burned: {}".format(x[0], x[1], x[2], x[3]))

    wid = input("Workout ID to delete: ").strip()

    if not wid.isdigit():
        print("Workout ID must be a number.")
        return

    sql = "DELETE FROM Workouts WHERE WorkoutID = %s"
    if execute_query(sql, (int(wid),)):
        print("Workout deleted successfully.")

def find_user_workout_summary():
    uid = input("User ID: ").strip()

    if not uid.isdigit():
        print("User ID must be a number.")
        return

    sql = """SELECT u.FirstName, u.LastName, w.Date, wt.WorkoutTypeName, w.DurationMinutes, w.CaloriesBurned 
             FROM Users u
             INNER JOIN Workouts w ON u.UserID = w.UserID
             INNER JOIN WorkoutTypes wt ON w.WorkoutTypeID = wt.WorkoutTypeID
             WHERE u.UserID = %s"""
    results = execute_query(sql, (int(uid),), fetch=True)

    if not results:
        print("No workout summary found for User ID {}.".format(uid))
        return

    print("\nWorkout Summary for User ID {}:".format(uid))
    for x in results:
        print("Name: {} {} | Date: {} | Type: {} | Duration: {} mins | Calories: {}".format(
            x[0], x[1], x[2], x[3], x[4], x[5]))
            
# Find average calories burned by workout type
def find_average_calories_by_workout_type():
    sql = """SELECT wt.WorkoutTypeName, AVG(w.CaloriesBurned) AS AverageCalories
             FROM Workouts w
             INNER JOIN WorkoutTypes wt ON w.WorkoutTypeID = wt.WorkoutTypeID
             GROUP BY wt.WorkoutTypeName"""
    results = execute_query(sql, fetch=True)

    if not results:
        print("No data found.")
        return

    print("\nAverage Calories Burned by Workout Type:")
    for x in results:
        print("Workout Type: {} | Average Calories: {:.2f}".format(x[0], x[1]))





while True:
    print("\n1. Add New User\n2. Find Workouts by User Id and Workout Type\n3. Find Exercises by Workout ID\n"
      "4. Add New Workout\n5. Update User Information\n6. Delete Workout Entry\n"
      "7. Find User Workout Summary\n8. Show average calorie burned by workout type \n9. Exit")
    choice = input("Choice: ").strip()

    if not choice.isdigit():
        print("Enter a valid number.")
        continue

    option = int(choice)

    if option == 9:
        print("Exiting...")
        break
    elif option == 1:
        add_new_user()
    elif option == 2:
        find_workouts_by_user_and_type()
    elif option == 3:
        find_exercises_by_workout_id()
    elif option == 4:
        add_new_workout()
    elif option == 5:
        update_user_info()
    elif option == 6:
        delete_workout_entry()
    elif option ==7:
        find_user_workout_summary()
    elif option == 8:
        find_average_calories_by_workout_type()
    else:
        print("Invalid choice.")
