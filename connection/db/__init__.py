import psycopg2

from config.config import Config
from connection.db.utils import convert_records

config = Config()


class DbExecutor(object):

    def __init__(self) -> None:
        self.host = config.db_host
        self.port = config.db_port
        self.username = config.db_username
        self.password = config.db_password
        self.schema = config.db_name
        self._pool = None

    @property
    def pool(self):
        if not self._pool:
            self._pool = psycopg2.connect(
                database=self.schema,
                host=self.host,
                user=self.username,
                password=self.password,
                port=self.port,
            )

        return self._pool

    def execute(self, sql, args=None, fetch_one=False, commit=False):
        conn = self.pool
        res = None

        try:
            cursor = conn.cursor()
            try:
                cursor.execute(sql, args)
                if commit:
                    conn.commit()
                else:
                    raw_res = cursor.fetchone() if fetch_one else cursor.fetchall()
                    res = convert_records(cursor.description, raw_res)
            finally:
                cursor.close()
        finally:
            conn.close()

        return res

    def close_pool(self):
        self.pool.close()


mindsculpt_db = DbExecutor()
