import smtplib
from email.mime.text import MIMEText

from aiogram import types
from aiogram.dispatcher import FSMContext

from db_api import db_quick_commands as db_commands
from db_api.schemas.users import Users_model as users
from config import dp, bot, _
import keyboards as kb
import handlers.states as states
import callback.quick_callback


#######################################################################################################################################
from language_middleware import get_lang
from settings import session


async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer(_("Не флуди :) Одне повідомлення в секунду"))

#######################################################################################################################################




#######################################################################################################################################

@dp.message_handler(commands=["start"])
@dp.throttled(anti_flood, rate=1)
async def start_handler(message: types.Message):
    if message.chat.type == 'private':
        try:
            if (not await db_commands.select_user(message.from_user.id)):
                db_commands.register_user(message)
                await message.answer(_('🔝 <b>Головне Меню</b>'), parse_mode='html', reply_markup=kb.markup_start)
                await message.answer(_('🤔 Оберіть ваш варіант 💭'))
            else:
                await message.answer(_('🔝 <b>Головне Меню</b>'), parse_mode='html', reply_markup=kb.markup_start)
                await message.answer(_('🤔 Оберіть ваш варіант 💭'))
        except:
            await message.answer(_('❗ Бот розроблений для кожного особисто, не можна його добавляти в групи. Поспілкуйтесь з ним самі: @trx_games_bot\nЯкщо у вас виникли інші проблеми, звертайтесь до нашого менеджера: @Christooo1'))
    else:
        await message.answer(_('❗ Бот розроблений для кожного особисто, не можна його добавляти в групи. Поспілкуйтесь з ним самі: @trx_games_bot\nЯкщо у вас виникли інші проблеми, звертайтесь до нашого менеджера: @Christooo1'))

#######################################################################################################################################



#######################################################################################################################################

@dp.message_handler(content_types=['text'])
@dp.throttled(anti_flood, rate=1)
async def text_message(message: types.Message):
    ban_mod = await users.query.where(users.user_id == message.from_user.id).gino.first()
    ban = ban_mod.ban
    if ban == 0:
        if (message.text == "🆘 Тех. Підтримка") or (message.text == "🆘 Тех. Поддержка") or (message.text == "🆘 Support"):
            markup = types.InlineKeyboardMarkup(row_width=1)
            change_language = types.InlineKeyboardButton('🔄 \n\nПоміняти мову | Сменить язык | Change the language', callback_data="change_language")
            up_button = types.InlineKeyboardButton("📺 Зв'язатись із тех. підтримкою", url="https://t.me/Ch")
            markup.add(change_language, up_button)
            photo = open('img/what-is-bot-management.png', 'rb')
            await bot.send_photo(message.from_user.id, photo, caption='При будь-яких питаннях звертайтесь до нашого менеджера: ', reply_markup=markup, parse_mode='html')

#######################################################################################################################################


