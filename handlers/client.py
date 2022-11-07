from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from create_bot import bot
from database import shop_db

call_start_btn = InlineKeyboardButton('Главное меню', callback_data='call_command_start')
start_btn = InlineKeyboardButton('Ассортимент товаров', callback_data='menu')
rep_btn = InlineKeyboardButton('Отзывы', callback_data='rep')
about_btn = InlineKeyboardButton('О нас', callback_data='about')
start_kb = InlineKeyboardMarkup().add(start_btn).add(rep_btn, about_btn)

menu_btn_newbalance = InlineKeyboardButton('NEW BALANCE', callback_data='newbalance')
menu_btn_adidas = InlineKeyboardButton('YEEZY', callback_data='adidas')
menu_btn_nike = InlineKeyboardButton('NIKE', callback_data='nike')
menu_btn_converse = InlineKeyboardButton('CONVERSE', callback_data='converse')
menu_btn_vans = InlineKeyboardButton('VANS', callback_data='vans')
menu_kb = InlineKeyboardMarkup().add(menu_btn_newbalance).add(menu_btn_adidas, menu_btn_nike).add(menu_btn_converse, menu_btn_vans).add(call_start_btn)

add_menu_btn_newbalance = InlineKeyboardButton('NEW BALANCE', callback_data='add_newbalance')
add_menu_btn_adidas = InlineKeyboardButton('YEEZY', callback_data='add_adidas')
add_menu_btn_nike = InlineKeyboardButton('NIKE', callback_data='add_nike')
add_menu_btn_converse = InlineKeyboardButton('CONVERSE', callback_data='add_converse')
add_menu_btn_vans = InlineKeyboardButton('VANS', callback_data='add_vans')
add_menu_kb = InlineKeyboardMarkup().add(add_menu_btn_newbalance).add(add_menu_btn_adidas, add_menu_btn_nike).add(add_menu_btn_converse, add_menu_btn_vans)

del_menu_btn_newbalance = InlineKeyboardButton('Удалить из NEW BALANCE', callback_data='deleting_item_newbalance')
del_menu_btn_adidas = InlineKeyboardButton('Удалить из YEEZY', callback_data='deleting_item_adidas')
del_menu_btn_nike = InlineKeyboardButton('Удалить из NIKE', callback_data='deleting_item_nike')
del_menu_btn_converse = InlineKeyboardButton('Удалить из CONVERSE', callback_data='deleting_item_converse')
del_menu_btn_vans = InlineKeyboardButton('Удалить из VANS', callback_data='deleting_item_vans')
del_menu_kb = InlineKeyboardMarkup().add(del_menu_btn_newbalance).add(del_menu_btn_adidas, del_menu_btn_nike).add(del_menu_btn_converse, del_menu_btn_vans)


class Client_data(StatesGroup):
    brand = State()
    item = State()
    size = State()
    contacts = State()
    name = State()
    id = State()


class Review(StatesGroup):
    mess = State()


class NewItem(StatesGroup):
    brand = State()
    name = State()
    price = State()
    photo_id = State()
    min_r = State()
    max_r = State()


class DelItem(StatesGroup):
    brand = State()


async def command_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await bot.send_photo(message.from_user.id, "AgACAgIAAxkBAAMKYqpTCWTLfoSRn6WW725N7ZwltRAAAhm_MRvLGVBJN7u1hsSAGscBAAMCAANzAAMkBA", caption='''*Интернет-магазин кроссовок "CROSS MARKET" приветствует Вас!*''', reply_markup=start_kb, parse_mode="Markdown")


async def call_command_start(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await callback_query.message.delete()
    await bot.send_photo(callback_query.message.chat.id, "AgACAgIAAxkBAAMKYqpTCWTLfoSRn6WW725N7ZwltRAAAhm_MRvLGVBJN7u1hsSAGscBAAMCAANzAAMkBA", caption='''*Интернет-магазин кроссовок "CROSS MARKET" приветствует Вас!*''', reply_markup=start_kb, parse_mode="Markdown")


async def admin_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await bot.send_photo(message.from_user.id, "AgACAgIAAxkBAAMKYqpTCWTLfoSRn6WW725N7ZwltRAAAhm_MRvLGVBJN7u1hsSAGscBAAMCAANzAAMkBA", caption='''*Панель администратора интернет-магазинa кроссовок "CROSS MARKET" приветствует Вас!*''',
                         reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Посмотреть/удалить отзывы', callback_data='delete_review')).add(InlineKeyboardButton('Добавить товар', callback_data='add_item')).add(InlineKeyboardButton('Удалить товар', callback_data='dele_items')), parse_mode="Markdown")


async def call_admin_start(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await callback_query.message.delete()
    await bot.send_photo(callback_query.message.chat.id, "AgACAgIAAxkBAAMKYqpTCWTLfoSRn6WW725N7ZwltRAAAhm_MRvLGVBJN7u1hsSAGscBAAMCAANzAAMkBA", caption='''*Панель администратора интернет-магазинa кроссовок "CROSS MARKET" приветствует Вас!*''',
                         reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Посмотреть/удалить отзывы', callback_data='delete_review')).add(InlineKeyboardButton('Добавить товар', callback_data='add_item')).add(InlineKeyboardButton('Удалить товар', callback_data='dele_items')), parse_mode="Markdown")


async def delete_review_menu(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await callback_query.message.delete()
    rowid = await shop_db.sql_delete_read_review(callback_query)
    for row in rowid:
        await bot.send_message(callback_query.message.chat.id, text=f'{row[1]}', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'''Удалить отзыв''', callback_data=f'''del {row[0]}''')))
    await bot.send_message(callback_query.message.chat.id, text="Если вы не хотите удалять отзывы, нажмите кнопку", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("Отменить", callback_data='call_admin_start')))



async def delete_review(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await callback_query.message.delete()
    item = callback_query.data.replace('del ', '')
    await shop_db.sql_delete_review(item)
    await bot.send_message(callback_query.message.chat.id, '*Отзыв успешно удален*', parse_mode="Markdown")
    await bot.send_photo(callback_query.message.chat.id, "AgACAgIAAxkBAAMKYqpTCWTLfoSRn6WW725N7ZwltRAAAhm_MRvLGVBJN7u1hsSAGscBAAMCAANzAAMkBA",caption='''*Панель администратора интернет-магазинa кроссовок "CROSS MARKET" приветствует Вас!*''', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Посмотреть/удалить отзывы', callback_data='delete_review')).add(InlineKeyboardButton('Добавить товар', callback_data='add_item')).add(InlineKeyboardButton('Удалить товар', callback_data='dele_items')), parse_mode="Markdown")


async def add_item(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.send_message(callback_query.message.chat.id, text='Выберите бренд', reply_markup=add_menu_kb.add(InlineKeyboardButton("Отменить", callback_data='call_admin_start')))
    await NewItem.brand.set()


async def add_item_brand(callback_query: types.CallbackQuery, state: FSMContext):
    brand = callback_query.data.replace('add_', '')
    async with state.proxy() as data:
        data['brand'] = brand
        print(data['brand'])
    await bot.send_message(callback_query.message.chat.id, text='Введите название товара')
    await NewItem.name.set()


async def add_item_name(message: types.Message, state: FSMContext):
    name = message.text
    async with state.proxy() as data:
        data['name'] = name
    await bot.send_message(message.chat.id, text='Введите цену товара')
    await NewItem.price.set()


async def add_item_price(message: types.Message, state: FSMContext):
    price = message.text
    async with state.proxy() as data:
        data['price'] = price
    await bot.send_message(message.chat.id, text='Пришлите фото товара')
    await NewItem.photo_id.set()


async def add_item_photo(message: types.Message, state: FSMContext):
    photo_id = message.photo[0].file_id
    async with state.proxy() as data:
        data['photo_id'] = photo_id
    await bot.send_message(message.chat.id, text='Введите минимальный размер')
    await NewItem.min_r.set()


async def add_item_min_r(message: types.Message, state: FSMContext):
    min_r = message.text
    async with state.proxy() as data:
        data['min_r'] = min_r
    await bot.send_message(message.chat.id, text='Введите максимальный размер')
    await NewItem.max_r.set()


async def add_item_max_r(message: types.Message, state: FSMContext):
    max_r = message.text
    async with state.proxy() as data:
        data['max_r'] = max_r
        brand = data['brand']
    if brand == 'newbalance':
        await shop_db.sql_add_newbalance(data['name'], data['price'], data['photo_id'], data['min_r'], data['max_r'])
    elif brand == 'adidas':
        await shop_db.sql_add_adidas(data['name'], data['price'], data['photo_id'], data['min_r'], data['max_r'])
    elif brand == 'nike':
        await shop_db.sql_add_nike(data['name'], data['price'], data['photo_id'], data['min_r'], data['max_r'])
    elif brand == 'converse':
        await shop_db.sql_add_converse(data['name'], data['price'], data['photo_id'], data['min_r'], data['max_r'])
    elif brand == 'vans':
        await shop_db.sql_add_vans(data['name'], data['price'], data['photo_id'], data['min_r'], data['max_r'])
    await bot.send_message(message.chat.id, text='Товар успешно добавлен', reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton('Посмотреть/удалить отзывы', callback_data='delete_review'),
            InlineKeyboardButton('Добавить товар', callback_data='add_item'),
            InlineKeyboardButton('Удалить товар', callback_data='dele_items')))
    await state.finish()


async def del_item_start(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, text='Выберите бренд для удаления товара',
                           reply_markup=del_menu_kb.add(InlineKeyboardButton("Отменить", callback_data='call_admin_start')))
    await DelItem.brand.set()


async def del_item_brand(callback_query: types.CallbackQuery, state: FSMContext):
    brand = callback_query.data.replace('deleting_item_', '')
    async with state.proxy() as data:
        data['brand'] = brand
    if brand == 'newbalance':
        items = await shop_db.sql_read_newbalance()
        for item in items:
            await bot.send_photo(callback_query.message.chat.id, f'''{item[2]}''', caption=f'''{item[0]}''',
                                 reply_markup=InlineKeyboardMarkup().add(
                                         InlineKeyboardButton(f'''Удалить''', callback_data=f'''delete {item[0]}''')))
    elif brand == 'adidas':
        items = await shop_db.sql_read_adidas()
        for item in items:
            await bot.send_photo(callback_query.message.chat.id, f'''{item[2]}''', caption=f'''{item[0]}''',
                                 reply_markup=InlineKeyboardMarkup().add(
                                         InlineKeyboardButton(f'''Удалить''', callback_data=f'''delete {item[0]}''')))
    elif brand == 'nike':
        items = await shop_db.sql_read_nike()
        for item in items:
            await bot.send_photo(callback_query.message.chat.id, f'''{item[2]}''', caption=f'''{item[0]}''',
                                 reply_markup=InlineKeyboardMarkup().add(
                                         InlineKeyboardButton(f'''Удалить''', callback_data=f'''delete {item[0]}''')))
    elif brand == 'converse':
        items = await shop_db.sql_read_converse()
        for item in items:
            await bot.send_photo(callback_query.message.chat.id, f'''{item[2]}''', caption=f'''{item[0]}''',
                                 reply_markup=InlineKeyboardMarkup().add(
                                         InlineKeyboardButton(f'''Удалить''', callback_data=f'''delete {item[0]}''')))
    elif brand == 'vans':
        items = await shop_db.sql_read_vans()
        for item in items:
            await bot.send_photo(callback_query.message.chat.id, f'''{item[2]}''', caption=f'''{item[0]}''',
                                 reply_markup=InlineKeyboardMarkup().add(
                                         InlineKeyboardButton(f'''Удалить''', callback_data=f'''delete {item[0]}''')))


async def del_item(callback_query: types.CallbackQuery, state: FSMContext):
    item = callback_query.data.replace('delete ', '')
    async with state.proxy() as data:
        brand = data['brand']
    if brand == 'newbalance':
        await shop_db.sql_del_mewbalance(item)
    elif brand == 'adidas':
        await shop_db.sql_del_adidas(item)
    elif brand == 'nike':
        await shop_db.sql_del_nike(item)
    elif brand == 'converse':
        await shop_db.sql_del_converse(item)
    elif brand == 'vans':
        await shop_db.sql_del_vans(item)
    await bot.send_message(callback_query.message.chat.id, text='''Товар успешно удален''', reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton('Посмотреть/удалить отзывы', callback_data='delete_review'),
            InlineKeyboardButton('Добавить товар', callback_data='add_item'),
            InlineKeyboardButton('Удалить товар', callback_data='dele_items')))
    await state.finish()


async def about(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.message.chat.id,
                         "AgACAgIAAxkBAAMKYqpTCWTLfoSRn6WW725N7ZwltRAAAhm_MRvLGVBJN7u1hsSAGscBAAMCAANzAAMkBA", caption='''*Мы - интернет-магазин кроссовок CROSS MARKET!
Главное для нас – предоставить вам качественный товар с максимальным комфортом!
Мы экономим ваше время: вам не нужно никуда выходить из своего дома, утомительно ходить по магазинам, мучиться выбором – все товары представлены в удобном каталоге, а заказ делается буквально за пару кликов.

Наш Интернет-Магазин занимается продажей фирменных кроссовок с доставкой по всей России, доставка кроссовок осуществляется в день заказа либо на следующий день после оформления заказа. По России отправляем кроссовки наложенным платежом, срок доставки рассчитывается индивидуально.

В каталоге CROSS MARKET  предоставлено множество известных моделей на любой вкус. Вы можете купить у нас кроссовки разных расцветок: Черные, Красные, Белые, Синие, Розовые, Серые, Голубые и множество других цветов.
Большой выбор кроссовок в интернет-магазине CROSS MARKET привлекательные цены, быстрая доставка, скидки постоянным покупателям!*
''', reply_markup=start_kb, parse_mode="Markdown")


async def reviews(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, text='*Отзывы*', reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton('Посмотреть отзывы', callback_data='show_review'),
            InlineKeyboardButton('Оставить отзыв', callback_data='set_review')).add(call_start_btn), parse_mode="Markdown")


async def show_review(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await callback_query.message.delete()
    await shop_db.sql_read_review(callback_query)
    await bot.send_message(callback_query.message.chat.id, text='*Отзывы*', reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton('Посмотреть отзывы', callback_data='show_review'),
            InlineKeyboardButton('Оставить отзыв', callback_data='set_review')).add(call_start_btn), parse_mode="Markdown")


async def set_review(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await callback_query.message.delete()
    await bot.send_message(callback_query.message.chat.id, text='*Оставьте ваш отзыв*', parse_mode="Markdown")
    await Review.mess.set()


async def set_review_end(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mess'] = message.text
    await shop_db.sql_set_review(data['mess'])
    await bot.send_message(message.from_user.id, text='*Ваш отзыв успешно опубликован!*',
                           reply_markup=InlineKeyboardMarkup().add(
                                   InlineKeyboardButton('Посмотреть отзывы', callback_data='show_review'),
                                   InlineKeyboardButton('Оставить отзыв', callback_data='set_review')).add(call_start_btn),
                           parse_mode="Markdown")
    await state.finish()


async def menu(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await callback_query.message.delete()

    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, text='*Ассортимент товаров*', reply_markup=menu_kb,
                           parse_mode="Markdown")


async def menu_newbalance(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    await state.finish()
    await bot.answer_callback_query(callback_query.id)
    items = await shop_db.sql_read_newbalance()

    for ret in items:
        menu_newbalance_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(f'Купить за {ret[1]}₽', callback_data=f'buy {ret[0]}')).add(InlineKeyboardButton(f'Доступны размеры с {ret[3]} по {ret[4]}', callback_data=f'buy {ret[0]}'))
        await bot.send_photo(callback_query.message.chat.id, str(ret[2]),
                             caption=f'*{ret[0]}*', reply_markup=menu_newbalance_kb, parse_mode="Markdown")
        menu_newbalance_kb = InlineKeyboardMarkup()
    await bot.send_message(callback_query.message.chat.id, '*Перейти в основной раздел*',
                           reply_markup=InlineKeyboardMarkup().add(start_btn).add(call_start_btn),
                           parse_mode="Markdown")
    await Client_data.brand.set()
    async with state.proxy() as data:
        data['brand'] = 'NEWBALANCE'
    await Client_data.item.set()


async def menu_adidas(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    await state.finish()
    await bot.answer_callback_query(callback_query.id)
    items = await shop_db.sql_read_adidas()
    for ret in items:
        menu_adidas_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(f'Купить за {ret[1]}₽', callback_data=f'buy {ret[0]}')).add(InlineKeyboardButton(f'Доступны размеры с {ret[3]} по {ret[4]}', callback_data=f'buy {ret[0]}'))
        await bot.send_photo(callback_query.message.chat.id, str(ret[2]),
                             caption=f'*{ret[0]}*', reply_markup=menu_adidas_kb, parse_mode="Markdown")
        menu_adidas_kb = InlineKeyboardMarkup()
    await bot.send_message(callback_query.message.chat.id, '*Перейти в основной раздел*',
                           reply_markup=InlineKeyboardMarkup().add(start_btn).add(call_start_btn),
                           parse_mode="Markdown")
    await Client_data.brand.set()
    async with state.proxy() as data:
        data['brand'] = 'ADIDAS'
    await Client_data.item.set()


async def menu_nike(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    await state.finish()
    await bot.answer_callback_query(callback_query.id)
    items = await shop_db.sql_read_nike()
    for ret in items:
        menu_nike_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(f'Купить за {ret[1]}₽', callback_data=f'buy {ret[0]}')).add(InlineKeyboardButton(f'Доступны размеры с {ret[3]} по {ret[4]}', callback_data=f'buy {ret[0]}'))
        await bot.send_photo(callback_query.message.chat.id, str(ret[2]),
                             caption=f'*{ret[0]}*', reply_markup=menu_nike_kb, parse_mode="Markdown")
        menu_nike_kb = InlineKeyboardMarkup()
    await bot.send_message(callback_query.message.chat.id, '*Перейти в основной раздел*',
                           reply_markup=InlineKeyboardMarkup().add(start_btn).add(call_start_btn),
                           parse_mode="Markdown")
    await Client_data.brand.set()
    async with state.proxy() as data:
        data['brand'] = 'NIKE'
    await Client_data.item.set()


async def menu_converse(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    await state.finish()
    await bot.answer_callback_query(callback_query.id)
    items = await shop_db.sql_read_converse()
    for ret in items:
        menu_converse_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(f'Купить за {ret[1]}₽', callback_data=f'buy {ret[0]}')).add(InlineKeyboardButton(f'Доступны размеры с {ret[3]} по {ret[4]}', callback_data=f'buy {ret[0]}'))
        await bot.send_photo(callback_query.message.chat.id, str(ret[2]),
                             caption=f'*{ret[0]}*', reply_markup=menu_converse_kb, parse_mode="Markdown")
        menu_converse_kb = InlineKeyboardMarkup()
    await bot.send_message(callback_query.message.chat.id, '*Перейти в основной раздел*',
                           reply_markup=InlineKeyboardMarkup().add(start_btn).add(call_start_btn),
                           parse_mode="Markdown")
    await Client_data.brand.set()
    async with state.proxy() as data:
        data['brand'] = 'CONVERSE'
    await Client_data.item.set()


async def menu_vans(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    await state.finish()
    await bot.answer_callback_query(callback_query.id)
    items = await shop_db.sql_read_vans()
    for ret in items:
        menu_vans_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(f'Купить за {ret[1]}₽', callback_data=f'buy {ret[0]}')).add(InlineKeyboardButton(f'Доступны размеры с {ret[3]} по {ret[4]}', callback_data=f'buy {ret[0]}'))
        await bot.send_photo(callback_query.message.chat.id, str(ret[2]),
                             caption=f'*{ret[0]}*', reply_markup=menu_vans_kb, parse_mode="Markdown")
        menu_vans_kb = InlineKeyboardMarkup()
    await bot.send_message(callback_query.message.chat.id, '*Перейти в основной раздел*',
                           reply_markup=InlineKeyboardMarkup().add(start_btn).add(call_start_btn),
                           parse_mode="Markdown")
    await Client_data.brand.set()
    async with state.proxy() as data:
        data['brand'] = 'VANS'
    await Client_data.item.set()


async def buy_command(callback_query: types.CallbackQuery, state: FSMContext):
    item = callback_query.data.replace('buy ', '')
    async with state.proxy() as data:
        data['item'] = item
    await Client_data.size.set()

    size = InlineKeyboardMarkup()

    async with state.proxy() as data:

        if data['brand'] == 'NEWBALANCE':
            sizes = await shop_db.sql_read_newbalance_size(item)
            for ret in sizes:
                i = ret[3]
                while i != (ret[4] + 1):
                    size.insert(InlineKeyboardButton(f'''{i}''', callback_data=f'''size {i}'''))
                    i += 1

        elif data['brand'] == 'ADIDAS':
            sizes = await shop_db.sql_read_adidas_size(item)
            for ret in sizes:
                i = ret[3]
                while i != (ret[4] + 1):
                    size.insert(InlineKeyboardButton(f'''{i}''', callback_data=f'''size {i}'''))
                    i += 1

        elif data['brand'] == 'NIKE':
            sizes = await shop_db.sql_read_nike_size(item)
            for ret in sizes:
                i = ret[3]
                while i != (ret[4] + 1):
                    size.insert(InlineKeyboardButton(f'''{i}''', callback_data=f'''size {i}'''))
                    i += 1

        elif data['brand'] == 'CONVERSE':
            sizes = await shop_db.sql_read_converse_size(item)
            for ret in sizes:
                i = ret[3]
                while i != (ret[4] + 1):
                    size.insert(InlineKeyboardButton(f'''{i}''', callback_data=f'''size {i}'''))
                    i += 1

        elif data['brand'] == 'VANS':
            sizes = await shop_db.sql_read_vans_size(item)
            for ret in sizes:
                i = ret[3]
                while i != (ret[4] + 1):
                    size.insert(InlineKeyboardButton(f'''{i}''', callback_data=f'''size {i}'''))
                    i += 1

        size.add(start_btn)
        await bot.send_message(callback_query.message.chat.id, f"*Выберите ваш размер*",
                               parse_mode="Markdown", reply_markup=size)


async def buy_command_half(callback_query: types.CallbackQuery, state: FSMContext):
    choosed_size = callback_query.data.replace('size ', '')
    async with state.proxy() as data:
        data['size'] = choosed_size
    await Client_data.contacts.set()
    await bot.send_message(callback_query.message.chat.id, "*Введите ваше имя и номер телефона*", parse_mode="Markdown")


async def buy_command_end(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contacts'] = message.text
        data['name'] = message.from_user.first_name
        data['id'] = message.from_user.id
    text = f'''- {data['item']}, {data['size']} размер'''
    await bot.send_message(message.chat.id, text=f'''*{text}\nВаш заказ принят. В ближайшее время ожидайте пожалуйста звонок нашего менеджера для уточнения деталей.*''', reply_markup=menu_kb, parse_mode='Markdown')
    await bot.send_message(-1001735383790, text=f'''*Новый заказ\n{text}\nКонтактные данные: {data['contacts']}*''', parse_mode='Markdown')
    await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(admin_start, commands=['admin'])
    dp.register_callback_query_handler(call_command_start, lambda c: c.data == 'call_command_start', state='*')
    dp.register_callback_query_handler(call_admin_start, lambda c: c.data == 'call_admin_start', state='*')
    dp.register_callback_query_handler(about, lambda c: c.data == 'about')
    dp.register_callback_query_handler(reviews, lambda c: c.data == 'rep')
    dp.register_callback_query_handler(show_review, lambda c: c.data == 'show_review')
    dp.register_callback_query_handler(set_review, lambda c: c.data == 'set_review')
    dp.register_message_handler(set_review_end, state=Review.mess)
    dp.register_callback_query_handler(menu, lambda c: c.data == 'menu', state='*')
    dp.register_callback_query_handler(menu_newbalance, lambda c: c.data == 'newbalance', state='*')
    dp.register_callback_query_handler(menu_adidas, lambda c: c.data == 'adidas', state='*')
    dp.register_callback_query_handler(menu_nike, lambda c: c.data == 'nike', state='*')
    dp.register_callback_query_handler(menu_converse, lambda c: c.data == 'converse', state='*')
    dp.register_callback_query_handler(menu_vans, lambda c: c.data == 'vans', state='*')
    dp.register_callback_query_handler(buy_command, lambda c: c.data and c.data.startswith('buy '),
                                       state=Client_data.item)
    dp.register_callback_query_handler(buy_command_half, lambda c: c.data and c.data.startswith('size '),
                                       state=Client_data.size)
    dp.register_message_handler(buy_command_end, state=Client_data.contacts)
    dp.register_callback_query_handler(delete_review, lambda c: c.data and c.data.startswith('del '))
    dp.register_callback_query_handler(delete_review_menu, lambda c: c.data == 'delete_review')
    dp.register_callback_query_handler(add_item, lambda c: c.data and c.data.startswith('add_'))
    dp.register_callback_query_handler(add_item_brand, state=NewItem.brand)
    dp.register_message_handler(add_item_name, state=NewItem.name)
    dp.register_message_handler(add_item_price, state=NewItem.price)
    dp.register_message_handler(add_item_photo, state=NewItem.photo_id, content_types=['photo'])
    dp.register_message_handler(add_item_min_r, state=NewItem.min_r)
    dp.register_message_handler(add_item_max_r, state=NewItem.max_r)
    dp.register_callback_query_handler(del_item_start, lambda c: c.data == 'dele_items')
    dp.register_callback_query_handler(del_item_brand, lambda c: c.data and c.data.startswith('deleting_item_'),
                                       state=DelItem.brand)
    dp.register_callback_query_handler(del_item, lambda c: c.data and c.data.startswith('delete '), state=DelItem)
