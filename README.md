# Habit_Tracker_Backend
# Description 
Habit Tracker backend is a command line interface application designed to help users track their habits and establish a routine for positive behavior. It provides a simple and efficient way to monitor, set goals and track progress in achieving them.
With the Habit Tracker,users can easily create and manage a list of habits they want to cultivate. They can define the periodicity of each habit, whether it's daily, weekly, or monthly. The application allows users to mark habits as completed, providing a sense of accomplishment and motivation.Additionally,the Habit Tracker provides analytics to give users insights into their habit tracking progress.

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
3. Mark Habit as Complete: Allows you to mark a habit as completed .
5. View Analytics: Choose this option to see the analytics and insights related to your habits.
4. Exit: Exits the Habit Tracker app.
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
This is my first Python project, and I welcome your comments, suggestions, and contributions. Whether you have ideas to improve the code, find bugs, or have feature requests, please feel free to contribute by following these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature, bug fix, or enhancement.
4. Make the necessary changes and additions in your branch.
5. Test your changes thoroughly.
6. Commit your changes and push them to your forked repository.
7. Submit a pull request to the main repository.

When submitting a pull request, please provide a clear and descriptive explanation of the changes you made.
Additionally, if you encounter any bugs or have feature requests, create an issue on the repository and provide as much detail as possible.

Your contributions will be greatly appreciated as they help improve the Habit Tracker project and make it better for everyone. Thank you!

Happy habit tracking!
