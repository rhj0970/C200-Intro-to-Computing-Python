import sqlite3

dog = sqlite3.connect("example1.db")
c = dog.cursor()
r = [("c","a"),("a","b"), ("a","e"),("c","d"),("c","f"),("f","g"), ("f","h"),("h","j"),("h","i")]

#c.execute("""CREATE TABLE T (Parenttext, Child)""")

#c.executemany("INSERT INTO T VALUES (?,?)", r)

#dog.commit()


q = lambda x,y: "SELECT Parenttext FROM T WHERE Child = '{}' AND Parenttext =(SELECT Parenttext FROM T WHERE Child = '{}')".format(x,y)


#TO DO: Implement Lambda function

print(c.execute(q("b","e")).fetchone())
print(c.execute(q("h","g")).fetchone())
print(c.execute(q("e","a")).fetchone())
dog.close()