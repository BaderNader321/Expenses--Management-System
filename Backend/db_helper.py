import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="expense_manager"
    )
    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_all_records():
    logger.info("fetch_all_records called")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT * FROM expenses 
               ORDER BY expense_date'''
        )
        expenses = cursor.fetchall()
        return expenses

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s",
                      (expense_date,)
        )
        expenses = cursor.fetchall()
        return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s",
                      (expense_date,)
        )

def fetch_categorically_expense_summary(start_date, end_date):
    logger.info(f"fetch_categorically_expense_summary: {start_date} end: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total 
               FROM expenses 
               WHERE expense_date BETWEEN %s and %s
               GROUP BY category
               ORDER BY total DESC''',
        (start_date, end_date)
        )
        data = cursor.fetchall()
        return data

def fetch_monthly_expense_summary():
    logger.info(f"fetch_monthly_expense_summary called")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT 
                    MONTHNAME(expense_date) AS month,  
                    SUM(amount) AS total
                FROM expenses
                GROUP BY month
                ORDER BY month'''
        )
        monthly_data = cursor.fetchall()
        return monthly_data
def main() -> None:
    data_all = fetch_all_records()
    for row_all in data_all:
        print(row_all)

    data_by_date = fetch_expenses_for_date("2024-08-15")
    for row_by_date in data_by_date:
        print(row_by_date)

    # print("***** Inserted a record! *****")
    # insert_expense("2024-08-05", 300, "Entertainment", "Watched Jawan Movie")
    #
    # print("***** Check if the record is inserted or not! *****")
    # print(fetch_expenses_for_date("2024-08-05"))
    #
    # print("***** Deleted the inserted record! *****")
    # delete_expenses_for_date("2024-08-05")
    #
    # print("***** Check if the record is deleted or not! *****")
    # print(fetch_expenses_for_date("2024-08-05"))

    summary = fetch_categorically_expense_summary("2024-08-01", "2024-08-05")
    for record in summary:
        print(record)

    monthly_summary = fetch_monthly_expense_summary()
    for row in monthly_summary:
        print(row)

if __name__ == '__main__':
    main()