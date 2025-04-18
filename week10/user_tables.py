import psycopg2
from config import load_config

def create_tables():
    """Создание таблиц для игры Snake в PostgreSQL"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            level INTEGER DEFAULT 1
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                print("Tables created or already exist.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while creating tables:", error)

if __name__ == '__main__':
    create_tables()