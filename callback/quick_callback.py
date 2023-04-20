from aiogram import types
from db_api.schemas.users import Users_model as users

from config import dp, bot, _
import keyboards as kb
from settings import session


async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer('One mess per second, pls')


@dp.callback_query_handler()
@dp.throttled(anti_flood, rate=1)
async def callback_guess(call: types.callback_query):
    if call.data == 'change_language':
        await bot.send_message(call.message.chat.id, '🇺🇦 Оберіть мову інтерфейсу\n\n🇷🇺 Выберите язык интерфейса\n\n🇬🇧 Choose the interface language', reply_markup=kb.markup_change_language, parse_mode='html')
    if call.data == "ua_lang":
        await users.update.values(user_language='uk').where(users.user_id == call.message.chat.id).gino.status()
        session.commit()
        await bot.send_message(call.message.chat.id, '🇺🇦 Вітаю\n\nВи обрали українську мову\n\nМову можна міняти в будь-який момент у розділі "🆘 Тех. Підтримка"', reply_markup=kb.markup_start, parse_mode='html')
        await call.message.answer(_('🔝 <b>Головне Меню</b>', locale='uk'), parse_mode='html')
    if call.data == "ru_lang":
        await users.update.values(user_language='ru').where(users.user_id == call.message.chat.id).gino.status()
        session.commit()
        await bot.send_message(call.message.chat.id, '🇷🇺 Поздравляю\n\nУ вас русский язык интерфейса\n\nЯзык можно менять в любой момент в разделе "🆘 Тех. Поддержка"', reply_markup=kb.markup_start, parse_mode='html')
        await call.message.answer(_('🔝 <b>Головне Меню</b>', locale='ru'), parse_mode='html')
    if call.data == "en_lang":
        await users.update.values(user_language='en').where(users.user_id == call.message.chat.id).gino.status()
        session.commit()
        await bot.send_message(call.message.chat.id, '🇬🇧 Congratulations\n\n You have chosen English\n\n You can change the language at any time in the section "🆘 Support"', reply_markup=kb.markup_start, parse_mode='html')
        await call.message.answer(_('🔝 <b>Головне Меню</b>', locale='en'), parse_mode='html')
