import MySQLdb

host="localhost"
user="app"
password="1234"
db="escola_curso"
port=3306

con = MySQLdb.connect(host, user, password, db, port)
c = con.cursor(MySQLdb.cursors.DictCursor) # variable to do query, adding MySQLdb.cursors.DictCursor results will be returned as dictionaries

# SELECT fields FROM table (WHERE condition)
def select(fields, tables, where=None):

    global c

    query = "SELECT " + fields + " FROM " + tables
    if (where): #if theres is a where, then assign it to query
        query = query + ' WHERE ' + where

    c.execute(query) #execute SQL query
    return c.fetchall() #return all results from query

# INSERT INTO table (fields) VALUES (...), (...), (...)
def insert(values, table, fields=None):
    global c, con
    
    query = "INSERT INTO " + table
    if (fields): #if there is a specific column, them do INSERT INTO table (field1, field2, field3...) VALUES (...)
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values]) #this will put values inside () and concatenate then with ","

    c.execute(query)
    con.commit()

#UPDATE table SET field = 'value' (WHERE condition)
def update(sets, table, where=None):
    global c, con
    # print(sets) #sets is a dictionarie with 'key': 'value'
    # print(sets.items()) #will create a array of tuples (key1, value1), (key2, value2) for each attribute in sets
    # for field, value in sets.items():
    #     print(field, value) #for will search in each tuple then print their respective key, value

    query = "UPDATE " + table + " SET " + ", ".join([field + " = '" + value + "'" for field, value in sets.items()])
    # for each tuple will return key = 'value', 
    if (where):
        query = query + " WHERE " + where
    
    c.execute(query)
    con.commit()

#DELETE FROM table WHERE condition
def delete(table, where):
    global c, con

    query = "DELETE FROM " + table + " WHERE " + where

    c.execute(query)
    con.commit()


# print(select("*", 'alunos', 'id_aluno = 8'))