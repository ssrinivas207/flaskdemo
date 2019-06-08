from sqlalchemy import create_engine
db = create_engine('sqlite:///employees.sqlite')
db.echo = True

conn = db.connect()

conn.execute("DROP TABLE IF EXISTS employee")
conn.execute("DROP TABLE IF EXISTS address")

conn.execute("""
CREATE TABLE employee (id INTEGER PRIMARY KEY,  
name STRING(100) NOT NULL,
birthday DATE NOT NULL )
""")

conn.execute("""
CREATE TABLE address(
    id INTEGER PRIMARY KEY,
    street STRING(100) NOT NULL,
    number INTEGER,
    google_maps STRING(25),
    id_employee INTEGER NOT NULL,
    FOREIGN KEY (id_employee) REFERENCES employee(id)
    )""")

trans = conn.begin()
try:
    conn.execute("INSERT INTO employee (name, birthday) VALUES ('marcos mango', date('1990-09-06'));")
    conn.execute("INSERT INTO employee (name, birthday) VALUES ('rosie rinn', date('1980-09-06') );")
    conn.execute("INSERT INTO employee (name, birthday) VALUES ('mannie moon', date('1970-07-06') );")
    #inserting the values into the address table
    conn.execute("INSERT INTO address (street, number, google_maps,id_employee) VALUES ('Oak', 399, '', 1)")    
    conn.execute("INSERT INTO address (street, number, google_maps, id_employee) VALUES ('First Boulevard', 1070, '', 1)")
    conn.execute("INSERT INTO address (street, number, google_maps,id_employee) VALUES ('Cleveland, OH', 10,'Cleveland,+OH,+USA/@41.4949426,-81.70586,11z', 2)")

    trans.commit()
except:
    trans.rollback()
    raise

#query to get the marcos mango address

for row in conn.execute("""SELECT * from address a left join employee e on a.id_employee = e.id where e.name like 'marcos mango'"""):
    print("address :", row)
conn.close()

