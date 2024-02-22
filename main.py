import asyncio
import logging

from aiogram.client.default import DefaultBotProperties

from config.settings import TOKEN

from aiogram import Bot, Dispatcher

from handlers import start_handler

logging.basicConfig(level=logging.INFO)


async def start():
    """Функция старта бота и его диспетчера"""
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    dp.include_routers(start_handler.router)

    try:
        await dp.start_polling(bot, skip_updates=True)
    except Exception as e:
        logging.exception(f'Ошибка во время пуллинга: {e}')
    finally:
        logging.info('Бот остановлен')


if __name__ == '__main__':
    asyncio.run(start())
