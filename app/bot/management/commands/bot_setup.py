# Django imports

from django.core.management import BaseCommand

# Aiogram imports
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# imports constants
from open_pycab.settings import TELEGRAM_TOKEN

async def main():

    # https://docs.aiogram.dev/en/latest/dispatcher/webhook.html#examples 
    # СМОТРИ СЮДА ШО ДЕЛАТЬ ИЩИ

    dp = Dispatcher()
    bot = Bot(TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
    print('start')
    await dp.start_polling(bot)
    print('finish')


class Command(BaseCommand):
    '''Django command '''

    def handle(self, *args, **options):
        ''' Just to start bot '''
        asyncio.run(main())
