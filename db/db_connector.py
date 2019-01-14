import json
import pymysql

from value_models.status import Status
from value_models.user import User


def _our_hash(password):
    return {
        "pass": "bf6116af8e4b3e83a7646640590b9d5f5c95b06bf7eebf6c424487ff39293833",
        "test": "62fc22c0da68a727562013a405e45ad29fe67725db24870d8dff48a39b37f5ae",
        "secret": "94d1297b55907d7158b27cd91f0d0b0d212abc0ccd4a3e861b1f4e1f404c67e0"
    }[password]


class DBConnector:
    def __init__(self, db_config):
        # Connect to the database
        self.connection = pymysql.connect(
             **db_config,
             charset='utf8mb4',
             cursorclass=pymysql.cursors.DictCursor)

    def create_user(self, user):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = '''INSERT INTO `ow_base_user` (`username`, `email`, `password`, `joinIp`)
                  'VALUES ("{}", "{}", "{}", "{}");'''
            cursor.execute(sql.format(user.username, user.email, _our_hash(user.password), "3246457523435"))
            # cursor.execute(sql, ('webmaster@python.org', 'very-suecret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.connection.commit()

    def get_users(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `username`, `password` FROM `ow_base_user`;"
            cursor.execute(sql)
            result = cursor.fetchall()
            # result = cursor.fetchone()
            # print(result)
        self.connection.commit()
        return [User(**u) for u in result]

    def delete_user(self, user):
        with self.connection.cursor() as cursor:
            sql = """DELETE FROM `ow_base_user` 
                    WHERE `ow_base_user`.`username` = %s"""
            cursor.execute(sql, (user.username,))  # tuple with one element
        self.connection.commit()

    def get_last_text_status(self):
        """ Get status with maximum id that is last added """
        with self.connection.cursor() as cursor:
            sql = """SELECT * FROM `ow_newsfeed_action` 
                     WHERE `id`= (SELECT MAX(`id`) FROM `ow_newsfeed_action`)
                     AND `entityType`="user-status"
                     """
            cursor.execute(sql)
            response = cursor.fetchone()
            data = json.loads(response["data"])
        self.connection.commit()
        return Status(text=data["status"])

    def count_status(self):
        with self.connection.cursor() as cursor:
            sql = """SELECT COUNT(*) FROM `ow_newsfeed_action` 
                     WHERE `entityType`="user-status"
                  """
            cursor.execute(sql)
        self.connection.commit()
        # print(cursor.fetchone())
        return cursor.fetchone()['COUNT(*)']

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    config = {
        "host": "localhost",
        "user": "oxwa128",
        "password": "wSSp@g!657",
        "db": "oxwa128"
        }
    db = DBConnector(config)
    print(db.get_last_text_status())
