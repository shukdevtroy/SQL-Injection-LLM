import sqlite3

def get_user_data(user_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    
    # Secure against SQL Injection using parameterized queries
    query = "SELECT * FROM users WHERE id = ?;"
    cursor.execute(query, (user_id,))
    
    results = cursor.fetchall()
    connection.close()
    
    return results

# Example usage
user_input = 1  # Simulated safe input
print(get_user_data(user_input))
