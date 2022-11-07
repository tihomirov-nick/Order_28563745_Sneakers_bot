import sqlite3 as sq

from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('shop.db')
    cur = base.cursor()
    if base:
        print("data base 'shop.db' connected")
    base.execute('CREATE TABLE IF NOT EXISTS REVIEW(message TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS NEWBALANCE(name TEXT, price TEXT, photo_id TEXT, size_min INT, size_max INT)')
    base.execute('CREATE TABLE IF NOT EXISTS ADIDAS(name TEXT, price TEXT, photo_id TEXT, size_min INT, size_max INT)')
    base.execute('CREATE TABLE IF NOT EXISTS NIKE(name TEXT, price TEXT, photo_id TEXT, size_min INT, size_max INT)')
    base.execute('CREATE TABLE IF NOT EXISTS CONVERSE(name TEXT, price TEXT, photo_id TEXT, size_min INT, size_max INT)')
    base.execute('CREATE TABLE IF NOT EXISTS VANS(name TEXT, price TEXT, photo_id TEXT, size_min INT, size_max INT)')
    base.commit()


async def sql_read_review(callback_query):
    for ret in cur.execute('SELECT * FROM REVIEW').fetchall():
        await bot.send_message(callback_query.message.chat.id, text=f'{ret[0]}')


async def sql_set_review(mess):
    cur.execute(f"INSERT INTO REVIEW VALUES ('{mess}')")
    base.commit()


async def sql_delete_read_review(callback_query):
    return cur.execute('SELECT rowid, * FROM REVIEW').fetchall()


async def sql_delete_review(item_message):
    cur.execute(f'''DELETE FROM REVIEW WHERE rowid == "{item_message}"''')
    base.commit()


# Items

async def sql_read_newbalance():
    return cur.execute('SELECT * FROM NEWBALANCE').fetchall()


async def sql_read_adidas():
    return cur.execute('SELECT * FROM ADIDAS').fetchall()


async def sql_read_nike():
    return cur.execute('SELECT * FROM NIKE').fetchall()


async def sql_read_converse():
    return cur.execute('SELECT * FROM CONVERSE').fetchall()


async def sql_read_vans():
    return cur.execute('SELECT * FROM VANS').fetchall()


# Size

async def sql_read_newbalance_size(item):
    return cur.execute(f'''SELECT * FROM NEWBALANCE WHERE name == "{item}"''').fetchall()


async def sql_read_adidas_size(item):
    return cur.execute(f'''SELECT * FROM ADIDAS WHERE name == "{item}"''').fetchall()


async def sql_read_nike_size(item):
    return cur.execute(f'''SELECT * FROM NIKE WHERE name == "{item}"''').fetchall()


async def sql_read_converse_size(item):
    return cur.execute(f'''SELECT * FROM CONVERSE WHERE name == "{item}"''').fetchall()


async def sql_read_vans_size(item):
    return cur.execute(f'''SELECT * FROM VANS WHERE name == "{item}"''').fetchall()


# Add

async def sql_add_newbalance(name, price, photo_id, size_min, size_max):
    cur.execute(f'''INSERT INTO NEWBALANCE VALUES ("{name}", "{price}", "{photo_id}", "{size_min}", "{size_max}")''')
    base.commit()


async def sql_add_adidas(name, price, photo_id, size_min, size_max):
    cur.execute(f'''INSERT INTO ADIDAS VALUES  ("{name}", "{price}", "{photo_id}", "{size_min}", "{size_max}")''')
    base.commit()


async def sql_add_nike(name, price, photo_id, size_min, size_max):
    cur.execute(f'''INSERT INTO NIKE VALUES  ("{name}", "{price}", "{photo_id}", "{size_min}", "{size_max}")''')
    base.commit()


async def sql_add_converse(name, price, photo_id, size_min, size_max):
    cur.execute(f'''INSERT INTO CONVERSE VALUES  ("{name}", "{price}", "{photo_id}", "{size_min}", "{size_max}")''')
    base.commit()


async def sql_add_vans(name, price, photo_id, size_min, size_max):
    cur.execute(f'''INSERT INTO VANS VALUES  ("{name}", "{price}", "{photo_id}", "{size_min}", "{size_max}")''')
    base.commit()


# Delete

async def sql_del_mewbalance(name):
    cur.execute(f'''DELETE FROM NEWBALANCE WHERE name == "{name}"''')
    base.commit()


async def sql_del_adidas(name):
    cur.execute(f'''DELETE FROM ADIDAS WHERE name == "{name}"''')
    base.commit()


async def sql_del_nike(name):
    cur.execute(f'''DELETE FROM NIKE WHERE name == "{name}"''')
    base.commit()


async def sql_del_converse(name):
    cur.execute(f'''DELETE FROM CONVERSE WHERE name == "{name}"''')
    base.commit()


async def sql_del_vans(name):
    cur.execute(f'''DELETE FROM VANS WHERE name == "{name}"''')
    base.commit()
