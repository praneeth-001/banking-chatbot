import mysql.connector
global cnx


cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="banking_data1"
)

# Function to fetch the order status from the order_tracking table
def get_classification(acc_number: int):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = (
        f"SELECT TRANSACTION_DETAILS, SUM(WITHDRAWL_AMT ) AS total_spent" 
        "FROM final" 
        "WHERE AccountNo = 1001"
        "GROUP BY transaction_details"

    )
    cursor.execute(query, (acc_number,),dictionary=True)

    # Fetching the result
    result = cursor.fetchall()

    # Closing the cursor
    cursor.close()

    if result:
        return result[0]
    # Returning the order status
    else:
        return None






