"""Завдання 4: Ітерація по рядку з циклом for
Програма, яка:

Встановлює рядок, наприклад, fruit = "apple".
Використовує цикл for, щоб перебрати всі символи цього рядка 
та вивести кожен символ на новому рядку."""

user_input = input("Enter the word:")
for ch in user_input:
    print(ch)