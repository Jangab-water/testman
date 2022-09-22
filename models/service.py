from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.schema import base

class ConnectionEngine:
    def __init__(self, config_path) -> None:
        cfg=ConfigParser()
        cfg.read(config_path)
        user, passwd, host, port, db_name=cfg['database']['user'], cfg['database']['passwd'], cfg["database"]['host'], cfg['database']['port'], cfg["database"]["db_name"]
        self.engine=create_engine(url=f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8mb4")

    def create(self):
        base.metadata.create_all(bind=self.engine)

    @property
    def get_engine(self):
        return self.engine

    @property
    def get_session(self):
        session_factory=sessionmaker(bind=self.engine)
        session=scoped_session(session_factory)
        return session

Engine=ConnectionEngine("./properties.ini")