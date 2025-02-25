import sqlite3

class Database:
    def __init__(self, db_name="trading.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS trades (
                id INTEGER PRIMARY KEY,
                symbol TEXT,
                trade_type TEXT,
                price REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def log_trade(self, symbol, trade_type, price):
        self.cursor.execute("INSERT INTO trades (symbol, trade_type, price) VALUES (?, ?, ?)", (symbol, trade_type, price))
        self.conn.commit()
