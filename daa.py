import sqlite3 as db
import platform
import psutil
from datetime import date
con = db.connect('debby.db')
cursor = con.cursor()
info = platform.system() + ' ' + str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + "GB"
# cursor.execute("""CREATE TABLE encrypt(
#                username text PRIMARY KEY,
#                password text,
#                aes BLOB,
#                pbk BLOB,
#                pvk BLOB,

#         )""")
# cursor.execute("""CREATE TABLE encrypt (
#                username TEXT PRIMARY KEY,
#                password TEXT,
#                aes BLOB,
#                pbk BLOB,
#                pvk BLOB
# )""")
# cursor.execute("INSERT INTO encrypt VALUES ('pilla', '1234', 'abcdefghijklmnop','abgfdhgduw','hjkhuiybjbnjhj')")
# con.commit()
# cursor.execute("DROP TABLE encrypt")
# con.commit()
def ins(name, pwd, aes, pbk, pvk):
    con = db.connect('debby.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO encrypt VALUES (?, ?, ?, ?, ?)", (name, pwd, aes,pbk,pvk))
    con.commit()
# ins('Krish', 'k234', b'abcdefghijklmnop', b'1234', b'5678')
def showdata():
    con = db.connect('debby.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM encrypt")
    print(cursor.fetchall())

def get(un, pd):
    con = db.connect('debby.db')
    cursor = con.cursor()
    l = list(cursor.execute("SELECT username, password, aes, pbk, pvk FROM encrypt WHERE username=?", (un,)))
    # print(l)
    # cursor.execute("DELETE FROM steg WHERE username=?",(un,))
    if not l:
        return -1,l
    if pd==l[0][1]:
        cursor.execute("DELETE FROM encrypt WHERE username=?",(un,))
        con.commit()
        # showdata()
        return 1,l
    # cursor.execute("DELETE FROM encrypt WHERE username=?",(un,))
    # con.commit()
    # showdata()
    return 0,l
# cursor.execute("""CREATE TABLE stego(
#                username text PRIMARY KEY,
#                password text,
#                frame INTEGER,
#                key text
#         )""")

# cursor.execute("DROP TABLE stego")
# con.commit()
# print(get('chandana', '123'))
# cursor.execute("INSERT INTO stego VALUES ('pilla', '1234', '12','hello')")
# con.commit()

def vid(un, pd, fn, k):
    con = db.connect('debby.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO stego VALUES (?, ?, ?, ?)", (un, pd, fn, k))
    con.commit()

def getvid(un, pd, fn, k):
    con = db.connect('debby.db')
    cursor = con.cursor()
    l = list(cursor.execute("SELECT username, password, frame, key FROM stego WHERE username=?", (un,)))
    # print(l)
    if not l:
        return -1,l
    if un!=l[0][0]:
        return 0,l
    if pd!=l[0][1]:
        return 1,l
    if fn!=l[0][2]:
        return 2,l
    if k!=l[0][-1]:
        return 3,l
    cursor.execute("DELETE FROM stego WHERE username=?",(un,))
    con.commit()
    cursor.execute("SELECT username, password FROM stego")
    print(cursor.fetchall())

    return 5,l



# cursor.execute("SELECT * FROM stego")
# print(cursor.fetchall())

con.close()