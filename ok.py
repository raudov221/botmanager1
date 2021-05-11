from vkbottle.user import User, Message
from vkbottle import PhotoUploader
import random

blocked = ["porno365", "porno", "xnxx", "vto", "vto.pe", "ru", "com", "pe"]


user = User("d8ecd8cb345c80a0a2dc573293763baee965fdba2b97e7e3dd107b8d5f786016e3b97e6f09f364ccad65a", mobile = True)

@user.on.message_handler(text=".брак пошалить", lower = True)
async def wrapper(ans: Message):
	if ans.from_id == "597825377":
		await ans("@grizzlybot ✅ Принять")


user.run_polling()
