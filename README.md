# Habit_Tracker_Backend
# Description 
Habit Tracker backend is a command line interface application designed to help users track their habits and establish a routine for positive behavior. It provides a simple and efficient way to monitor, set goals and track progress in achieving them.
With the Habit Tracker, users can easily create and manage a list of habits they want to cultivate.They can define the periodicity of each habit, whether it's daily, weekly or monthly.The application allows users to mark habits as completed, providing a sense of accomplishment and motivation.Additionally, the Habit Tracker provides analytics to give users insights into their habit tracking progress.

This programm is a part of the IU university OOFPP course. 

# Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Contribution](#contribution)

# Prerequisites
Before using the Habit Tracker, ensure that you have the following software installed on your operating system: 

- Python 3.11 or higher installed on your operating system. If you don't have Python installed, you can download and install the latest version from the official Python website [here](https://www.python.org/downloads/).
- SQLite: The Habit Tracker uses SQLite as the database backend. SQLite comes bundled with Python, so there is no need for separate installation or setup.

# Getting Started 
To start using the Habit Tracker CLI, follow these steps:
1. Open a command prompt or terminal window and navigate to the folder where you saved the Habit Tracker files.
2. Run the following command to launch the program:
```
python main.py
```
3. Once the program starts, you will be presented with a menu of options. Use the provided menu options to create habit,manage habits,mark habits as completed and see analytics.
4. Follow the on-screen instructions to interact with the Habit Tracker CLI and manage your habits effectively.

Please note that if you encounter the "Warning: Input is not a terminal (fd=0)" message, you can try running the program with the -i flag as shown in the previous response:

```bash
python -i main.py
```
This will launch the program in interactive mode and help avoid the warning message.

# Usage
The Habit Tracker CLI provides the following options:
1. Add Habit: Allows you to add a new habit to track. You can specify the name, category and periodicity (daily, weekly or monthly) .
2. Manage Habit:
   - Delete Habit: Choose this option to delete a habit from your habit list.You will be prompted to select the habit you want to delete.
   - Delete Category: Choose this option to delete a category from your category list. You will be prompted to select the category you want to delete.
   - Update Habit: Select this option to update the periodicity of a habit. You can change the habit's periodicity to daily, weekly, or monthly.
3. Check Off habit: Allows you to mark a habit as completed .
5. View Analytics: Choose this option to see the analytics and insights related to your habits.
   - All your current habits with their details.
   - All habits with a same time-period
   - The longest streak you have out of all your current habits. 
   - The longest streak you've had for a specific habit
7. Exit: Exits the Habit Tracker app.

Follow the prompts and instructions provided by the CLI to navigate through the options and manage your habits efficiently.

# Running Tests
To run the tests for this project, you will need the following packages installed:

- unittest: For running unit tests.

 ```bash
  pip install -U unittest
 ```
- freezegun: For freezing time.

```bash
  pip install freezegun
```
Once you have the required packages installed, follow these steps to run the tests:

1. Clone the repository to your local machine.
2. Navigate to the project's root directory.
3. Open a terminal or command prompt.
4. Run the following command to execute the test suite:

```bash
python -m unittest discover
```
This command will automatically discover and run all the test cases in the project.

After executing the tests, the test results will be displayed in the terminal or command prompt. Any failures or errors will be reported.

Note: Make sure you have Python installed on your machine.

# Contribution
This is my first Python project, and I welcome your contributions to help improve the Habit Tracker. Your comments, suggestions, bug reports, and feature requests are valuable in enhancing the project. Feel free to open an issue on the repository to report bugs or request new features. Thank you!


**Happy habit tracking!**
