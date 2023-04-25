from aiogram import types
from utils import get_img_url
from loader import dp


@dp.message_handler()
async def send_dog(message: types.Message):
    img_url = await get_img_url()
    if img_url:
        await message.answer_photo(img_url)