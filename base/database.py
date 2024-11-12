import asyncpg
import os

DATABASE_URL = os.getenv("DATABASE_URL")


class Database:
    def __init__(self):
        self.connection = None


    async def connect(self):
        self.connection = await asyncpg.connect(DATABASE_URL)
        await self.create_tables()


    async def close(self):
        await self.connection.close()


    async def create_tables(self):
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id BIGINT UNIQUE NOT NULL,
            balance DECIMAL DEFAULT 0
        );
        """

        create_payment_history_table_query = """
        CREATE TABLE IF NOT EXISTS payment_history (
            id SERIAL PRIMARY KEY,
            user_id BIGINT REFERENCES users(user_id),
            date DATE NOT NULL,
            time TIME NOT NULL,
            amount DECIMAL NOT NULL,
            type VARCHAR(50) NOT NULL
        );
        """

        await self.connection.execute(create_users_table_query)
        await self.connection.execute(create_payment_history_table_query)


    async def get_user_balance(self, user_id):
        query = "SELECT balance FROM users WHERE user_id = \$1"
        balance = await self.connection.fetchval(query, user_id)
        return balance


    async def update_user_balance(self, user_id, amount):
        query = "UPDATE users SET balance = balance + \$1 WHERE user_id = \$2"
        await self.connection.execute(query, amount, user_id)


    async def get_payment_history(self, user_id):
        query = """
        SELECT date, time, amount, type FROM payment_history WHERE user_id = \$1 
        ORDER BY date DESC
        """
        pay_his = await self.connection.fetch(query, user_id)
        return pay_his


