# database.py
import sqlite3
import os
import regex as re
from logger import setup_logger

# Get the configured logger
logger = setup_logger()

DB_PATH = "ChatBridge.db"  # adjust the path as needed
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def validate_email(email: str) -> bool:
    """Validate email format using regex"""
    return bool(EMAIL_REGEX.match(email))


def get_connection():
    logger.info(f"Connecting to the {DB_PATH}...")
    return sqlite3.connect(DB_PATH)


def init_db():
    logger.info(f"Initializing {DB_PATH}...")
    conn = get_connection()
    c = conn.cursor()
    # Create users table
    c.execute(
        """CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY,
                  email TEXT UNIQUE NOT NULL,
                  password TEXT)"""
    )

    # Create chatbots table
    c.execute(
        """CREATE TABLE IF NOT EXISTS chatbots (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     bot_id TEXT UNIQUE DEFAULT (LOWER(HEX(RANDOMBLOB(16)))),
                     bot_name TEXT UNIQUE,
                     username TEXT,
                     company_name TEXT,
                     domain TEXT,
                     industry TEXT,
                     system_prompt TEXT,
                     documents TEXT,
                     created_at DATETIME,
                     FOREIGN KEY(username) REFERENCES users(username)
                 )"""
    )

    # Create chat_history table
    c.execute(
        """CREATE TABLE IF NOT EXISTS chat_history (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     bot_id INTEGER,
                     bot_name TEXT,
                     role TEXT,
                     content TEXT,
                     timestamp DATETIME,
                     FOREIGN KEY(bot_id) REFERENCES chatbots(id)
                 )"""
    )

    # Add index for faster email lookups
    c.execute("CREATE INDEX IF NOT EXISTS idx_email ON users(email)")

    conn.commit()
    conn.close()


def init_file_storage():
    if not os.path.exists("user_docs"):
        os.makedirs("user_docs")
