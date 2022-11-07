import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('order.db')
    cur = base.cursor()
    if base:
        print("data base 'order.db' connected")
    base.execute(
        'CREATE TABLE IF NOT EXISTS ORDERS(brand TEXT, item TEXT, size TEXT, contacts TEXT, name TEXT, id TEXT)')


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO ORDERS VALUES (?, ?, ?, ?, ?, ?)", tuple(data.values()))
        base.commit()


async def sql_read(id):
    return cur.execute(f'SELECT * FROM ORDERS WHERE id == {id}').fetchall()


async def sql_delete(item, size, id):
    cur.execute(f"DELETE FROM ORDERS WHERE item == '{str(item)}' and size == '{str(size)}' and id == '{str(id)}'")
    base.commit()


async def sql_delete_all(id):
    cur.execute(f"DELETE FROM ORDERS WHERE id == '{str(id)}'")
    base.commit()
