from aiogram.utils import executor
from create_bot import dp
from database import shop_db, order_db
from aiogram import types

async def on_startup(dp):
	print('Bot online...')
	shop_db.sql_start()
	order_db.sql_start()
	await dp.bot.set_my_commands([
		types.BotCommand("start", "Запустить бота")])


from handlers import client

client.register_handlers_client(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)