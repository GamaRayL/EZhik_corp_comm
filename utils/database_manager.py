import sqlite3 as sq


class DatabaseManager:
    def __init__(self, db_name: str) -> None:
        self.db = sq.connect(db_name)
        self.cur = self.db.cursor()
        self.__create_tb_users()

    def __create_tb_users(self) -> None:
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS 'users' (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    tg_id TEXT
                )
            """)
            self.db.commit()
        except sq.Error as e:
            print(f'При создании базы данных возникла ошибка: {e}')

    def create_user(self, first_name: str, last_name: str, tg_id: str) -> None:

        user = self.cur.execute("""
            SELECT 1 FROM users
            WHERE tg_id = ?
        """, (tg_id,)).fetchone()

        if not user:
            self.cur.execute("""
                INSERT INTO users (first_name, last_name, tg_id) VALUES (?, ?, ?)
            """, (first_name, last_name, tg_id))
            self.db.commit()

    def update_user(self):
        pass

    def select_user(self, tg_user_id):
        user = self.cur.execute("""
            SELECT * FROM users
            WHERE tg_id = ?
        """, (tg_user_id,)).fetchone()

        return user