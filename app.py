import sqlite3
import bcrypt

# Hash a password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Check hashed password
def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def signup(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:        
        hashed_password = hash_password(password)
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        return "User registered successfully!"
    except sqlite3.IntegrityError:
        return "Username already exists!"
    finally:
        conn.close()

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()

    conn.close()

    if result:
        stored_password = result[0]

        if check_password(stored_password, password):
            return "Login successful!"
        else:
            return "Incorrect password!"
    else:
        return "Username not found!"

if __name__ == "__main__":
    # Example of user registration
    print(signup('john_doe', 'securepassword123'))

    # Example of user login
    print(login('john_doe', 'securepassword123'))
    print(login('john_doe', 'wrongpassword'))
    print(login('unknown_user', 'password'))