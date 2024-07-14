import psycopg2

import config
from connection.db.utils import convert_records

cfg = config.get_config()


class DbExecutor:

    def __init__(self) -> None:
        self.host = cfg.db_host
        self.port = cfg.db_port
        self.username = cfg.db_username
        self.password = cfg.db_password
        self.schema = cfg.db_name
        self._pool = None

    @property
    def pool(self):
        if not self._pool or self._pool.closed != 0:
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
