from vkbottle import *
from PIL import Image, ImageDraw, ImageFont
import sys
import json
import re

bot=Bot('32e0395facce5c1284e84ba0a17ff33d07b46d192516868fbc81d9f9962d10e36cdbb3a26c0cab931b08f')
group_id = 202725378
photo_uploader = PhotoUploader(bot.api, generate_attachment_strings=True)  # Создание объекта загрузчика

def reg( ans ):
    data = json.load( open( "data.json", "r" ) )
    if str( ans.from_id ) in data[ "user" ]:
       	pass
    else:
        data[ "user" ][ str( ans.from_id ) ] = "reg"
        data[ "name" ][ str( ans.from_id ) ] = "Пользователь"
        data[ "status" ][ str( ans.from_id ) ] = "Для того, чтобы добавить заметку, введите команду '/заметки {название}' и в следующей строке текст. Также можно создать заметку из пересылаемого сообщения."
        data[ "prava" ][ str( ans.from_id ) ] = 0
        data[ "pred" ][ str( ans.from_id ) ] = 0
        data[ "id" ][ str( ans.from_id ) ] = str( len( data[ "user" ] ) )
        json.dump( data, open( "data.json", "w" ) )

@bot.on.message_handler(text='Текст <name>')
async def photo(ans: Message, name):
    try:
        photo1 = Image.open("rectangle.png")
    except:
        await ans('Ошибка')
        sys.exit(1)
    
    idraw = ImageDraw.Draw(photo1)
    font = ImageFont.truetype("arial.ttf", size=52)
    idraw.text((400, 200), name, font=font)
    photo1.save('photo1_watermarked.png')
    photo = await photo_uploader.upload_message_photo('photo1_watermarked.png')
    await ans('Держите фото:', attachment=photo)

@bot.on.message_handler(text='текст <name>')
async def photo(ans: Message, name):
    try:
        photo1 = Image.open("rectangle.png")
    except:
        await ans('Ошибка')
        sys.exit(1)
    
    idraw = ImageDraw.Draw(photo1)
    font = ImageFont.truetype("arial.ttf", size=52)
    idraw.text((400, 200), name, font=font)
    photo1.save('photo1_watermarked.png')
    photo = await photo_uploader.upload_message_photo('photo1_watermarked.png')
    await ans('Держите фото:', attachment=photo)

@bot.on.message_handler(text='ладно')
async def wrapper(ans: Message):
    await ans('шиколадно')

@bot.on.message_handler(text='бот пошел нахуй')
async def wrapper(ans: Message):
    await ans('зач')

@bot.on.message_handler(text='/заметки <name>')
async def wrapper(ans: Message, name):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	await ans(f'теперь ваш статус: {name}')
	data["status"][str(ans.from_id)] = name
	json.dump( data, open( "data.json", "w" ) )

@bot.on.message_handler(text='заметки')
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	await ans(f"🗓 [id{ans.from_id}|{data['name'][str(ans.from_id)]}], Ваши заметки:\n\n💬 {data['status'][str(ans.from_id)]}")

@bot.on.message_handler(text='ник <name>')
async def wrapper(ans: Message, name):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	data["name"][str(ans.from_id)] = name
	await ans(f"ваш ник теперь - {name}")
	json.dump( data, open( "data.json", "w" ) )

@bot.on.message_handler(text='админ права')
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	list_admin = [i for i in await bot.api.messages.get_convetsation_members(chat_id = ans.chat_id) if i.is_admin]

	if ans.from_id in list_admin:
		if data["prava"] == 4:
			await ans("У вас уже есть админ права")
		else:
			await ans("Вы получили админ права!")

@bot.on.message_handler(text='кто я')
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	b = data[ 'prava' ][ str( ans.from_id ) ]
	await ans(f"Вы [id{ans.from_id}|{data['name'][str(ans.from_id)]}]:  \n\n1.Ранк: {b}")

@bot.on.message_handler(text='кик')
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	if data["prava"][str(ans.from_id)] == 4:
		await bot.api.messages.remove_chat_user(user_id = ans.reply_message.from_id, chat_id = ans.chat_id)
		await ans('Был исключен!')
	else:
		await ans('Нужно иметь 4 ранк!')

@bot.on.message_handler(text='Кик')
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	if data["prava"][str(ans.from_id)] == 4:
		await bot.api.messages.remove_chat_user(user_id = ans.reply_message.from_id, chat_id = ans.chat_id)
		await ans('Был исключен!')
	else:
		await ans('Нужно иметь 4 ранк!')

@bot.on.message_handler(text='.повысить')
async def wrapper(ans: Message):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	if data["prava"][str(ans.from_id)] == 4:
		data["prava"][str(ans.reply_message.from_id)] += 1
		await ans(f"Вы повысили {data['name'][str(ans.reply_message.from_id)]} до {data['prava'][str(ans.reply_message.from_id)]}!")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message_handler(text='пред')
async def wrapper(ans: Message):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	if data["prava"][str(ans.from_id)] == 4:
		data["pred"][str(ans.reply_message.from_id)] += 1
		await ans(f"Было выдано предупреждение [id{ans.reply_message.from_id}|человеку]")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message_handler(text='пред снять')
async def wrapper(ans: Message):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	if data["prava"][str(ans.from_id)] == 4:
		data["pred"][str(ans.reply_message.from_id)] -= 1
		await ans(f"Было убрано 1 предупреждение [id{ans.reply_message.from_id}|человеку], его предупреждения: {data['pred'][str(ans.reply_message.from_id)]}")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message_handler(text='<da>')
async def wrapper(ans: Message, da):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	if data["pred"][str(ans.from_id)] == 3:
		await ans("Больше 3 предупреждений")
		data["pred"][str(ans.from_id)] = 0
		await bot.api.messages.remove_chat_user(user_id = ans.from_id, chat_id = ans.chat_id)
	else:
		pass

@bot.on.message_handler(text='поцеловать')
async def wrapper(ans: Message, da):
	reg( ans )
	await ans(f"[id{ans.from_id}|{data['name'][str(ans.from_id)]}], поцеловал [id{ans.reply_message.from_id}|{data['name'][str(ans.from_id)]}]")
		  
@bot.on.message_handler(text='Поцеловать')
async def wrapper(ans: Message, da):
	reg( ans )
	await ans(f"[id{ans.from_id}|{data['name'][str(ans.from_id)]}], поцеловал [id{ans.reply_message.from_id}|{data['name'][str(ans.from_id)]}]")
			  
bot.run_polling()
             
              
