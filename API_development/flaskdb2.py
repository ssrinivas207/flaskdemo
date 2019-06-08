from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime 
import datetime 

engine = create_engine('sqlite:///employees.sqlite')
engine.echo = True

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()

# creating a model

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key = True)
    street = Column(String(100))
    number = Column(Integer)
    google_maps = Column(String(255))
    id_employee = Column(Integer, ForeignKey('employee.id'))

    def __repr__(self):
        return u"%s, %d" %(self.street,self.number)

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key= True)
    name = Column(String(100))
    birthday = Column(Date)
    addresses = relationship("Address", backref = "employee")

    def __repr__(self):
        return self.name

Base.metadata.create_all(engine)

session.add_all([Employee(name='marcos mango',birthday=datetime.datetime.strptime('1990-09-06', '%Y-%m-%d')),
Employee(name='rosie rinn',birthday=datetime.datetime.strptime('1980-09-06', '%Y-%m-%d')),
Employee(name='mannie moon',birthday=datetime.datetime.strptime('1970-07-06', '%Y-%m-%d'))])

session.commit()

session.add_all([Address(street='Oak', number=399, google_maps='',id_employee=1),
Address(street='First Boulevard', number=1070, google_maps='',id_employee=1),
Address(street='Cleveland, OH', number=10,google_maps='Cleveland,+OH,+USA/@41.4949426,-81.70586,11z', id_employee=2)]) 

session.commit()

marcos = session.query(Employee).filter(Employee.name.like(r"%marcos%")).first()
for address in marcos.addresses:
    print("Address: ", address)

