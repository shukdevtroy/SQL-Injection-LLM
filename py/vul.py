import sqlite3

def get_user_data(user_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    
    # Potential SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id};"
    cursor.execute(query)
    
    results = cursor.fetchall()
    connection.close()
    
    return results

# Example usage
user_input = "1 OR 1=1"  # This simulates a malicious input
print(get_user_data(user_input))
