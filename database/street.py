import sqlalchemy
from sqlalchemy import select
import pandas
from database import Database
from sqlalchemy import text

class StreetDatabase(Database):
    def __init__(self):
        super().__init__()
        self.table = sqlalchemy.Table("street", self.metadata)
        self.connection.execute(
            text(
                '''CREATE TABLE IF NOT EXISTS street3 (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    idcity INT NOT NULL,
                    FOREIGN KEY (idcity)
                        REFERENCES city (id),
                    namestr VARCHAR(55) NOT NULL
                );''')
        )
        self.connection.commit()

    def select(self, city_id: int):             #вывод улиц по выбранному городу
        return [i[-1] for i in self.connection.execute(select(self.table).where(
            self.table.c.idcity == city_id)).fetchall()]
