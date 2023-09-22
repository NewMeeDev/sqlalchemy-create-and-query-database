from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///mydb.sqlite", echo=False) # echo means - print db-actions


class Person(Base):
  
  __tablename__ = "people"
  
  ssn = Column("ssn", Integer, primary_key=True)
  firstname = Column("firstname", String)
  lastname = Column("lastname", String)
  gender = Column("gender", CHAR)
  age = Column("age", Integer)
  
  def __init__(self, ssn, firstname, lastname, gender, age):
    self.ssn = ssn
    self.firstname = firstname
    self.lastname = lastname
    self.gender = gender
    self.age = age
    
  def __repr__(self):
    return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"
  

class Thing(Base):
  
  __tablename__ = "things"
  
  tid = Column("tid", Integer, primary_key=True)
  description = Column("desription", String)
  owner = Column(Integer, ForeignKey("people.ssn"))
  
  def __init__(self, tid, description, owner):
    self.tid = tid
    self.description = description
    self.owner = owner
    
  def __repr__(self):
    return f"({self.tid}) {self.description} owned by {self.owner})"
  
  


# MAIN
if __name__ == "__main__":
   
  Base.metadata.create_all(bind=engine)

  Session = sessionmaker(bind=engine)
  session = Session()

  person = Person(12312, "Marc", "Neumann", "m", 45)
  session.add(person)
  session.commit()

  p1 = Person(32122, "Anna", "Blue", "f", 40)
  p2 = Person(12453, "Bob", "Blue", "m", 35)
  p3 = Person(24532, "Angela", "Cold", "f", 22)

  session.add(p1)
  session.add(p2)
  session.add(p3)
  session.commit()
  
  t1 = Thing(1, "Car", p1.ssn)
  t2 = Thing(2, "Laptop", p1.ssn)
  t3 = Thing(3, "PS5", p2.ssn)
  t4 = Thing(4, "Tool", p3.ssn)
  t5 = Thing(5, "Book", p3.ssn)
  
  session.add(t1)
  session.add(t2)
  session.add(t3)
  session.add(t4)
  session.add(t5)
  session.commit()
  
