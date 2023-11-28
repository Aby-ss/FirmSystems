from rich import text
from rich import print
from rich import box
from rich.panel import Panel
from rich.prompt import Prompt

from rich.traceback import install
install(show_locals=True)

import sqlite3

employee_conn = sqlite3.connect("EmployeeDatabase.db")
cursor = employee_conn.cursor()

cursor.EXECUTE('''
               CREATE TABLE IF NOT EXISTS EmployeeDatabase
               EmployeeID INTEGER PRIMARY KEY,
               Name TEXT,
               Age INTEGER,
               Role TEXT,
               Salary INTEGER
               ''')

password = "4556786"
user_identification = Prompt.ask("Enter Password ")


def add_employee():
    new_employee_name = Prompt.ask("Enter new employee's name ")
    new_employee_ID = Prompt/ask("Enter new employee's ID ")
    new_employee_age = Prompt.ask("Enter new employee's age ")
    new_Employee_role = Prompt.ask("Enter new employee's role ")
    new_employee_salary = Prompt.ask("Enter new employee's salary")

    cursor.EXECUTE(f"INSERT INTO EmployeeDatabase (EmployeeID, Name, Age, Role, Salary) VALUES (?, ?, ?, ?, ?)", (new_employee_ID, new_employee_name, new_employee_age, new_employee_role, new_employee_salary))

    employee_conn.commit()
    employee_conn.close()


if user_identification == password:
    print(Panel("User Authorised!", box=box.SQUARE, border_style="bold green"))

    print(Panel.fit("Choose an Option:\n1- Add new employee\n2- Discard employee\n3- Print employee database", box = box.SQUARE, border_style="bold white"))
else:
    print(Panel("Incorrect Password", box=box.SQUARE, border_style="bold red"))






