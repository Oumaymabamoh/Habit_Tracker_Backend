import sqlite3
from datetime import datetime


def connect(name="habits.db"):
    """
    Connects to the SQLite database.
    :param name: Name of the database file (default: "habits.db")
    :return: Database connection object
    """
    db = sqlite3.connect(name)  # Connect to the database
    create_tables(db)  # Create the necessary tables if they don't exist
    return db


def create_tables(db):
    """
    Creates the necessary tables if they don't exist in the database.
    :param db: Database connection object
    """
    c = db.cursor()

    # Create "habit" table
    c.execute("""CREATE TABLE IF NOT EXISTS habit (
              name TEXT PRIMARY KEY,
              category TEXT,
              periodicity TEXT,
              creation_time TEXT,
              completion_time TEXT,
              streak INT
    )""")

    # Create "habit_checks" table
    c.execute("""CREATE TABLE IF NOT EXISTS habit_checks(
             name TEXT,
             checkoff INT,
             streak INT DEFAULT 0,
             completion_time TEXT,
             FOREIGN KEY  (name) REFERENCES habit(name)

)""")

    db.commit()


def new_habit(db, name, category, periodicity, creation_time, completion_time=None, streak=0):
    """
    Adds a new habit to the database.
    :param db: Database connection object
    :param name: Name of the habit
    :param category: Category of the habit
    :param periodicity: Periodicity of the habit
    :param creation_time: Creation time of the habit
    :param completion_time: Completion time of the habit (default: None)
    :param streak: Habit streak count (default: 0)
    """
    c = db.cursor()
    c.execute("INSERT INTO habit VALUES (?, ?, ?, ?, ?, ?)", (name, category, periodicity, creation_time, completion_time, streak))
    db.commit()


def checkoff_habit(db, habit_name, checkoff, streak, completion_time):
    """
    Adds a checkoff entry for a habit in the database.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :param checkoff: Checkoff value
    :param streak: Habit streak count
    :param completion_time: Completion time of the habit
    """
    c = db.cursor()
    c.execute("INSERT INTO habit_checks VALUES (?, ?, ?, ?)", (habit_name, checkoff, streak, completion_time))
    db.commit()


def habit_exists(db, habit_name):
    """
    Checks if a habit exists in the database.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :return: True if habit exists, False otherwise
    """
    c = db.cursor()
    query = "SELECT * FROM habit WHERE name = ? "
    c.execute(query, (habit_name,))
    data = c.fetchone()
    return bool(data)


def delete_habit(db, habit_name):
    """
    Deletes a habit from the database.
    :param db: Database connection object
    :param habit_name: Name of the habit
    """
    c = db.cursor()
    c.execute("DELETE FROM habit WHERE name = ?", (habit_name,))
    db.commit()
    reset_checks(db, habit_name)


def get_all_categories(db):
    """
    Retrieves all categories from the habit database.
    :param db: Database connection object
    :return: List of categories
    """
    c = db.cursor()
    c.execute("SELECT category FROM habit")
    data = [row[0].capitalize() for row in c]
    return data


def delete_category(db, habit_name, category_name):
    """
    Deletes a category and its associated habits from the database.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :param category_name: Name of the category
    """
    c = db.cursor()
    c.execute("DELETE FROM habit WHERE category = ?", (category_name,))
    db.commit()
    reset_checks(db, habit_name)


def update_streak(db,  habit_name, streak, completion_time):
    """
    Updates the streak count and completion time of a habit.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :param streak: New streak count
    :param completion_time: New completion time
    """
    c = db.cursor()
    c.execute("UPDATE habit_checks SET streak=?, completion_time=? WHERE name=?", (streak, completion_time, habit_name))
    db.commit()


def update_periodicity(db, habit_name, new_periodicity):
    """
    Updates the periodicity of a habit and resets completion time and streak count.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :param new_periodicity: New periodicity value
    """
    c = db.cursor()
    query = "UPDATE habit SET periodicity = ? WHERE name = ?"
    data = (new_periodicity, habit_name)
    c.execute(query, data)
    db.commit()
    reset_checks(db, habit_name)


def reset_checks(db, habit_name):
    """
    Resets the checkoff entries for a habit.
    :param db: Database connection object
    :param habit_name: Name of the habit
    """
    c = db.cursor()
    query = "DELETE FROM habit_checks WHERE name = ?"
    c.execute(query, (habit_name,))
    db.commit()


def fetch_habits_as_choices(db):
    """
    Gets all the habits listed in the habit database.
    param db: To maintain connection with the database
    return: Returns the list of habit names
    """
    c = db.cursor()
    c.execute("SELECT DISTINCT name FROM habit")
    habits = c.fetchall()
    choices = [habit[0] for habit in habits]
    return choices


def fetch_habit_periodicity(db, habit_name):
    """
    Retrieves the periodicity of a habit from the database.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :return: Periodicity of the habit
    """
    c = db.cursor()
    query = "SELECT periodicity FROM habit WHERE name = ?"
    c.execute(query, (habit_name,))
    row = c.fetchone()
    if row is not None:
        return row[0]
    else:
        return None


def get_periodicity(db, periodicity):
    """
    Retrieves all habits of the specified periodicity from the database.
    :param db: Database connection object
    :param periodicity: Periodicity value (e.g., daily, weekly, monthly)
    :return: List of habits with the specified periodicity
    """
    c = db.cursor()
    query = "SELECT * FROM habit WHERE periodicity = ?"
    c.execute(query, (periodicity,))
    records = c.fetchall()
    return records


def get_streak_count(db, habit_name):
    """
    Retrieves the streak count of a habit from the database.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :return: Streak count of the habit
    """
    c = db.cursor()
    query = "SELECT streak FROM habit WHERE name= ?"
    c.execute(query, (habit_name,))
    row = c.fetchall()
    if row is not None:
        return row[0]
    else:
        return 0


def fetch_last_completed(db, habit_name):
    """
    Retrieves the completion time of the last checkoff for a specific habit from the database.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :return: The completion time of the last checkoff, or None if no checkoffs found
    """
    c = db.cursor()
    query = "SELECT completion_time FROM habit WHERE name = ?"
    c.execute(query, (habit_name,))
    result = c.fetchone()
    if result is not None:
        return result[0]
    else:
        return None


def fetch_last_completed_week(db, habit_name):
    """
    Retrieves the week number of the last completed checkoff for a habit.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :return: Week number of the last completed checkoff
    """
    c = db.cursor()
    query = "SELECT MAX(completion_time) FROM habit_checks WHERE name = ? AND completion_time = 1"
    c.execute(query, (habit_name,))
    data = c.fetchall()
    if data[0][0]:
        last_completed_week = datetime.strptime(data[0][0], "%m/%d/%Y %H:%M").strftime("%W")
        return last_completed_week
    else:
        return None


def fetch_last_completed_month(db, habit_name):
    """
    Retrieves the month of the last completed checkoff for a habit.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :return: Month of the last completed checkoff
    """
    c = db.cursor()
    query = "SELECT MAX(completion_time) FROM habit WHERE name = ?"
    c.execute(query, (habit_name,))
    last_completed_month = c.fetchone()[0]
    if last_completed_month:
        return last_completed_month.strftime("%Y-%m")
    else:
        return None


def get_longest_habit_streak(db, habit_name):
    """
    Retrieves the longest streak for a specific habit from the database.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :return: List containing the longest streak value
        """
    c = db.cursor()
    c.execute("SELECT MAX(streak) FROM habit_checks WHERE name=? ")
    return c.fetchall()


def get_all_habits(db):
    """
    Retrieves all habits from the database.
    :param db: Database connection object
    :return: List of all habits
    """
    c = db.cursor()
    c.execute("SELECT * FROM habit")
    data = c.fetchall()
    return data


def get_habit_checkoffs(db, habit_name):
    """
    Retrieves all checkoffs for a specific habit from the database.
    :param db: Database connection object
    :param habit_name: Name of the habit
    :return: List of all checkoffs for the specified habit
    """
    c = db.cursor()
    c.execute("SELECT * FROM habit WHERE name=?", (habit_name,))
    return c.fetchall()
