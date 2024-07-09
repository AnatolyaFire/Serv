import sqlalchemy
from sqlalchemy import URL


class Database:
    def __init__(self):
        self.url_object = URL.create(
            "mysql+pymysql",
            username="root",

            password="Edgar123321",     #---необходимо вставить свой свой пароль от аккаунта root в MySQL
            host="127.0.0.1",

            database="serv",            #---необходимо указать название свой базы данных или создать под названием serv
        )
        self.engine = sqlalchemy.create_engine(
            url=self.url_object,
            echo=True
        )
        self.connection = self.engine.connect()
        self.metadata = sqlalchemy.MetaData()
        self.metadata.reflect(self.engine)
