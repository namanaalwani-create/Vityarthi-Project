# Vityarthi-Project
Personal Expense Manager 
This program includes adding expenses , storing them as records and dipslaying them in a list and performming a few arithematic opperations.
# Personal Expense Tracker

## 1. Project Title

**Personal Expense Tracker**

## 2. Overview of the Project

Personal Expense Tracker is a Python-based console application used to manage daily expenses.

The program allows the us to add, view, search, update, and delete expenses. It also calculates the total amount of all recorded expenses.

This project is designed as a beginner-level Python project and demonstrates the use of functions, lists, dictionaries, loops, conditional statements, user input, and basic Python operations.

## 3. Features

The project has the following features:

* **Add Expense** – Add a new expense by entering the date, category, and amount.
* **View Expenses** – Display all the expenses stored in the program.
* **Search Expense** – Search for expenses using their category.
* **Update Expense** – Modify the date, category, or amount of an existing expense.
* **Delete Expense** – Remove an expense from the list.
* **Total Expense** – Calculate and display the total amount of all expenses.
* **Exit** – Exit the program safely.

## 4. Technologies/Tools Used

* **Programming Language:** Python
* **Editor/IDE:** Visual Studio Code
* **Data Structure:** List and Dictionary
* **Python Concepts Used:**

  * Variables
  * Functions
  * Lists
  * Dictionaries
  * `if-elif-else` statements
  * `for` and `while` loops
  * User input
  * Type conversion
  * String methods
  * Basic arithmetic operations

## 5. Steps to Install & Run the Project

### Step 1: Install Python

Download and install Python from the official Python website if it is not already installed.

### Step 2: Install Visual Studio Code

Open the project in Visual Studio Code.

### Step 3: Create the Python File

Save the program as:

`expense_tracker.py`

### Step 4: Open the Terminal

Open the terminal in Visual Studio Code.

### Step 5: Run the Program

Use the following command:

```bash
python expense_tracker.py
```

The program will display the main menu:

```text
Personal Expense Tracker
1. Add Expense
2. view
3. Search Expense
4. Update
5. Delete Expense
6. Total Expense
7. Exit
```

Enter the number corresponding to the operation you want to perform.

## 6. Instructions for Testing

The following tests can be performed to check whether the program works correctly.

### Test 1: Add Expense

1. Select option `1`.
2. Enter a date.
3. Enter an expense category.
4. Enter the expense amount.
5. Check that the message **"Expense added"** is displayed.

Example:

```text
Enter date: 29-09-2026
Enter category: Food
Enter amount: 250
Expense added
```

### Test 2: View Expenses

1. Select option `2`.
2. Check whether the added expense is displayed correctly.

### Test 3: Search Expense

1. Select option `3`.
2. Enter an existing category such as `Food`.
3. Check whether the matching expense is displayed.

Also test a category that does not exist and check that:

```text
Expense not found
```

is displayed.

### Test 4: Update Expense

1. Select option `4`.
2. Enter the expense number.
3. Enter the new date, category, and amount.
4. Select option `2` to confirm that the expense was updated.

### Test 5: Delete Expense

1. Select option `5`.
2. Enter the expense number.
3. Check that **"Expense deleted"** is displayed.
4. Select option `2` to confirm that the expense has been removed.

### Test 6: Total Expense

1. Add two or more expenses.
2. Select option `6`.
3. Check that the program displays the correct total amount.

Example:

```text
Total expense = 500.0
```

### Test 7: Exit

Select option `7`.

The program should display:

```text
Thank you
```

and terminate.
## 8. Conclusion

The Personal Expense Tracker is a Python project that helps users manage their expenses through a menu-driven console application. It demonstrates us about Python programming concepts and provides practical implementation of functions, lists, dictionaries, loops, and conditional statements.
