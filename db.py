import sqlite3

def create_database():
    # Connect to the SQLite database (it will be created if it doesn't exist)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Create the users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')

    # Insert sample data
    cursor.execute("INSERT INTO users (username, email) VALUES ('alice', 'alice@example.com')")
    cursor.execute("INSERT INTO users (username, email) VALUES ('bob', 'bob@example.com')")
    cursor.execute("INSERT INTO users (username, email) VALUES ('charlie', 'charlie@example.com')")

    # Commit the changes and close the connection
    connection.commit()
    connection.close()
    print("Database created and sample data inserted.")

if __name__ == "__main__":
    create_database()
