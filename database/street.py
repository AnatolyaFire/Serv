import json

import sqlalchemy
from sqlalchemy import select
import pandas
from database import Database


class StreetDatabase(Database):
    def __init__(self):
        super().__init__()
        self.table = sqlalchemy.Table("street", self.metadata)

    def select(self, city_id: int):             #вывод улиц по выбранному городу
        return [i[-1] for i in self.connection.execute(select(self.table).where(
            self.table.c.idcity == city_id)).fetchall()]
