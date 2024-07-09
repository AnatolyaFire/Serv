import sqlalchemy
from sqlalchemy import select
from sqlalchemy import text
from database import Database


class CityDatabase(Database):
    def __init__(self):
        super().__init__()
        self.table = sqlalchemy.Table("city", self.metadata)
        self.connection.commit()
        self.connection.execute(text(
            ''' CREATE TABLE IF NOT EXISTS city( 
    id INT AUTO_INCREMENT PRIMARY KEY,
namecity VARCHAR(55) NOT NULL UNIQUE);
        ''')
        )
        self.connection.commit()

    def select(self):
        a = [i[1] for i in self.connection.execute(select(self.table)).fetchall()]
        return a
