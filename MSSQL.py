import pyodbc

file = open('Query', 'r')
query = file.read()

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.80.52.11;DATABASE=ASUZD; Trusted_connection=yes')
                      # 'UID=se\\abduragimov-ga;PWD=Gfhjkm1987!')

if cnxn:
    print('Connect')
cursor = cnxn.cursor()

# cursor.execute('update _test_usr set Email = \'123\' where Email = \'321\'')
# cnxn.commit()
# cursor.execute('select * from _test_usr where Email = \'Voroshilov-SV@rosseti-ural.ru\'')
rows = cursor.execute(query).fetchall()
# rows = cursor.fetchall()
print(len(rows))
# print(len(rows))
for row in rows:
    print(row)
# if cursor.fetchall():
# print(cursor.fetchall())


cnxn.close()
