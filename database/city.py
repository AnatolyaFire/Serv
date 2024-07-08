import sqlalchemy
from sqlalchemy import select
from database import Database


class CityDatabase(Database):
    def __init__(self):
        super().__init__()
        self.table = sqlalchemy.Table("city", self.metadata)

    def select(self):
        a = [i[1] for i in self.connection.execute(select(self.table)).fetchall()]
        return a
