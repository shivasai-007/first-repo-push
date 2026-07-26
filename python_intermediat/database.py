import sqlite3

class person :
    def __init__(self,id_number=-1,first="",last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last 
        self.age = age
        self.connection = sqlite3.connect("mydata.db")
        self.cursor = self.connection.cursor()

    def load_person(self,id_number):
        self.cursor.execute("""
        SELECT * FROM person 
        WHERE id = {}
        """.format(id_number))

        result = self.cursor.fetchone()

        self.id_number = id_number
        self.first = result[1]
        self.last = result[2]
        self.age = result[3]


    def insert_person(self):
        self.cursor.execute(
            """
            INSERT INTO person VALUES({},'{}','{}',{})
            """.format(self.id_number,self.first,self.last,self.age)
        )
        self.connection.commit()



# connection = sqlite3.connect("mydata.db")
# cursor = connection.cursor()



# cursor.execute("""
# CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY ,
#     first_name TEXT,
#     last_name TEXT,
#     age INTEGER
# );
# """)
# cursor.execute("""
# INSERT INTO person VALUES 
# (1,"shivasai","byroju",19),
# (2,"karthikeya ","gancari ",19)

# """)

# cursor.execute("""
# SELECT * FROM person 
# """)

# rows = cursor.fetchall()
# print(rows)

# connection.commit()

# connection.close()

p1 = person(7,"vijju","kummar",30)
p1.insert_person()
# p1.load_person(1)
# print(p1.first)
# print(p1.last)
# print(p1.age)
# print(p1.id_number)



connection = sqlite3.connect("mydata.db")
cursor = connection.cursor()


cursor.execute("""
SELECT * FROM person 
""")

rows = cursor.fetchall()
print(rows,end ='\n')