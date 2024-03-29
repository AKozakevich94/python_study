from youtube_search import YoutubeSearch
import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import hashlib


def searcher(text):
    res = YoutubeSearch(text, max_results=10).to_dict()
    return res


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def start(message: types.Message):
    await message.answer('Не надо мне писать, это инлайн бот!')


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or 'echo'
    links = searcher(text)

    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(f'{link["id"]}'.encode()).hexdigest(),
        title=f'{link["title"]}',
        url=f'https://www.youtube.com/watch?v={link["id"]}',
        thumb_url=f'{link["thumbnails"][0]}',
        input_message_content=types.InputTextMessageContent(
            message_text=f'https://www.youtube.com/watch?v={link["id"]}')
    ) for link in links]

    await query.answer(articles, cache_time=60, is_personal=True)


executor.start_polling(dp, skip_updates=True)
