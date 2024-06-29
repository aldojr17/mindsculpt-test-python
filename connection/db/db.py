from connection.db import mindsculpt_db
from connection.db.utils import fetch_one_record


class DBUtils:
    @classmethod
    def get_image_generation_by_id(cls, image_id):
        db = mindsculpt_db
        sql = "SELECT * FROM image_generation WHERE id = %s"
        return fetch_one_record(db, sql, (image_id,))
