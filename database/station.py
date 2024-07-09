import sqlalchemy
from sqlalchemy import select
from database import Database
from database.models import NewStation
from sqlalchemy import text


class StationDatabase(Database):
    def __init__(self):
        super().__init__()
        self.table = sqlalchemy.Table("station", self.metadata)
        self.connection.execute(text(
                    '''CREATE TABLE IF NOT EXISTS station (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        namestaiton VARCHAR(55) NOT NULL,
                        timeopen TIME,
                        timeclose TIME,
                        idstr INT NOT NULL,
                        FOREIGN KEY (idstr)
                            REFERENCES street (id)
                    );''')
        )
        self.connection.commit()

    def select(self, data: {}):     #select запрос, видоизменяющийся в зависимости от входных параметров
        SSQL = f'SELECT  station.namestaiton, station.timeopen, station.timeclose, street.namestr, (SELECT namecity FROM city WHERE (street.idcity = id)) AS CityName FROM station LEFT JOIN street ON station.idstr = street.id'

        if not data:
            _SQL = text(SSQL+';')
        else:
            SSQL = SSQL + ' HAVING ('
            if data['namecity']: SSQL = SSQL + f"CityName = '{data['namecity']}' AND "
            if data['namestr']: SSQL = SSQL + f"namestr = '{data['namestr']}' AND "
            if data['is_open'] == 1: SSQL = SSQL + "(timeopen < current_time() AND timeclose > current_time()) AND "
            elif data['is_open'] == 0: SSQL = SSQL + "(timeopen > current_time() OR timeclose < current_time()) AND "
            SSQL = SSQL[:-5]
            _SQL = text(SSQL + ");")
        res = self.connection.execute(_SQL).fetchall()
        return str(res)

    def insert(self, data: NewStation):     #создание новой точки СТО
        print(data.dict())
        self.connection.execute(self.table.insert().values(data.dict()))
        self.connection.commit()
        id_s = self.connection.execute(select(self.table.c.id).where(
            self.table.c.namestaiton == data.namestaiton,
            self.table.c.nhouse == data.nhouse,
            self.table.c.timeopen == data.timeopen,
            self.table.c.timeclose == data.timeclose,
            self.table.c.idstr == data.idstr
        )).fetchall()
        return int(id_s[-1][0])


if __name__ == "__main__":
    d = StationDatabase()
    print(d.select({}))

