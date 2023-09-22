from sqlalchemy.orm import sessionmaker
from create import Person, Thing, engine

Session = sessionmaker(bind=engine)
session = Session()


# get all the people
results = session.query(Person).all()
print("\nAll People in Table:")
for r in results:
  print(r)
  
# get all the people where lastname == "Blue"
results = session.query(Person).filter(Person.lastname == "Blue")
print("\nAll People in Table where lastname == 'Blue':")
for r in results:
  print(r)
  
# get all the people where firstname like "%An%"
results = session.query(Person).filter(Person.firstname.like("%An%"))
print("\nAll People in Table where firstname like '%An%':")
for r in results:
  print(r)
  
# get all the people where firstname in ("Angela", "Anna")
results = session.query(Person).filter(Person.firstname.in_(["Angela", "Anna"]))
print("\nAll People in Table where firstname in ('Angela', 'Anna'):")
for r in results:
  print(r)

# get all things and owners data, owned by firstname in ("Angela", "Anna")
results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.firstname.in_(["Angela", "Anna"]))
print("\nAll Things and Owner-Data in DB where firstname in ('Angela', 'Anna'):")
for r in results:
  print(r)
