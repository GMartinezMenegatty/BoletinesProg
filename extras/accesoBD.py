import sqlite3 as bdapi

bbdd = bdapi.connect('baseExemplo.bd')
print(bbdd)

cursor = bbdd.cursor()
print (cursor)

"""cursor.execute('''CREATE TABLE empregados (dni text, nome text, antiguedade integer)''')"""

"""cursor.execute('''INSERT INTO empregados VALUES (?, ?, ?)''', ('7777U', 'Zoe', '18'))"""

bbdd.commit()

    cursor.execute('''SELECT dni, nome, antiguedade FROM empregados''')
    unRexistro = cursor.fetchone()
    print(unRexistro)

except dbapi.OperationalError as e:
    print(e)
bbdd.close()