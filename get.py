from database import connect, get_all_categories, fetch_habits_as_choices
import questionary as qt


def habit_name():
    """
    Prompts the user to enter the name of the habit.
    Habit name is restricted to alphabets only. No whitespaces or special
    characters are allowed.
    :return:  Returns the name of the habit that the user has entered.
    """
    return qt.text("Please Enter the Name of Your Habit:",
                   validate=lambda name: True if name.isalpha() and len(name) > 1
                   else "Please enter a valid name").ask().lower()


def habits_from_db(db):
    """
    Returns the selected habit from the available habits in the database.
    """
    list_of_habits = fetch_habits_as_choices(db)
    if list_of_habits:
        return qt.select("Please select a habit", choices=list_of_habits).ask().lower()
    else:
        raise ValueError("No habit in the database; Add a habit first to use this function")


def periodicity(db):
    """
    Prompts the user to select the desired frequency for a habit.
    :return: The selected periodicity as a lowercase string.
    """
    return qt.select("How many times do you want to do this task",
                     choices=["Daily",
                              "weekly",
                              "Monthly"
                              ]).ask().lower()


def defined_categories():
    """
    Displays the categories available in the database for the user to choose from.
    :return: Returns the selected category from the list of choices
    :raises ValueError: If no categories are available in the database then raises a ValueError
    """

    db = connect()
    categories = get_all_categories(db)

    if not categories:
        raise ValueError(
                "No categories found in database; please define a category using the 'Add habit' function.")

    category_choice = qt.select("Please select a category:", choices=sorted(categories)).ask().lower()
    return category_choice


def show_period_choices():
    """
    Prompts the user to select from the list of provided period display choices.
    :return: Return the chosen action as str
    """
    choice = qt.select("Would you like to view all habits or sort habit by periodicity?",
                       choices=[
                           "View Daily Habits",
                           "View Weekly Habits",
                           "View Monthly Habits",
                           "Back to Main Menu"
                       ]).ask()
    return choice

