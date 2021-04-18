from sqlalchemy import INTEGER, Column, ForeignKey, String
from sqlalchemy.orm import declarative_base, relationship

# declarative base class
Base = declarative_base()

class Query(Base):
	__tablename__ = 'query'

	region = Column(String)
	search_query = Column(String)


class Time(Base):
	__tablename__ = 'time'

	query = relationship("Query", back_populates="qr")
	count = Column(Integer)
	time = Column(Integer)