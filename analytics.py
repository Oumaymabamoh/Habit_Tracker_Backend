from database import *


# return a list of all tracked habits
def habits_list(db):
    """
    Gets the list of all tracked habits from the database and displays them in a formatted table.
    :param db: Database connection object
    :return: None
    """
    habits = get_all_habits(db)
    if not habits:
        print("No habits found.")
        return None
    else:
        habits = get_all_habits(db)
    if len(habits) > 0:
        # Uses string formatting to set columns and rows for the table
        print("\n{:<10} {:<15} {:<10} {:<15}".format("Name", "Category", "Periodicity", "Date/Time"))
        print("-------------------------------------------------------")
        for row in habits:
            print("{:<10} {:<15} {:<10} {:<15}".format(
                row[0].capitalize(),  # Name
                row[1].capitalize(),  # Periodicity
                row[2].capitalize(),  # Streak
                row[3].capitalize()))  # Completion TIme
        print("-------------------------------------------------------\n")

    else:
        print("\nNo habit found in the specified periodicity!\n")


# return habits with the same periodicity
def habits_by_period(db, periodicity):
    """
    Gets the list of all habits of the specified periodicity.
    :param db: To maintain connection with the database
    :param periodicity: To get list of specified periodicity habits
    :return: list of all specified periodicity habits
    """
    habits = get_periodicity(db, periodicity)
    # Uses string formatting to set columns and rows for the table
    print(f"\nHabits with tracking period {periodicity}:")
    print("\n{:<10} {:<15} {:<10} {:<15}".format("Name", "Periodicity", "Streak", "Completion Time"))
    print("-------------------------------------------------------")
    for habit in habits:
        print("{:<10} {:<15} {:<10} {:<15}".format(
          habit[0].capitalize(),  # Name
          habit[1].capitalize(),  # Periodicity
          habit[2],  # Streak
          habit[3]))  # Completion Time
    print("-------------------------------------------------------\n")


# return the longest run streak for all habits
def longest_streak_all_habits(db):
    """
    Calculates the longest streak among all habits.
    :param db: To maintain connection with the database
    :return: The longest streak value
    """
    habits = get_all_habits(db)
    longest_streak = 0

    for habit in habits:
        streak = habit_longest_streak(db, habit[0])
        if streak > longest_streak:
            longest_streak = streak

    return longest_streak


# return the longest run streak for a given habit
def habit_longest_streak(db, habit_name):
    """
    Retrieves the longest streak for a given habit.
    :param db: To maintain connection with the database
    :param habit_name: The name of the habit
    :return: The longest streak value
    """
    try:
        c = db.cursor()
        query = "SELECT MAX(streak) FROM habit_checks WHERE name = ?"
        c.execute(query, (habit_name,))
        data = c.fetchone()
        return data[0] if data[0] is not None else 0
    except Exception as e:
        print(f"An error occurred while fetching longest streak for habit {habit_name}: {str(e)}")
        return 0
