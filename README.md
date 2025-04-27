# Python SQLite Login and Signup System

This repository contains a simple login and signup system using Python and SQLite.

## Description

This is a basic implementation of user registration and login using Python and SQLite as the database. The passwords are hashed using bcrypt to ensure security.

## Features
- User registration with unique username
- Password hashing using bcrypt
- Login with password verification

## Requirements
- Python 3.x
- sqlite3
- bcrypt (install via pip)

## Setup
1. Clone the repository:

```bash
git clone https://github.com/CyberNet-Inc/python-sqlite-login-signup.git
```
2. Navigate into the project directory:

```bash
cd python-sqlite-login-signup
```
3. Install bcrypt if not already installed:

```bash
pip install bcrypt
```
4. Run the application:

```bash
python app.py
```

## Usage

The script provides functions for signing up new users and logging in existing users. It includes example calls to both functions at the bottom of `app.py`.

Feel free to expand and integrate this basic example into a larger project or to add more features like email verification, password reset, etc.
