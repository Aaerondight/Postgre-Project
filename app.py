import os
import psycopg2

from dotenv import load_dotenv
load_dotenv()

connection = psycopg2.connect(os.getenv("DATABASE_URL"))

#cursor = connection.cursor()
with connection.cursor() as cursor:
    name = 'Jaime'
    cursor.execute("SELECT * FROM users WHERE name=%s;", (name,))
    row = cursor.fetchone()
    print(row)
    first_user = cursor.fetchall() #fetchone(), fetchall()
    cursor.execute("SELECT * FROM users JOIN swords ON users.id = swords.owner_id")
    names_swords = cursor.fetchall()

for user in first_user:
    if user[1] == 'Jaime':
        print("I am Jaime Lannister")
        assert user[1] == 'Jaime'
    elif user[1] == 'Jon Snow':
        print("I don't want it")
    elif user[1] == 'Theon Greyjoy':
        print("Let me defend Winterfell")

print(names_swords)

#connection.close()

#%S