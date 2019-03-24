from hashlib import md5

from threading import Timer
from sqlalchemy import *
from sqlalchemy.orm import *


def getConnection(host, database, user, password):
    url = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(user, password, host, database)
    engine = create_engine(url)
    #with connect(host=host, user=user, password=password, database=database) as mysqlConn:
    return engine.connect()


def getResultSet(connection, tableName):
    cursor = connection.cursor()


def getSession(host, database, user, password):
    url = "mysql+mysqlconnector://{0}:{1}@{2}:3306/{3}".format(user, password, host, database)
    print(url)
    DBSession = sessionmaker(bind=create_engine(url, max_overflow=5))
    return DBSession()


def main():
    connection = getConnection("10.0.0.17", "walletnowx", "walletnow", "2bSXaBN%GTicy")


if __name__ == '__main__':
    main()
