
import sqlite3
import os

# Get the database path from an environment variable (for deployment flexibility)
DATABASE_PATH = os.getenv("DATABASE_PATH", "users.db")

# Initialize database
def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            balance INTEGER DEFAULT 0,
            invites INTEGER DEFAULT 0,
            is_banned INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Add user
def add_user(user_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO users (user_id) VALUES (?)
    ''', (user_id,))
    conn.commit()
    conn.close()

# Get user information
def get_user(user_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE user_id = ?
    ''', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

# Update user information
def update_user(user_id, balance=None, invites=None, is_banned=None):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    if balance is not None:
        cursor.execute("UPDATE users SET balance = ? WHERE user_id = ?", (balance, user_id))
    if invites is not None:
        cursor.execute("UPDATE users SET invites = ? WHERE user_id = ?", (invites, user_id))
    if is_banned is not None:
        cursor.execute("UPDATE users SET is_banned = ? WHERE user_id = ?", (is_banned, user_id))
    conn.commit()
    conn.close()
