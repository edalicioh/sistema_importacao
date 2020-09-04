
from Database import Database


class Create:

    def __init__(self):
        self.db = Database()

    def create_table(self):
        sql = """
            CREATE TABLE dados (
                
            )
        """
        self.db.execute_query(sql)
        print("Create table")
