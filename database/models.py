from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Date

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RetailSales(Base):
    __tablename__ = "retail_sales"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(Date)

    store = Column(Integer)

    item = Column(Integer)

    sales = Column(Integer)