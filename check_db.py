import sqlite3

# Connect to the database
conn = sqlite3.connect("./users.db")
cursor = conn.cursor()

# Check if the users table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
table = cursor.fetchone()

if table:
    print("✅ 'users' table exists!")
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    if users:
        print("👤 Users in database:")
        for user in users:
            print(user)
    else:
        print("⚠️ No users found in the database.")
else:
    print("❌ 'users' table does not exist. Database might be empty.")

# Close connection
conn.close()
