import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="banking_data1"
)

# Function to fetch the order status from the order_tracking table
def get_account_balance(acc_number: int):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = (f"SELECT balance FROM accounts1 WHERE account_number = %s")
    cursor.execute(query,(acc_number,))

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None
def get_card_status(acc_number: int):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = (f"UPDATE accounts1 SET card_status = 'inactive' WHERE account_number = %s")
    cursor.execute(query, (acc_number,))

    # Fetching the result
    result = cnx.commit()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None

''' def get_classification(acc_number: int):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = (f"SELECT account_type FROM accounts1 WHERE account_number = %s")
    cursor.execute(query, (acc_number,))

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None
'''


