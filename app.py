import os
from asyncio.windows_events import NULL

import psycopg2

from dotenv import load_dotenv
load_dotenv()

connection = psycopg2.connect(os.getenv("DATABASE_URL"))
JOIN = "SELECT * FROM users JOIN swords ON users.id = swords.owner_id ORDER BY users.id ASC;"
#cursor = connection.cursor()
with connection.cursor() as cursor:
    name = 'Jaime'
    cursor.execute("SELECT * FROM users WHERE name=%s;", (name,))
    row = cursor.fetchone()
    assert row is not None
    assert row[1] == name

    first_user = cursor.fetchall() #fetchone(), fetchall()
    cursor.execute(JOIN)
    names_swords = cursor.fetchall()

for user in names_swords:

    if user[2] == "Wolf Bane":
        assert user[2] == "Wolf Bane"
        print("Found Wolf Bane!")
        break
    else:
        print("Finding Wolf Bane..")

# for user in first_user:
#     if user[1] == 'Jaime':
#         print("I am Jaime Lannister")
#         assert user[1] == 'Jaime'
#     elif user[1] == 'Jon Snow':
#         print("I don't want it")
#     elif user[1] == 'Theon Greyjoy':
#         print("Let me defend Winterfell")
#
# print(names_swords)

#connection.close()

#%S