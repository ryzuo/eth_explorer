from sqlalchemy.sql import sqltypes as sqltypes
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

Base = declarative_base()


class Block(Base):
    __tablename__ = 'blocks'

    number = Column(Integer, name='number', primary_key=True)
    blockHash = Column(String(256), name='hash')
    gasLimit = Column(DECIMAL(50, 18), name='gas_limit')
    gasUsed = Column(DECIMAL(50, 18), name='gas_used')
    size = Column(Integer, name='size')
    ts = Column(BigInteger, name='ts')


class Transaction(Base):
    __tablename__ = 'transactions'

    id1 = Column(BigInteger, name='id1', primary_key=True)
    id2 = Column(BigInteger, name='id2', primary_key=True)
    id3 = Column(BigInteger, name='id3', primary_key=True)
    id4 = Column(BigInteger, name='id4', primary_key=True)
    bnumber = Column(Integer, name='block_number')
    value = Column(DECIMAL(50, 18), name='eth_value')
    fromAddr = Column(String(128), name='from_addr')
    toAddr = Column(String(128), name='to_addr')
    contract = Column(String(128), name='contract')
    tokenValue = Column(DECIMAL(50, 18), name='token_value')
    succeed = Column(Boolean, name='succeed')
    gasUsed = Column(DECIMAL(50, 18), name='gas')
    gasPrice = Column(DECIMAL(50, 18), name='gas_price')
    ts = Column(BigInteger, name='ts')

    __table_args__ = (
        PrimaryKeyConstraint(id1, id2, id3, id4)
    )


"""
class Wallet(Base):
    __tablename__ = 'wallets'

    number = Column(Integer, name='number', primary_key=True)
    blockHash = Column(String(256), name='hash')
    gasLimit = Column(String(256), name='gas_limit')
    gasUsed = Column(String(256), name='gas_used')
    size = Column(Integer, name='size')
    ts = Column(TIMESTAMP, name='ts')
"""


class Token(Base):
    __tablename__ = 'tokens'

    id1 = Column(BigInteger, name='id1', primary_key=True)
    id2 = Column(BigInteger, name='id2', primary_key=True)
    id3 = Column(BigInteger, name='id3', primary_key=True)
    name = Column(String(96), name='name')
    decimals = Column(SMALLINT, name='decimals')

    __table_args__ = (
        PrimaryKeyConstraint(id1, id2, id3)
    )
