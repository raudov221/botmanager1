from vkbottle.user import User, Message
from vkbottle import PhotoUploader
import random

blocked = ["porno365", "porno", "xnxx", "vto", "vto.pe", "ru", "com", "pe"]


user = User("7600dc5954d0b7a9bbaa1a928ad408372062a8e14c51975fd06bfeb18d183fa4f9c18eac38e8283930997", mobile = True)

@user.on.message_handler(text=".брак пошалить", lower = True)
async def wrapper(ans: Message):
	await ans(".брак принять")


user.run_polling()
