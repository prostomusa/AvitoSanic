from sqlalchemy import INTEGER, Column, String, DateTime
from sqlalchemy.orm import declarative_base, relationship

# declarative base class
Base = declarative_base()

class QueryList(Base):
	__tablename__ = 'querylist'

	id = Column(INTEGER(), primary_key=True)
	region = Column(String)
	search_query = Column(String)


class Time(Base):
	__tablename__ = 'time'

	id = Column(INTEGER(), primary_key=True)
	query_list = relationship("QueryList", cascade="all, delete", back_populates="qr")
	count = Column(INTEGER())
	time = Column(DateTime)