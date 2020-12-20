from vkbottle import Bot, Message, Mailing
bot = Bot('e0273154fd1767633850be5e8758a640188af6147a90eb5b95105050f863707a48d9837974e3787b2140e', group_id, debug=True)

@bot.on.message('/mail <text>')
async def mail(ans: Message, text):
  m = mailing([api_82735_N1cGUGYqt2f3oPL5YHFoLSSM]) # ID бери из настроек приложения
  m(text)
  await ans('Рассылка началась!')
  a = await m.run_now()

bot.run_polling()
