from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from config.settings import ADMIN_ID
from utils.database_manager import DatabaseManager

router = Router()


@router.startup()
async def start_bot(bot: Bot):
    """Хэндлер об успешном запуске бота."""
    await bot.send_message(ADMIN_ID, text='🤖 Бот успешно запущен! 🚀')


@router.message(Command('start'))
async def get_start(message: Message, bot: Bot):
    """Хэндлер приветствующий пользователя при команде /start."""
    db = DatabaseManager()
    tg_user_id = message.from_user.id
    tg_username = message.from_user.username

    user = db.select_user(tg_user_id)

    if user:
        await bot.send_message(
            message.from_user.id,
            f'Здравствуй {user[1]}! 👋',
            reply_markup=None
        )
    else:
        await bot.send_message(
            message.from_user.id,
            f'Здравствуй {tg_username}! 👋',
            reply_markup=None
        )