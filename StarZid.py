#!/usr/bin/python
# -*- coding: utf-8 -*-
#import telebot
#from telebot import types
import random
import json
import pickle
import asyncio
from time import sleep
# from loguru import logger
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import textwrap
import os
import sys
#from pythonping import ping
from textwrap import wrap
from random import randint, choice
from requests import get
from io import BytesIO
import colorama
from colorama import Fore, Back
nex_id=986023905
drax_id=994434215
crab_id=5101138428
just_id=831781432
support_id=919644121
version = "1.3 "
#bot = telebot.TeleBot('5319579657:AAHyJBAX4H-LW50hEtVvdtPtmnHwevPOaJs')
#mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
tag = "<b>⭐️ @starzedscripts </b>"
tager = "<b> ⭐️ @starzedscripts </b>"
a = ["Разработчик", "Администратор", "DEVELOPER",]

def format_exc(e: Exception, hint: str = None):
    traceback.print_exc()
    if isinstance(e, errors.RPCError):
        return (
            f"<b>Telegram API error!</b>\n"
            f"<code>[{e.CODE} {e.ID or e.NAME}] - {e.MESSAGE}</code>"
        )
    else:
        if hint:
            hint_text = f"\n\n<b>Hint: {hint}</b>"
        else:
            hint_text = ""
        return (
            f"<b>Error!</b>\n" f"<code>{e.__class__.__name__}: {e}</code>" + hint_text
        )


def with_reply(func):
    async def wrapped(client, message: types.Message):
        if not message.reply_to_message:
            await message.edit("<b>Reply to message is required</b>")
        else:
            return await func(client, message)

    return wrapped

if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
#okda = ping('8.8.8.8', size=40, count=10)
#print(Fore.GREEN +  "PING:" + str(okda.rtt_avg_ms))
# print(Fore.LIGHTRED_EX + f'Пользуясь ботом, вы автоматически принимаете {Fore.RED}"Пользовательское соглашение"{Fore.WHITE}\n --Введите свои данные--{Fore.LIGHTBLACK_EX}\n 1) Номер телефона.\n 2) Ввод буквы Y для подтверждения номера.\n 3) Код, который пришел в telegram.\n 4) Пароль для двухэтапной авторизации, если вы его установили. \n\n{Fore.YELLOW}')
print(Fore.LIGHTYELLOW_EX + f'''

                                                                  
  Пользуясь ботом вы автоматически принимаете и соглашаетесь со     
  всеми правилами пользовательского соглашения.                     
                                                                    
  {Fore.LIGHTRED_EX} Если вы запускаете бота в первый раз выполните 
   следующие действия:                                              
                                                                    
     1)  Введите номер телефона                                     
     2)  Введите букву {Fore.RED}Y{Fore.LIGHTRED_EX}                
     3)  Введите код который пришел в Telegram                      
     4)  Введите пароль для двухэтапной авторизации, если он есть.                                                                
                                                                     
    {Fore.YELLOW}''')
sleep(3)


m = '''
████████
██
██
██████
██
██
██'''

h = "╔┓┏╦━━╦┓╔┓╔━━╗ \n║┗┛║┗━╣┃║┃║╯╰║ \n║┏┓║┏━╣┗╣┗╣╰╯║ \n╚┛┗╩━━╩━╩━╩━━╝"



fuckk = '''
╱▔▔▔╲┈┈┈┈┈╱▔▔▔╲
▏╰┈╮┈╲╲┈╱╱┈╭┈╯▕
╲╮┈╰┈╮╲▉╱╭┈╯┈╭╱
▕╰┈╮┈╰╮▉╭╯┈╭┈╯▏
┈╲▂╰┈┈╱▉╲┈┈╯▂╱
┈┈╱▔▔▔╭▊╮▔▔▔╲
┈┈▏╭┈┈╯▊╰┈┈╮▕
┈▕╭╯┈┈╱▋╲┈┈╰╮▏
┈┈╲▂▂╱┈┈┈╲▂▂╱
'''

d = ''' 
████╗███╗█╗█╗
█╔══╝█╔█║█║█║
████╗███║███║
█╔═█║█╔█║█╔█║
████║█║█║█║█║
╚═══╝╚╝╚╝╚╝╚╝'''


app = Client('StarZed', lang_code="ru", api_id=15897262, api_hash='90476d9c65a86b03837e1e249314cd75')


app.start()

app.stop()
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
sleep(1)
print(Fore.LIGHTCYAN_EX + f''' 

  ---{Fore.LIGHTCYAN_EX}███{Fore.CYAN}██████████████████████{Fore.LIGHTCYAN_EX}
  ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTCYAN_EX}
  ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTCYAN_EX}
 {Fore.LIGHTCYAN_EX} ████{Fore.LIGHTCYAN_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤  ││┃█{Fore.LIGHTCYAN_EX}
 {Fore.LIGHTCYAN_EX} █{Fore.LIGHTCYAN_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTCYAN_EX}                     
  {Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┊Version: 1.3            ┃█{Fore.LIGHTCYAN_EX} 
  {Fore.CYAN}█{Fore.LIGHTCYAN_EX}┊Telegram: starzedscripts┃█{Fore.LIGHTCYAN_EX} 
 {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTCYAN_EX}
 {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTCYAN_EX}
  {Fore.CYAN}██████████████████{Fore.LIGHTCYAN_EX}█---------
                

''')
sleep(0.05)
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
print(Fore.LIGHTCYAN_EX + f''' 

   ---{Fore.LIGHTCYAN_EX}███{Fore.CYAN}██████████████████████{Fore.LIGHTCYAN_EX}
   ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTCYAN_EX}
   ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTCYAN_EX}
  {Fore.LIGHTCYAN_EX} ████{Fore.LIGHTCYAN_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤  ││┃█{Fore.LIGHTCYAN_EX}
  {Fore.LIGHTCYAN_EX} █{Fore.LIGHTCYAN_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTCYAN_EX}                     
   {Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┊Version: 1.3            ┃█{Fore.LIGHTCYAN_EX} 
   {Fore.CYAN}█{Fore.LIGHTCYAN_EX}┊Telegram: starzedscripts┃█{Fore.LIGHTCYAN_EX} 
  {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTCYAN_EX}
  {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTCYAN_EX}
   {Fore.CYAN}██████████████████{Fore.LIGHTCYAN_EX}█---------
                

''')
sleep(0.05)
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
print(Fore.LIGHTCYAN_EX + f''' 

     ---{Fore.LIGHTCYAN_EX}███{Fore.CYAN}██████████████████████{Fore.LIGHTCYAN_EX}
     ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTCYAN_EX}
     ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTCYAN_EX}
    {Fore.LIGHTCYAN_EX} ████{Fore.LIGHTCYAN_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤  ││┃█{Fore.LIGHTCYAN_EX}
    {Fore.LIGHTCYAN_EX} █{Fore.LIGHTCYAN_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTCYAN_EX}                     
     {Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┊Version: 1.3            ┃█{Fore.LIGHTCYAN_EX} 
     {Fore.CYAN}█{Fore.LIGHTCYAN_EX}┊Telegram: starzedscripts┃█{Fore.LIGHTCYAN_EX} 
    {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTCYAN_EX}
    {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTCYAN_EX}
     {Fore.CYAN}██████████████████{Fore.LIGHTCYAN_EX}█---------
                

''')
sleep(0.05)
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
print(Fore.LIGHTCYAN_EX + f''' 

      ---{Fore.LIGHTCYAN_EX}███{Fore.CYAN}██████████████████████{Fore.LIGHTCYAN_EX}
      ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTCYAN_EX}
      ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTCYAN_EX}
     {Fore.LIGHTCYAN_EX} ████{Fore.LIGHTCYAN_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤  ││┃█{Fore.LIGHTCYAN_EX}
     {Fore.LIGHTCYAN_EX} █{Fore.LIGHTCYAN_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTCYAN_EX}                     
      {Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┊Version: 1.3            ┃█{Fore.LIGHTCYAN_EX} 
      {Fore.CYAN}█{Fore.LIGHTCYAN_EX}┊Telegram: starzedscripts┃█{Fore.LIGHTCYAN_EX} 
     {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTCYAN_EX}
     {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTCYAN_EX}
      {Fore.CYAN}██████████████████{Fore.LIGHTCYAN_EX}█---------
                

''')
sleep(0.05)
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
print(Fore.LIGHTCYAN_EX + f''' 

        ---{Fore.LIGHTCYAN_EX}███{Fore.CYAN}██████████████████████{Fore.LIGHTCYAN_EX}
        ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTCYAN_EX}
        ---{Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTCYAN_EX}
       {Fore.LIGHTCYAN_EX} ████{Fore.LIGHTCYAN_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤  ││┃█{Fore.LIGHTCYAN_EX}
       {Fore.LIGHTCYAN_EX} █{Fore.LIGHTCYAN_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTCYAN_EX}                     
        {Fore.LIGHTCYAN_EX}█{Fore.LIGHTCYAN_EX}┊Version: 1.3            ┃█{Fore.LIGHTCYAN_EX} 
        {Fore.CYAN}█{Fore.LIGHTCYAN_EX}┊Telegram: starzedscripts┃█{Fore.LIGHTCYAN_EX} 
       {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTCYAN_EX}
       {Fore.CYAN} █{Fore.LIGHTCYAN_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTCYAN_EX}
        {Fore.CYAN}██████████████████{Fore.LIGHTCYAN_EX}█---------
                

''')
sleep(0.05)
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
print(Fore.LIGHTYELLOW_EX + f''' 

        ---{Fore.LIGHTYELLOW_EX}███{Fore.YELLOW}██████████████████████{Fore.LIGHTYELLOW_EX}
        ---{Fore.LIGHTYELLOW_EX}█{Fore.LIGHTYELLOW_EX}┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑█{Fore.LIGHTYELLOW_EX}
        ---{Fore.LIGHTYELLOW_EX}█{Fore.LIGHTYELLOW_EX}┃╔═╗┌┬┐┌─┐┬─┐╔═╗┌─┐┌┬┐┃█{Fore.LIGHTYELLOW_EX}
       {Fore.LIGHTYELLOW_EX} ████{Fore.LIGHTYELLOW_EX}┃╚═╗ │ ├─┤├┬┘╔═╝├┤  ││┃█{Fore.LIGHTYELLOW_EX}
       {Fore.LIGHTYELLOW_EX} █{Fore.LIGHTYELLOW_EX}┏┅┅┛╚═╝ ┴ ┴ ┴┴└─╚═╝└─┘─┴┘┃█{Fore.LIGHTYELLOW_EX}                     
        {Fore.LIGHTYELLOW_EX}█{Fore.LIGHTYELLOW_EX}┊Version: 1.3            ┃█{Fore.LIGHTYELLOW_EX} 
        {Fore.YELLOW}█{Fore.LIGHTYELLOW_EX}┊Telegram: starzedscripts┃█{Fore.LIGHTYELLOW_EX} 
       {Fore.YELLOW} █{Fore.LIGHTYELLOW_EX}┊Made by Criblle┎━━━━━━━━┛█{Fore.LIGHTYELLOW_EX}
       {Fore.YELLOW} █{Fore.LIGHTYELLOW_EX}┗━━━━━━━━━━━━━━━┛██████████{Fore.LIGHTYELLOW_EX}
        {Fore.YELLOW}██████████████████{Fore.LIGHTYELLOW_EX}█---------
                

''')

print(Fore.LIGHTYELLOW_EX + f"  После ввода задержки напишите в любой telegram чат команду {Fore.YELLOW}/help{Fore.LIGHTYELLOW_EX} для просмотра команд!")
print(Fore.LIGHTYELLOW_EX + f"\n ► {Fore.YELLOW}МЫ {Fore.LIGHTYELLOW_EX}НЕ{Fore.YELLOW} Н{Fore.LIGHTYELLOW_EX}ЕС{Fore.YELLOW}ЕМ{Fore.LIGHTYELLOW_EX} О{Fore.YELLOW}ТВ{Fore.LIGHTYELLOW_EX}ЕТ{Fore.YELLOW}СВ{Fore.LIGHTYELLOW_EX}ЕН{Fore.YELLOW}НО{Fore.LIGHTYELLOW_EX}СТ{Fore.YELLOW}И З{Fore.LIGHTYELLOW_EX}А ВА{Fore.YELLOW}ШИ ДЕ{Fore.LIGHTYELLOW_EX}ЙС{Fore.YELLOW}ТВ{Fore.LIGHTYELLOW_EX}ИЯ! ◄ ")
print()
cool = int(input(Fore.WHITE + f" <$> Введите завис.скорость:{Fore.LIGHTBLACK_EX} "))
print(Fore.LIGHTCYAN_EX + f" \n Вернитесь в Telegram и введите /help для просмотра команд! \n")
#bot.send_message(-733171711, f"<b> 💫  Пользователь запустил скрипт!</b>")

global number
number = 0

while cool == 0:
    print("Слишком быстро!")
    cool = int(input(" <$> Введите завис.скорость: "))

while cool == 1:
    print("Слишком быстро!")
    cool = int(input(" <$> Введите завис.скорость: "))

while cool == 2:
    print("Слишком быстро!")
    cool = int(input(" <$> Введите завис.скорость: "))

while cool > 10:
    print("Слишком медленно!")
    cool = int(input(" <$> Введите завис.скорость: "))

while cool < 0:
    print("ОЧЕНЬ БЫСТРО........")
    cool = int(input(" <$> Введите завис.скорость: "))

# with open('Prefix.txt', 'w') as f:
#     f.write(str("prefix"))
#     f.close()


@app.on_message(filters.command("bombs", prefixes = ".") & filters.me)
async def bombs(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .bombs')
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    global number
    number = number + 1
    await message.edit_text(tag)

#with app:
   # app.join_chat("starzedscripts")
    #app.join_chat("starzedscripts_chat")



#symbols = ['1', '*', '3', '2', '&', '#', '@', '$', '%', '^', '+', '-', '?', '№', ';', '"']




@app.on_message(filters.command("snow", prefixes=".") & filters.me)
async def betaloves(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .snow')
    global number
    number = number + 1
    await message.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️





⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await message.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    





⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await message.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️




⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await message.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️



⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await message.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️
❄️     ❄️    ❄️     ❄️    ❄️


⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await message.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️
❄️     ❄️    ❄️     ❄️    ❄️    
    ❄️     ❄️    ❄️     ❄️

⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await message.edit(tag)



@app.on_message(filters.command("hello", prefixes=".") & filters.me)
async def betaloves(app ,message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .hello')
    global number
    number = number + 1
    current = ""
    for chunk in list(h):
        current += chunk
        if not chunk.strip():
            continue
        await message.edit(current)
        await asyncio.sleep(.25)
    await asyncio.sleep(2)
    await message.edit(tag)


russia = '''


⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥

'''

steve = '''


🏿🏿🏿🏿🏿🏿🏿🏿
🏿🏿🏽🏽🏽🏽🏿🏿
🏽🏽🏽🏽🏽🏽🏽🏽
🏽⬜️⬛️🏽🏽⬛️⬜️🏽
🏽🏽🏽🏿🏿🏽🏽🏽
🏽🏽🏿🏽🏽🏿🏽🏽
🏽🏽🏿🏿🏿🏿🏽🏽

'''

ykraine = '''


🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦
🟨🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨


'''

@app.on_message(filters.command("germany", prefixes=".") & filters.me)
async def betaloves(app ,message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .ukraine')
    global number
    number = number + 1
    current = ""
    for chunk in list(germany):
        current += chunk
        if not chunk.strip():
            continue
        await message.edit(current)
        await asyncio.sleep(.10)
    await asyncio.sleep(3)
    await message.edit(tag)

@app.on_message(filters.command("ukraine", prefixes=".") & filters.me)
async def betaloves(app ,message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .ukraine')
    global number
    number = number + 1
    current = ""
    for chunk in list(ykraine):
        current += chunk
        if not chunk.strip():
            continue
        await message.edit(current)
        await asyncio.sleep(.10)
    await asyncio.sleep(3)
    await message.edit(tag)

@app.on_message(filters.command("steve", prefixes=".") & filters.me)
async def betaloves(app ,message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .steve')
    global number
    number = number + 1
    current = ""
    for chunk in list(steve):
        current += chunk
        if not chunk.strip():
            continue
        await message.edit(current)
        await asyncio.sleep(.10)
    await asyncio.sleep(3)
    await message.edit(tag)

@app.on_message(filters.command("russia", prefixes=".") & filters.me)
async def betaloves(app ,message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .russia')
    global number
    number = number + 1
    current = ""
    for chunk in list(russia):
        current += chunk
        if not chunk.strip():
            continue
        await message.edit(current)
        await asyncio.sleep(.10)
    await asyncio.sleep(3)
    await message.edit(tag)

@app.on_message(filters.command("F", prefixes=".") & filters.me)
async def betaloves(app ,message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .F')
    global number
    number = number + 1
    current = ""
    for chunk in list(m):
        current += chunk
        if not chunk.strip():
            continue
        await message.edit(current)
        await asyncio.sleep(.25)
    await asyncio.sleep(2)
    await message.edit(tag)

@app.on_message(filters.command("ban", prefixes=".") & filters.me)
async def betaloves(app ,message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .ban')
    global number
    number = number + 1
    current = ""
    for chunk in list(d):
        current += chunk
        if not chunk.strip():
            continue
        await message.edit(current)
        await asyncio.sleep(.15)
    await asyncio.sleep(2)
    await message.edit(tag)

@app.on_message(filters.command("bf", prefixes=".") & filters.me)
async def betaloves(app ,message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .bf')
    global number
    number = number + 1
    current = ""
    for chunk in list(fuckk):
        current += chunk
        if not chunk.strip():
            continue
        await message.edit(current)
        await asyncio.sleep(.10)
    await asyncio.sleep(2)
    await message.edit(tag)

@app.on_message(filters.command("timer", prefixes=".") & filters.me)
async def timer(_,message):
    try:
        score = int(message.text.split()[1])

        #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .timer на {score} секнуд')
        global number
        number = number + 1
        while score > 0:
            score -=1
            await message.edit(f'''<b>{score}</b>''')
            await asyncio.sleep(1)
        await message.edit(tag)
    except IndexError:
        await message.edit("<b>Вы забыли указать число.\nПример:</b><code>.timer 30</code>")
  

@app.on_message(filters.command("spamstick", prefixes=".") & filters.me)
def spam(app, message):
    global number
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил спам стикерами!')
    number = number + 1
    try:
        stick_id = str(message.text.split()[2])
        for _ in range(int(message.command[1])):
            sleep(0.01)
            app.send_sticker(message.chat.id, stick_id)
    except IndexError:
        message.edit("<b>Вы не ввели ID стикера!!\nПример:</b><code>.spamstick 5 CAACAgIAAxkBAAEEEDZiI8ZlrkTWVAVlsaJ1yfd63euS2AACMgwAAgqBoEs52ePcv8NaIiME</code>")


@app.on_message(filters.command("prefix", prefixes=".") & filters.me)
async def prefix(_,message):
    try:
        global prefix
        prefix = str(message.text.split()[1])
        prefix = prefix
        await message.edit("<b>Префикс установлен!</b>") 
        #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .timer на {score} секнуд')
    except IndexError:
        await message.edit("<b>Вы забыли указать префикс\nПример:</b><code>.prefix StarЗед</code>")

prefix = "Отсутствует"   



@app.on_message(filters.command("restart", prefixes = ".") & filters.me)
async def bombs(app, message):
    print(Fore.RED + "\n Restart...")
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .bombs')
    await asyncio.sleep(1)
    await message.edit_text("<b>Перезагрузка\n Это сообщение удалится через: 5</b>")
    await asyncio.sleep(1)
    await message.edit_text("<b>Перезагрузка\n Это сообщение удалится через: 4</b>")
    await asyncio.sleep(1)
    await message.edit_text("<b>Перезагрузка\n Это сообщение удалится через: 3</b>")
    await asyncio.sleep(1)
    await message.edit_text("<b>Перезагрузка\n Это сообщение удалится через: 2</b>")
    await asyncio.sleep(1)
    await message.edit_text("<b>Перезагрузка\n Это сообщение удалится через: 1</b>")
    await asyncio.sleep(0.2)
    await message.delete()
    os.execl(sys.executable, sys.executable, *sys.argv)
  

@app.on_message(filters.command("msgclear", prefixes = ".") & filters.me)
async def clearchat(app_, msg):
    await msg.edit_text("<b> Очистка сообщений! </b>")
    await asyncio.sleep(3)

    async for x in app_.iter_history(msg.chat.id, limit=1, reverse=True):
          first = x.message_id

    chunk = 100

    ids = range(first, msg.message_id)

    for _ in (ids[i:i+chunk] for i in range(0, len(ids), chunk)):
        try:
            asyncio.create_task(app_.delete_messages(msg.chat.id, _))
        except:
            pass
    await msg.edit_text("<b> Очистка сообщений завершена! </b>")
    await asyncio.sleep(3)
    await msg.delete()


@app.on_message(filters.command('stupid', prefixes='.') & filters.me)
async def ment(app, message):
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n🧠         (^_^)🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n🧠       (^_^)  🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n🧠     (^_^)    🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n🧠    (^_^)     🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n🧠   (^_^)      🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n🧠  (^_^)       🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n🧠< (^_^ <)         🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n(> ^_^)>🧠         🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n (> ^_^)>🧠       🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n  (> ^_^)>🧠     🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n   (> ^_^)>🧠   🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n    (> ^_^)>🧠 🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n     (> ^_^)>🧠🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n    (> ^_^)>🧠🗑')
    sleep(1)
    await message.edit(f'YOUR BRAIN ➡️ 🧠\n\n    (> ^_^)>🗑')
    sleep(3)
    await message.edit(tag)


@app.on_message(filters.command("spamreaction", prefixes=".") & filters.me)
def spam(app, message):
    global number
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил спам стикерами!')
    number = number + 1
    try:
        score = int(message.text.split()[1])
        reaction = str(message.text.split()[2])
        h = app.get_history(chat_id=message.chat.id, limit=score) # получаем историю сообщений (первые 100)
        for x in h:
            x = x.message_id # достаем ид сообщения
            app.send_reaction(message_id=x, chat_id=message.chat.id, emoji=reaction) # ставим реакцию (в эмодзи указать смайлик доступный в тг)
    except IndexError:
        message.edit("<b>Вы не ввели реакцию или количество повторов!\nПример:</b> <code>.spamreaction 10 🔥</code>")

# call = []
# chat = -1001744117594

# with app:
#     h = app.get_history(chat_id=chat, limit=100) # получаем историю сообщений (первые 100)
#     for x in h: # идем по списку
#       #  y = x.from_user.id
#         x = x.message_id # достаем ид сообщения
#         #if y in call: можно добавить проверку на определенного человека/людей
#         app.send_reaction(message_id=x, chat_id=chat, emoji="🔥") # ставим реакцию (в эмодзи указать смайлик доступный в тг)
#         logger.info(x)

@app.on_message(filters.command('vip', prefixes='.') & filters.me)
async def ment(app, message):
    await message.edit(f'❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️')
    sleep(1)
    await message.edit(f'❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️❇️❇️✴️❇️❇️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️')
    sleep(1)
    await message.edit(f'❇️❇️❇️❇️❇️❇️❇️\n❇️✴️❇️❇️❇️✴️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️❇️❇️✴️❇️❇️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️✴️❇️❇️❇️✴️❇️\n❇️❇️❇️❇️❇️❇️❇️')
    sleep(1)
    await message.edit(f'✴️❇️❇️❇️❇️❇️✴️\n❇️✴️❇️❇️❇️✴️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️❇️❇️✴️❇️❇️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️✴️❇️❇️❇️✴️❇️\n✴️❇️❇️❇️❇️❇️✴️')
    sleep(1)
    await message.edit(f'✴️❇️❇️❇️❇️❇️✴️\n❇️✴️❇️❇️❇️✴️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️✴️❇️❇️❇️✴️❇️\n✴️❇️❇️❇️❇️❇️✴️')
    sleep(1)
    await message.edit(f'✴️❇️❇️❇️❇️❇️✴️\n❇️✴️❇️❇️❇️✴️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️✴️❇️❇️❇️✴️❇️\n✴️❇️❇️❇️❇️❇️✴️')
    sleep(1)
    await message.edit(f'✴️❇️❇️❇️❇️❇️✴️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n✴️❇️❇️❇️❇️❇️✴️')
    sleep(1)
    await message.edit(f'✴️❇️❇️❇️❇️✴️✴️\n✴️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️✴️\n✴️✴️❇️❇️❇️❇️✴️')
    sleep(1)
    await message.edit(f'✴️❇️❇️❇️✴️✴️✴️\n✴️❇️❇️❇️❇️❇️❇️\n✴️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️✴️\n❇️❇️❇️❇️❇️❇️✴️\n✴️✴️✴️❇️❇️❇️✴️')
    sleep(1)
    await message.edit(f'✴️❇️❇️✴️✴️✴️✴️\n✴️❇️❇️❇️❇️❇️❇️\n✴️❇️❇️❇️❇️❇️❇️\n✴️❇️❇️❇️❇️❇️✴️\n❇️❇️❇️❇️❇️❇️✴️\n❇️❇️❇️❇️❇️❇️✴️\n✴️✴️✴️✴️❇️❇️✴️')
    sleep(1)
    await message.edit(f'✴️❇️✴️✴️✴️✴️✴️\n✴️❇️❇️❇️❇️❇️❇️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n❇️❇️❇️❇️❇️❇️✴️\n✴️✴️✴️✴️✴️❇️✴️')
    sleep(1)
    await message.edit(f'✴️✴️✴️✴️✴️✴️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️✴️✴️✴️✴️✴️✴️')
    sleep(1)
    await message.edit(f'✴️✴️✴️✴️✴️✴️✴️\n✴️👑👑👑👑👑✴️\n✴️👑❇️❇️❇️👑✴️\n✴️👑❇️❇️❇️👑✴️\n✴️👑❇️❇️❇️👑✴️\n✴️👑👑👑👑👑✴️\n✴️✴️✴️✴️✴️✴️✴️')
    sleep(1)
    await message.edit(f'✴️✴️✴️✴️✴️✴️✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑❇️👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️✴️✴️✴️✴️✴️✴️')
    sleep(1)
    await message.edit(f'✴️✴️✴️✴️✴️✴️✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑💍👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️✴️✴️✴️✴️✴️✴️')
    sleep(1)
    await message.edit(f'✴️✴️✴️✴️✴️✴️✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑🟠👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️✴️✴️✴️✴️✴️✴️')
    sleep(1)
    await message.edit(f'✴️✴️✴️✴️✴️✴️✴️\n✴️👑👑👑👑👑✴️\n✴️👑🟠🟠🟠👑✴️\n✴️👑🟠🟠🟠👑✴️\n✴️👑🟠🟠🟠👑✴️\n✴️👑👑👑👑👑✴️\n✴️✴️✴️✴️✴️✴️✴️')
    sleep(1)
    await message.edit(f'✴️✴️✴️✴️✴️✴️✴️\n✴️🟠🟠🟠🟠🟠✴️\n✴️🟠🟠🟠🟠🟠✴️\n✴️🟠🟠🟠🟠🟠✴️\n✴️🟠🟠🟠🟠🟠✴️\n✴️🟠🟠🟠🟠🟠✴️\n✴️✴️✴️✴️✴️✴️✴️')
    sleep(1)
    await message.edit(f'🟠🟠🟠🟠🟠\n🟠🟠🟠🟠🟠\n🟠🟠🟠🟠🟠\n🟠🟠🟠🟠🟠\n🟠🟠🟠🟠🟠')
    sleep(1)
    await message.edit(f'🟠🟠🟠\n🟠🟠🟠\n🟠🟠🟠')
    sleep(1)
    await message.edit(f'🟠')
    sleep(3)
    await message.edit(tag)


#@app.on_message(filters.command("amogus", prefixes=".") & filters.me)
#async def amogus(app, message):
 #   global number
  #  number = number + 1
   # clrs = {'red': 1, 'lime': 2, 'green': 3, 'blue': 4, 'cyan': 5, 'brown': 6, 'purple': 7, 'pink': 8, 'orange': 9, 'yellow': 10, 'white': 11, 'black': 12}
    #clr = randint(1,12)
    #text = " ".join(message.command[1:])

    #await message.edit("<b>amgus, tun tun tun tun tun tun tun tudududn tun tun...</b>")
    #url = "https://raw.githubusercontent.com/KeyZenD/AmongUs/master/"
    #font = ImageFont.truetype(BytesIO(get(url+"bold.ttf").content), 60)
    #imposter = Image.open(BytesIO(get(f"{url}{clr}.png").content))
    #text_ = "\n".join(["\n".join(wrap(part, 30)) for part in text.split("\n")])
    #w, h = ImageDraw.Draw(Image.new("RGB", (1,1))).multiline_textsize(text_, font, stroke_width=2)
    #text = Image.new("RGBA", (w+30, h+30))
    #ImageDraw.Draw(text).multiline_text((15,15), text_, "#FFF", font, stroke_width=2, stroke_fill="#000")
    #w = imposter.width + text.width + 10
    #h = max(imposter.height, text.height)
    #image = Image.new("RGBA", (w, h))
    #image.paste(imposter, (0, h-imposter.height), imposter)
    #image.paste(text, (w-text.width, 0), text)
    #image.thumbnail((512, 512))
    #output = BytesIO()
    #output.name = "imposter.webp"
    #image.save(output)
    #output.seek(0)
    #await message.delete()
    #await app.send_sticker(message.chat.id, output)

def format_exc(e: Exception, hint: str = None):
    traceback.print_exc()
    if isinstance(e, errors.RPCError):
        return (
            f"<b>Telegram API error!</b>\n"
            f"<code>[{e.CODE} {e.ID or e.NAME}] - {e.MESSAGE}</code>"
        )
    else:
        if hint:
            hint_text = f"\n\n<b>Hint: {hint}</b>"
        else:
            hint_text = ""
        return (
            f"<b>Error!</b>\n" f"<code>{e.__class__.__name__}: {e}</code>" + hint_text
        )


def with_reply(func):
    async def wrapped(client, message: types.Message):
        if not message.reply_to_message:
            await message.edit("<b>Reply to message is required</b>")
        else:
            return await func(client, message)

    return wrapped




R = "❤️"
W = "🤍"

heart_list = [
    W * 9,
    W * 2 + R * 2 + W + R * 2 + W * 2,
    W + R * 7 + W,
    W + R * 7 + W,
    W + R * 7 + W,
    W * 2 + R * 5 + W * 2,
    W * 3 + R * 3 + W * 3,
    W * 4 + R + W * 4,
    W * 9,
]
joined_heart = "\n".join(heart_list)
heartlet_len = joined_heart.count(R)
SLEEP = 0.1


async def _wrap_edit(message, text: str):
    """Floodwait-safe utility wrapper for edit"""
    try:
        await message.edit(text)
    except FloodWait as fl:
        await asyncio.sleep(fl.x)


async def phase1(message):
    """Big scroll"""
    BIG_SCROLL = "🧡💛💚💙💜🖤🤎"
    await _wrap_edit(message, joined_heart)
    for heart in BIG_SCROLL:
        await _wrap_edit(message, joined_heart.replace(R, heart))
        await asyncio.sleep(SLEEP)


async def phase2(message):
    """Per-heart randomiser"""
    ALL = ["❤️"] + list("🧡💛💚💙💜🤎🖤")  # don't include white heart

    format_heart = joined_heart.replace(R, "{}")
    for _ in range(5):
        heart = format_heart.format(*random.choices(ALL, k=heartlet_len))
        await _wrap_edit(message, heart)
        await asyncio.sleep(SLEEP)


async def phase3(message):
    """Fill up heartlet matrix"""
    await _wrap_edit(message, joined_heart)
    await asyncio.sleep(SLEEP * 2)
    repl = joined_heart
    for _ in range(joined_heart.count(W)):
        repl = repl.replace(W, R, 1)
        await _wrap_edit(message, repl)
        await asyncio.sleep(SLEEP)


async def phase4(message):
    """Matrix shrinking"""
    for i in range(7, 0, -1):
        heart_matrix = "\n".join([R * i] * i)
        await _wrap_edit(message, heart_matrix)
        await asyncio.sleep(SLEEP)


@app.on_message(filters.command(["magic"], prefixes=".") & filters.me)
async def hearts(app, message):
    score1 = (message.text.split()[1])
    await phase1(message)
    await phase2(message)
    await phase3(message)
    await phase4(message)
    await asyncio.sleep(SLEEP * 3)

    await message.edit(f"**{score1} {tag}**")
    await asyncio.sleep(0.5)

@app.on_message(filters.command('nick', '.') & filters.me)
async def ment(app, message):
    try:
        count = "".join(message.command[1])
        string = " ".join(message.command[2:])
        if count == "1":
            if "сменить" in message.text:
                string = string.replace("сменить", " ")
                with open("chars.json", "r") as file:
                   chars = json.load(file)
                for normal, font_char in chars.items():
                    string = string.replace(normal, font_char)
                await app.update_profile(first_name=string, last_name = "", bio="Developed by @starzedscripts")
                await message.edit("<b>Генерирую шрифт...</b>")
                await asyncio.sleep(2)
                await message.edit("<b>Отправка...</b>")
                await asyncio.sleep(0.7)
                await message.edit(f'<b>Ваш никнэйм готов!\nА так же применён!</b> <code>{string}</code>')
            else:
                with open("chars.json", "r") as file:
                    chars = json.load(file)
                for normal, font_char in chars.items():
                    string = string.replace(normal, font_char)
                await message.edit("<b>Генерирую шрифт...</b>")
                await asyncio.sleep(2)
                await message.edit("<b>Отправка...</b>")
                await asyncio.sleep(0.7)
                await message.edit(f'<b>Ваш никнэйм готов!</b>\n<code>{string}</code>')
        if count == "2":
            if "сменить" in message.text:
                string = string.replace("сменить", " ")
                with open("chars1.json", "r") as file:
                    chars = json.load(file)
                for normal, font_char in chars.items():
                    string = string.replace(normal, font_char)
                await app.update_profile(first_name=string, last_name = "", bio="Developed by @starzedscripts")
                await message.edit("<b>Генерирую шрифт...</b>")
                await asyncio.sleep(2)
                await message.edit("<b>Отправка...</b>")
                await asyncio.sleep(0.7)
                await message.edit(f'<b>Ваш никнэйм готов!\nА так же применён!</b> <code>{string}</code>')
            else:
                with open("chars1.json", "r") as file:
                    chars = json.load(file)
                for normal, font_char in chars.items():
                    string = string.replace(normal, font_char)
                await message.edit("<b>Генерирую шрифт...</b>")
                await asyncio.sleep(2)
                await message.edit("<b>Отправка...</b>")
                await asyncio.sleep(0.7)
                await message.edit(f'<b>Ваш никнэйм готов!</b>\n<code>{string}</code>')
        if count == "3":
            if "сменить" in message.text:
                string = string.replace("сменить", " ")
                with open("chars2.json", "r") as file:
                   chars = json.load(file)
                for normal, font_char in chars.items():
                    string = string.replace(normal, font_char)
                await app.update_profile(first_name=string, last_name = "", bio="Developed by @starzedscripts")
                await message.edit("<b>Генерирую шрифт...</b>")
                await asyncio.sleep(2)
                await message.edit("<b>Отправка...</b>")
                await asyncio.sleep(0.7)
                await message.edit(f'<b>Ваш никнэйм готов!\nА так же применён!</b> <code>{string}</code>')
            else:
                with open("chars2.json", "r") as file:
                   chars = json.load(file)
                for normal, font_char in chars.items():
                    string = string.replace(normal, font_char)
                await message.edit("<b>Генерирую шрифт...</b>")
                await asyncio.sleep(2)
                await message.edit("<b>Отправка...</b>")
                await asyncio.sleep(0.7)
                await message.edit(f'<b>Ваш никнэйм готов!</b>\n<code>{string}</code>')
        if count == "4":
            if "сменить" in message.text:
                string = string.replace("сменить", " ")
                with open("chars3.json", "r") as file:
                   chars = json.load(file)
                for normal, font_char in chars.items():
                    string = string.replace(normal, font_char)
                await app.update_profile(first_name=string, last_name = "", bio="Developed by @starzedscripts")
                await message.edit("<b>Генерирую шрифт...</b>")
                await asyncio.sleep(2)
                await message.edit("<b>Отправка...</b>")
                await asyncio.sleep(0.7)
                await message.edit(f'<b>Ваш никнэйм готов!\nА так же применён!</b> <code>{string}</code>')
            else:
                with open("chars3.json", "r") as file:
                   chars = json.load(file)
                for normal, font_char in chars.items():
                    string = string.replace(normal, font_char)
                await message.edit("<b>Генерирую шрифт...</b>")
                await asyncio.sleep(2)
                await message.edit("<b>Отправка...</b>")
                await asyncio.sleep(0.7)
                await message.edit(f'<b>Ваш никнэйм готов!</b>\n<code>{string}</code>')
    except:
        await message.edit("Инструкция:\n1 - 𝔸\n2 - 𝕬\n3 - 𝓐\n4 - Ⓐ\nПример:<code>.nick 3 text</code>")


@app.on_message(filters.command("uno", prefixes=".") & filters.me)
async def betaloves(_ ,msg):
    current = ""
    for chunk in unoo.splitlines():
        current += f"{chunk}\n"
        if not chunk.strip():
            continue
        await msg.edit(current)
        await asyncio.sleep(.60)
    sleep(4)
    await msg.edit(f'''{tag}''')




@app.on_message(filters.command("pizza", prefixes=".") & filters.me)
async def betaloves(_ ,msg):
    current = ""
    for chunk in piz.splitlines():
        current += f"{chunk}\n"
        if not chunk.strip():
            continue
        await msg.edit(current)
        await asyncio.sleep(.60)
    sleep(4)
    await msg.edit(f'''{tag}''')



@app.on_message(filters.command("pikachu", prefixes=".") & filters.me)
async def betaloves(_ ,msg):
    current = ""
    for chunk in pika.splitlines():
        current += f"{chunk}\n"
        if not chunk.strip():
            continue
        await msg.edit(current)
        await asyncio.sleep(.60)
    sleep(4)
    await msg.edit(f'''{tag}''')





@app.on_message(filters.command("gubka", prefixes=".") & filters.me)
async def betaloves(_ ,msg):
    current = ""
    for chunk in list(spanch):
        current += chunk
        if not chunk.strip():
            continue
        await msg.edit(current)
        await asyncio.sleep(.40)
    sleep(4)
    await msg.edit(f'''{tag}''')

            



@app.on_message(filters.command("gifspam", prefixes=".") & filters.me)
def sendgif(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил спам гифками!')
    global number
    number = number + 1
    try:
        for _ in range (int(message.command[1])):
            sleep(0.01)
            app.send_document(message.chat.id, "https://tenor.com/view/spam-toon-toonio-%D1%82%D1%83%D0%BD%D0%B8%D0%BE-pomidorkin-gif-24712213")
    except IndexError:
        message.edit("<b>Вы не ввели число!\nПример:</b><code>.gifspam 3</code>")

@app.on_message(filters.command("dead", prefixes=".") & filters.me)
def valentine(app, message):
    try:
        txt = textded.split("\n")
        e = True
        etime = int(message.text.split('.dead ', maxsplit=1)[1])
    except IndexError:
        message.edit("<b>Вы забыли указать скорость!\n Пример:</b> <code>.dead 0</code>")
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                message.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                message.delete()
            except:
                pass
        else:
            try:
                #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .dead')
                message.edit(f'❤️{i} ❤️')
                sleep(time/cool)
                message.edit(f'🧡 {i} 🧡')
                sleep(time/cool)
                message.edit(f'💛 {i} 💛')
                sleep(time/cool)
                message.edit(f'💚 {i} 💚')
                sleep(time/cool)
                message.edit(f'💙 {i} 💙')
                sleep(time/cool)
                message.edit(f'💜 {i} 💜')
                sleep(time/cool)
                message.edit(f'🖤 {i} 🖤')
                sleep(time/cool)
                message.edit(f'🤍 {i} 🤍')
                sleep(time/cool)
            except:
                pass
    global number
    number = number + 1
    message.edit(tag)
    message.edit(tager)

textded = '''
<b> Я дед инсайд </b>
<b> Мне 9 лет </b>
<b> И я хочу в Психокидс </b>
'''


# @app.on_message(filters.command("mining", prefixes=".") & filters.me)
# async def valentine(client, message):
#     twtw = 1.2
#     btc = [random.randint(0,1), random.random()]
#     #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .iq')
#     await message.edit(str("Start of mining"))
#     await message.edit(str("<b>Start of mining</b>"))
#     await message.edit(str("Start of mining"))
#     await message.edit(str("<b>Start of mining</b>"))
#     await message.edit(str("Start of mining"))
#     await message.edit(str("<b>Start of mining</b>"))
#     await message.edit(str("Start of mining"))
#     await message.edit(str("<b>Start of mining</b>"))
#     await message.edit(str("Start of mining"))
#     await message.edit(str("<b>Start of mining</b>"))
#     await message.edit(str("Start of mining"))
#     await message.edit("<b>Start of mining</b>")
#     await asyncio.sleep(2)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  112Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 1%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 8°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  89Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 2%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 9°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┅┅┅┅▌▒▌█  104Mh/s 
# █▐▒▐┅┅┅┅▌▒▌█  Mining: 5%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 18°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  102Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 9%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 23°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  98Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 15%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 29°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┅┅┅┅▌▒▌█  101Mh/s 
# █▐▒▐┅┅┅┅▌▒▌█  Mining: 29%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 43°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  113Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 46%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 52°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  110Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 47%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 53°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┅┅┅┅▌▒▌█  109Mh/s 
# █▐▒▐┅┅┅┅▌▒▌█  Mining: 49%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 51°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  108Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 54%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 54°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  111Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 60%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 59°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┅┅┅┅▌▒▌█  103Mh/s 
# █▐▒▐┅┅┅┅▌▒▌█  Mining: 70%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 62°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  90Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 70%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 51°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  114Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 89%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 31°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┅┅┅┅▌▒▌█  110Mh/s 
# █▐▒▐┅┅┅┅▌▒▌█  Mining: 92%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 35°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  108Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 95%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 42°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  101Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 99%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 49°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┅┅┅┅▌▒▌█  109Mh/s 
# █▐▒▐┅┅┅┅▌▒▌█  Mining: 100%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 40°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  109Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 100%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 23°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  109Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 100%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 9°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str('''
# ████████████ ——————
# █▐▒▒▄▄▄▄▒▒▌█  Rtx 3090 
# █▐▒▐┼┼┼┼▌▒▌█  109Mh/s 
# █▐▒▐┼┼┼┼▌▒▌█  Mining: 100%
# █▐▒▒▀▀▀▀▒▒▌█  Temp: 8°
# ████████████——————'''))
#     await asyncio.sleep(twtw)
#     await message.edit(str(f'''Mining results: {random.choice(btc)}<b>BTC</b>'''))


@app.on_message(filters.command("nuclear", prefixes=".") & filters.me)
async def valentine(client, message):
    country2 = ['Австралию', 'Австрия', 'Азербайджан', 'Албанию', 'Алжир', 'Анголу', 'Андорру', 'Антигуа и Барбуда', ' Аргентину', 'Армению', 'Афганистан', 'Багамы', 'Бангладеш', 'Барбадос', 'Бахрейн', 'Белоруссию', 'Белиз', 'Бельгию', 'Бенин', 'Болгарию', 'Боливию', 'Боснию и Герцеговину', 'Ботсвану', 'Бразилию', 'Бруней', 'Буркина-Фасо', 'Бурунди', 'Бутан', 'Вануату', 'Великобританию', 'Венгрию', 'Венесуэлу', 'Восточный Тимор', 'Вьетнам', 'Габон', 'Гаити', 'Гайану', 'Гамбию', 'Гану', 'Гватемалу', 'Гвинею', 'Гвинею-Бисау', 'Германию', 'Гондурас', 'Гренаду', 'Грецию', 'Грузию', 'Данию', ' Джибути', 'Доминику', 'Доминикану', 'Египет', 'Замбию', 'Зимбабве', 'Израиль', 'Индию', 'Индонезию', 'Иорданию', 'Ирак', 'Иран', 'Ирландию', 'Исландию', 'Испанию', 'Италию', 'Йемен', 'Кабо-Верде', 'Казахстан', 'Камбоджу', 'Камерун', 'Канаду', 'Катар', 'Кению', 'Кипр', 'Киргизию', 'Кирибати', 'Китай', 'Колумбию', 'Коморы', 'Конго', 'ДР Конго', 'КНДР', 'Корея', 'Коста-Рику', 'Кот-д’Ивуар', 'Кубу', 'Кувейт', 'Лаос', 'Латвию', 'Лесото', 'Либерию', 'Ливан', 'Ливию', 'Литву', 'Лихтенштейн', 'Люксембург', 'Маврикий', 'Мавританию', 'Мадагаскар', 'Малави', 'Малайзию', 'Мали', 'Мальдивы', 'Мальту', 'Марокко', 'Маршалловы Острова', 'Мексику', 'Микронезию', 'Мозамбик', 'Молдавию', 'Монако', 'Монголию', 'Мьянму', 'Намибию', 'Науру', 'Непал', 'Нигер', 'Нигерию', 'Нидерланды', 'Никарагую', 'Новую Зеландию', 'Норвегию', 'ОАЭ', 'Оман', 'Пакистан', 'Палау', 'Панаму', 'Новую Гвинею', 'Парагвай', 'Перу', 'Польшу', 'Португалию', 'Россию', 'Руанду', 'Румынию', 'Сальвадор', 'Самоу', 'Сан-Марино', 'Сан-Томе и Принсипи', 'Саудовскую Аравию', 'Северную Македонию', 'Сейшелы', 'Сенегал', 'Сент-Винсент и Гренадины', 'Сент-Китс и Невис', ' Сент-Люсию', 'Сербию', 'Сингапур', 'Сирию', 'Словакию', 'Словению', 'США', 'Соломоновы Острова', 'Сомали', 'Судан', 'Суринам', 'Сьерра-Леоне', 'Таджикистан', 'Tаиланд', 'Танзанию', 'Того', 'Тонгу', 'Тринидад и Тобаго', 'Тувалу', 'Тунис', 'Туркмению', 'Турцию', 'Уганду', 'Узбекистан', 'Украину', 'Уругвай', 'Фиджи', 'Филиппины', 'Финляндию', 'Францию', 'Хорватию', 'ЦАР', 'Чад', 'Черногорию', 'Чехию', 'Чили', 'Швейцарию', 'Швецию', 'Шри-Ланку', 'Эквадор', 'Экваториальную Гвинею', 'Эритрею', 'Эсватини', 'Эстонию', 'Эфиопию', 'ЮАР', 'Южный Судан', 'Ямайкy', 'Японию']
    country = ['Россия', 'США', 'Великобритания', 'Франция', 'Китай', 'Индия', 'Пакистан', 'Северная Корея', 'Израиль']
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .iq')
    await asyncio.sleep(2)
    await message.edit(str("<b>Выбор государства.</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Выбор государства..</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Выбор государства...</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Выбор государства.</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Выбор государства..</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Выбор государства...</b>"))
    await asyncio.sleep(0.9)
    country4 = random.choice(country)
    await message.edit(str(f"<b>Ядерную бомбу запускает - {country4}</b>"))
    await asyncio.sleep(1.9)
    await message.edit(str("<b>Вычисление кoординат.</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление кoординат..</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление кoординат...</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление кoординат.</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление кoординат..</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление кoординат...</b>"))
    await asyncio.sleep(0.9)
    country3 = random.choice(country2)
    await message.edit(str(f"<b>Ядерная бомба отправится в {country3}</b>"))
    await asyncio.sleep(1.9)
    await message.edit(str("<b>Подготовка.</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Подготовка..</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Подготовка...</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Подготовка.</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Подготовка..</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Подготовка...</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Запуск!</b>"))
    await asyncio.sleep(0.3)
    await message.edit(str("<b>Запуск!!</b>"))
    await asyncio.sleep(0.3)
    await message.edit(str("<b>Запуск!!!</b>"))
    await asyncio.sleep(0.7)
    await message.edit(str(f"<b>START {random.randint(1, 10)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>START {random.randint(10, 20)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>START {random.randint(20, 30)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>START {random.randint(30, 40)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>START {random.randint(40, 50)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>START {random.randint(50, 70)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>START {random.randint(80, 90)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>START 99%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"Successful launch ✅"))
    await asyncio.sleep(1.5)
    await message.edit(str(f"<b>Выброс ядерной энергии.</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Выброс ядерной энергии..</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Выброс ядерной энергии...</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Выброс ядерной энергии.</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Выброс ядерной энергии..</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Выброс ядерной энергии...</b>"))
    await asyncio.sleep(0.7)
    await message.edit(str(f"<b>Получение результатов {random.randint(1, 10)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Получение результатов {random.randint(10, 20)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Получение результатов {random.randint(20, 30)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Получение результатов {random.randint(30, 40)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Получение результатов {random.randint(40, 50)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Получение результатов {random.randint(50, 70)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Получение результатов {random.randint(80, 90)}%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"<b>Получение результатов 99%</b>"))
    await asyncio.sleep(0.5)
    await message.edit(str(f"Success ✅"))
    await asyncio.sleep(2)
    dieds = random.randint(10,100000)
    await message.edit(str(f"<b>🌐 Results: \n- Запуск ЯБ от <code>{country4}</code>\n- Выброс в <code>{country3}</code>\n- Мощность: <code>{random.randint(1,10)}</code>\n- Излучение: <code>{random.randint(10,69)}%</code>\n- Радиация: <code>{random.randint(1,19)}%</code>\n- Разрушения: <code>{random.randint(10,98)}%</code>\n- Смерти: <code>{dieds}</code>\n- Выжившие: <code>{random.randint(random.randint(10,10000),random.randint(1000,10000000))}</code> </b>"))


    

@app.on_message(filters.command("iq", prefixes=".") & filters.me)
async def valentine(client, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .iq')
    await message.edit(str("IQ"))
    await message.edit(str("<b>IQ</b>"))
    await message.edit(str("IQ"))
    await message.edit(str("<b>IQ</b>"))
    await message.edit(str("IQ"))
    await message.edit(str("<b>IQ</b>"))
    await message.edit(str("IQ"))
    await message.edit(str("<b>IQ</b>"))
    await message.edit(str("IQ"))
    await message.edit(str("<b>IQ</b>"))
    await message.edit(str("IQ"))
    await message.edit("<b>IQ</b>")
    await asyncio.sleep(2)
    await message.edit(str("<b>Вычисление.</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление..</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление...</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление.</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление..</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление...</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление.</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление..</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление...</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление.</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление..</b>"))
    await asyncio.sleep(0.9)
    await message.edit(str("<b>Вычисление...</b>"))
    await asyncio.sleep(1.9)
    text2 = f"<b>🏵 Ваш IQ ≈ {random.randint(60,200)}</b>"
    await message.edit(str(text2))
    await asyncio.sleep(5)


@app.on_message(filters.command("drugs", prefixes=".") & filters.me)
async def valentine(client, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .drugs')
    text = f"<b>💊 Поиск запрещённых препаратов.. </b>"
    await message.edit(str(text))
    await asyncio.sleep(2)
    kilogramm = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    text2 = f"<b>🚬 Найдено {random.choice(kilogramm)} кг шпекса</b>"
    await message.edit(str(text2))
    await asyncio.sleep(3)
    text3 = f"<b>🌿⚗️ Оформляем вкид</b>"
    await message.edit(str(text3))
    await asyncio.sleep(5)
    drugsss = [f'<b>😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты</b>',
               f'<b>🥴 Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид</b>',
               f'<b>😖 Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз</b>',
               f'<b>😌 Вы оформили вкид, Вам понравилось</b>']
    drug = random.choice(drugsss)
    await message.edit(drug)
    await asyncio.sleep(5)
    await message.edit(tag)

@app.on_message(filters.command("mum", prefixes=".") & filters.me)
async def mum(client, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .mum')
    mamka = [f'<b>❌ Мамаша не найдена</b>',f'<b> ✅ МАМАША НАЙДЕНА</b>' ]
    text = "<b>🔍 Поиск твоей мамки начался...</b>"
    await message.edit(str(text))
    await asyncio.sleep(3.0)
    text2 = "<b>🔍 Ищем твою мамашу на Авито... </b>"
    await message.edit(str(text2))
    await asyncio.sleep(1)
    text3 = random.choice(mamka)
    await message.edit(str(text3))
    await asyncio.sleep(3.0)
    text4 = "<b>🔍 Поиск твоей мамаши на свалке... </b>"
    await message.edit(str(text4))
    await asyncio.sleep(3.0)
    text5 = random.choice(mamka)
    await message.edit(str(text5))
    await asyncio.sleep(5.0)
    await message.edit(str(tag))

@app.on_message(filters.command("version", prefixes=".") & filters.me)
async def valentine(app, message):
    text = '[Criblle](https://github.com/Criblle/StarZed)'
    await app.send_message(message.chat.id, f''' Version: 1.3 \nGit Hub - ''' + text, parse_mode='Markdown')


@app.on_message(filters.command("xuy", prefixes=".") & filters.me)
async def valentine(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} отправил .xuy')
    await message.edit(f'''<b>🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆</b>''')


@app.on_message(filters.command("type", prefixes=".") & filters.me)
def valentine(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .type')
    global number
    number = number + 1
    try:
        orig_text = message.text.split(".type ", maxsplit=1)[1]
        text = orig_text
        tbp = ""
        typing_symbol = "█"
        while (tbp != orig_text):
            try:
                message.edit(tbp + typing_symbol)
                sleep(0.05)

                tbp = tbp + text[0]
                text = text[1:]

                message.edit(tbp)
                sleep(0.05)

            except FloodWait as e:
                sleep(e.x)
    except IndexError:
        message.edit("<b>Вы не ввели текст\nПример:</b> <code>.type текст</code>")


germany = '''
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
🟨🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨
'''


textded1 = '''
<b>спокойной ночи зайка 💚</b>
<b>спокойной ночи солнышко 💛</b>
<b>спокойной ночи котёнок ❤</b>️
<b>спокойной ночи цветочек 💙</b>
<b>спокойной ночи ангелочек 💜</b>
<b>спокойной ночи принцесса 💓</b>
<b>спокойной ночи красотка 💕</b>
<b>спокойной ночи милашка 💖</b>
<b>спокойной ночи симпатяжка 💗</b>
<b>спокойной ночи бусинка 💘</b>
<b>❤я❤</b>️
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
'''


@app.on_message(filters.command("compli", prefixes=".") & filters.me)
def valentine(app, message):
    try:
        txt = comp.split("\n")
        e = True
        etime = int(message.text.split('.compli ', maxsplit=1)[1])
    except IndexError:
        message.edit("<b>Вы забыли указать скорость!\n Пример:</b> <code>.compli 5</code>")
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                message.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                message.delete()
            except:
                pass
        else:
            try:
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .compli')
    global number
    number = number + 1
    message.edit(tag)
    message.edit(tager)


@app.on_message(filters.command("night", prefixes=".") & filters.me)
def valentine(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .night')
    txt = textded1.split("\n")
    e = True
    try:
        etime = int(message.text.split('.night ', maxsplit=1)[1])
    except IndexError:
        message.edit("<b>Вы не ввели число!\nПример:</b><code>.night 5</code>")
    else:
        for i in txt:
            time = etime
            if e == True:
                e = False
            elif time > 10:
                try:
                    message.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                    sleep(0.5)
                    message.delete()
                except:
                    pass
            else:
                try:
                    message.edit(f'{i}')
                    sleep(time/cool)
                    message.edit(f'{i}')
                    sleep(time/cool)
                    message.edit(f'{i}')
                    sleep(time/cool)
                    message.edit(f'{i}')
                    sleep(time/cool)
                    message.edit(f'{i}')
                    sleep(time/cool)
                    message.edit(f'{i}')
                    sleep(time/cool)
                    message.edit(f'{i}')
                    sleep(time/cool)
                    message.edit(f'{i}')
                    sleep(time/cool)
                except:
                    pass
        global number
        number = number + 1
        message.edit(tag)
        message.edit(tager)

@app.on_message(filters.command("random", prefixes=".") & filters.me)
def random_(app, message):
    try:
        x = int(message.command[1])
    except IndexError:
        message.edit("<b>Вы не ввели число для диапазона!\nПример:</b><code>.random 15</code>")
    else:
        random_number = str(random.randint(0, x))
        message.edit(roi + random_number)


chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
too = random.randint(0, 100)
roi = f'<b> Случайное число: </b>'
    
@app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
def valentine(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил спам .ghoul')
    global number
    number = number + 1
    sleep(2)
    i = 1000
    while i > 0:
        try:
            app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(0)

    if(end_message != ''):
        app.send_message(message.chat.id, tag)


@app.on_message(filters.command("clear", prefixes=".") & filters.me)
def spam(app, message):
    message.edit("<b>Консоль очищена!</b>")
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

#@app.on_message(filters.command("stop", prefixes = ".") & filters.me)
#def restartt(app, message):
    #print("Бот выключен.\nКоманда для перезапуска - cd StarZed $$ python start.py (Если вы находитесь уже в репозитории то введите python start.py)")
    #os.exit()



#@app.on_message(filters.command("dice", prefixes=".") & filters.me)
#async def dice_text(app, message):
 #   chat = message.chat
 #   try:
 #       values = [int(val) for val in message.text.split()[1].split(',')]
  #      if True not in [i in values for i in range(1, 7)]:
    #        return await message.edit('Защита от дурачка, число больше 6 или меньше 1, нельзя')
   #     message.dice = BaseDice
 #       while message.dice.value not in values:
           # message = (await asyncio.gather(message.delete(revoke=True),
   #                    app.send_dice(chat_id=chat.id)))[1]

   # except Exception as e:
        #await message.edit(f"<b>Произошла ошибка:</b> <code>{format_exc(e)}</code>")

#@app.on_message(filters.command("reaction", prefixes=".") & filters.me)
#def spam(app, message):
#    try:
  #      spams = " ".join(message.command[2:])
  #      global number
 #   #    number = number + 1
#    except:
  #      message.edit("<b>Вы не ввели число для спама!\nПример:</b><code>.spam 10 текст</code>")
  #  try:
   #     for _ in range(int(message.command[1])):
     #       sleep(0.01)
    #        app.send_reaction(message.chat.id, message_id, "🔥")
    #except IndexError:
       # message.edit("<b>Вы не ввели число для спама!\nПример:</b><code>.spam 10 текст</code>")
#



@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(app, message):
    try:
        spams = " ".join(message.command[2:])
        global number
        number = number + 1
    except:
        message.edit("<b>Вы не ввели число для спама!\nПример:</b><code>.spam 10 текст</code>")
    try:
        for _ in range(int(message.command[1])):
            sleep(0.01)
            app.send_message(message.chat.id, str(spams))
    except IndexError:
        message.edit("<b>Вы не ввели число для спама!\nПример:</b><code>.spam 10 текст</code>")


@app.on_message(filters.command("help", prefixes="/") & filters.me)
def valentine(app, message):
    app.send_message(message.chat.id,f'''
📙<b> Команды:</b> \n<b> - https://telegra.ph/Aktualnye-komandy-02-26</b> \n

💎 <b>Приобрести PREMIUM анимацию: </b>\n <b>- https://telegra.ph/Priobresti-Vip-status-03-02</b> \n                             

''', disable_web_page_preview=True)


@app.on_message(filters.command("install", prefixes=".") & filters.me)
def betalove(app, message):
    app.send_message(message.chat.id, f'''<b>
📕 Актуальный гайд по установке: https://telegra.ph/Ustanovka-animacii-Telegram-by-starzedscript-03-06

📹 Видео-гайд: https://youtu.be/QNeFXv1fj8Y

💌 Программа на компьютер: https://disk.yandex.ru/d/3JYVQiqxm5ht0A </b>
        ''',  disable_web_page_preview=True)


#https://giphy.com/gifs/art-ascii-detudoumpouku-HwE6lukm7fgqY
#@app.on_message(filters.command('update', prefixes=".") & filters.me)
#async def update(client, message):
 #   try:
  #      await message.edit('Updating...')
 #       link = "https://github.com/Criblle/StarZed/archive/refs/heads/main.zip"
   #     wget.download(link, 'temp/archive.zip')
#
  #      with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
   #         zip_ref.extractall("temp/")
    #    os.remove("temp/archive.zip")
#
 #       shutil.make_archive("temp/archive", "zip", "temp/StarZed-main/")
#
 #       with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
  #          zip_ref.extractall(".")
 #  #     os.remove("temp/archive.zip")
##
   #     await message.edit('Userbot succesfully updated\nRestarting...')
  #      await restart(message, restart_type="update")
    #except:
     #   await message.edit(f"An error occured...")

@app.on_message(filters.command("profile", prefixes="/") & filters.me)
def help(app, message):

    global number
    if message.from_user.id in {drax_id}:
        app.send_message(message.chat.id, f'''
💾<b> Профиль\n
</b> <b> Пользователь:</b><code> {message.from_user.first_name}</code>
<b>  Статус: </b> <code>{random.choice(a)}</code>\n
<b>  Префикс: </b> <code>{prefix}</code>
<b>  Chat_ID: </b><code> {message.chat.id}</code>
<b>  User_ID: </b><code> {message.from_user.id}</code>
<b>  Версия: </b><code> {version}</code>
<b>  Анимаций по старту:</b> <code>{number}</code>\n </b>''')
    if message.from_user.id in {crab_id, support_id}:
        app.send_message(message.chat.id, f'''
💾<b> Профиль\n
</b> <b> Пользователь:</b><code> {message.from_user.first_name}</code>
<b>  Статус: </b> <code>Developer</code>\n
<b>  Префикс: </b> <code>{prefix}</code>
<b>  Chat_ID: </b><code> {message.chat.id}</code>
<b>  User_ID: </b><code> {message.from_user.id}</code>
<b>  Версия: </b><code> {version}</code>
<b>  Анимаций по старту:</b> <code>{number}</code>\n </b>''')
    else:
        app.send_message(message.chat.id,f'''
💾<b> Профиль\n
</b> <b>Пользователь:</b><code> {message.from_user.first_name}</code>
<b> Статус: </b> <code>User</code>\n
<b> Префикс: </b> <code>{prefix}</code>
<b> Chat_ID: </b><code> {message.chat.id}</code>
<b> User_ID: </b><code> {message.from_user.id}</code>
<b> Версия: </b><code> {version}</code>
<b> Анимаций по старту:</b> <code>{number}</code>\n </b>''')
#<b> Ping:</b> 📶 <code>{str(okda.rtt_avg_ms)}Ms</code>


@app.on_message(filters.command("maslo", prefixes=".") & filters.me)
def betalove(app, message):

    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .maslo')
    time = 0.6
    for i in range(1):
        message.edit(f"<b>я</b>")  # red
        sleep(time)
        message.edit(f"<b>я люблю</b>")  # orange
        sleep(time)
        message.edit(f"<b>я люблю когда</b>")  # orange
        sleep(time)
        message.edit(f"<b>я люблю когда волосатые</b>")  # red
        sleep(time)
        message.edit(f"<b>я люблю когда волосатые мужики</b>")  # orange
        sleep(time)
        message.edit(f"<b>я люблю когда волосатые мужики обмазываются</b>")  # red
        sleep(time)
        message.edit(f"<b>я люблю когда волосатые мужики обмазываются маслом 🧈</b>")  # orange
        sleep(5)
        global number
        number = number + 1
        message.edit(tag)
        message.edit(tager)

@app.on_message(filters.command("football", prefixes=".") & filters.me)
def betalove(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .football')
    time = 0.6
    for i in range(1):
        message.edit(f"<b>⚽️ Вы зашли на футбольное поле, вам предстоит забить пенальти, чтобы победить</b>")  # red
        sleep(2)
        message.edit(f"<b>⏳ Подготовка к игре.</b>")  # orange
        sleep(2)
        message.edit(f"<b>⌛ Подготовка к игре..</b>")  # orange
        sleep(time)
        message.edit(f"<b>⏳ Подготовка к игре...</b>")  # red
        sleep(time)
        message.edit(f"<b>⚽ Удар.</b>")  # orange
        sleep(time)
        message.edit(f"<b>⚽ Удар..</b>")  # red
        sleep(time)
        message.edit(f"<b>⚽ Удар...</b>")  # orange
        sleep(time)
        message.edit(random.choice(foot))
        sleep(5)
        global number
        number = number + 1
        message.edit(tag)
        message.edit(tager)

foot = ["<b>❌ К сожалению, вы проиграли..</b>", "<b>✅ Вы забили гол и победили в игре!</b>"]

@app.on_message(filters.command("kill", prefixes=".") & filters.me)
def betalove(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .kill')
    time = 0.6
    for i in range(1):
        message.edit(f"<b>🔪 На тебя заказали убийство.</b>")  # red
        sleep(3)
        message.edit(f"<b>👀 У тебя есть пару секунд чтобы спрятаться.</b>")  # orange
        sleep(2)
        message.edit(f"<b>⏳ [ 5s ]</b>")  # orange
        sleep(time)
        message.edit(f"<b>⌛ [ 4s ]</b>")  # red
        sleep(time)
        message.edit(f"<b>⏳ [ 3s ]</b>")  # orange
        sleep(time)
        message.edit(f"<b>⌛ [ 2s ]</b>")  # red
        sleep(time)
        message.edit(f"<b>⏳ [ 1s ]</b>")  # orange
        sleep(time)
        message.edit(f"<b>🔪 Убийца вышел на твои поиски, надеюсь ты хорошо спрятался</b>")  # orange
        sleep(time)
        message.edit(f"<b>👀 Поиск.</b>")  # orange
        sleep(time)
        message.edit(f"<b>👀 Поиск..</b>")  # orange
        sleep(time)
        message.edit(f"<b>👀 Поиск...</b>")  # orange
        sleep(time)
        message.edit(f"<b>👀 Поиск.</b>")  # orange
        sleep(time)
        message.edit(f"<b>👀 Поиск..</b>")
        sleep(time)
        message.edit(f"<b>👀 Поиск...</b>")
        sleep(time)
        message.edit(random.choice(kill))
        sleep(5)
        global number
        number = number + 1
        message.edit(tag)
        message.edit(tager)

kill = ["<b>🔪 Убийца нашел тебя, к сожалению ты спрятался плохо и был убит</b>", "<b>⚔️Убийца не нашел тебя, вы  очень хорошо спрятались.</b>"]



@app.on_message(filters.command("jopa", prefixes=".") & filters.me)
def valentine(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .jopa')
    txt = jopa.split("\n")
    e = True
    try:
        etime = int(message.text.split('.jopa ', maxsplit=1)[1])
    except IndexError:
        message.edit("<b>Вы не ввели число!\nПример:</b><code>.jopa 5</code>")
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                message.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(1)
                message.edit("@starzedscripts")
            except:
                pass
        else:
            try:
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    global number
    number = number + 1
    message.edit(tag)
    message.edit(tager)


@app.on_message(filters.command("health", prefixes=".") & filters.me)
def valentine(app, message):
    try:
        txt = health.split("\n\n")
        e = True
        etime = int(message.text.split('.health ', maxsplit=1)[1])
    except IndexError:
        message.edit("<b>Вы забыли указать скорость!\n Пример:</b> <code>.health 5</code>")
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                message.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                message.edit("@starzedscripts")
            except:
                pass
        else:
            try:
                #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .health')
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    global number
    number = number + 1
    message.edit(tag)
    message.edit(tager)
            

            
@app.on_message(filters.command("firelove", prefixes=".") & filters.me)
def valentine(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .love')
    txt = heart2.split("\n\n")
    e = True
    try:
        etime = int(message.text.split('.firelove', maxsplit=1)[1])
    except ValueError:
        message.edit("<b>Вы не ввели число!\nПример:</b> <code>.firelove 5</code>")
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                message.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                message.delete()
            except:
                pass
        else:
            try:
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
            except:
                pass
    global number
    number = number + 1
    sleep(4)
    message.edit(tag)
    message.edit(tager)

@app.on_message(filters.command("animcryt", prefixes=".") & filters.me)
def spam(app, message):
    score = int(message.text.split()[1])
    global number
    number = number + score
    message.edit("<b>Number of animations changed ✅</b>")

@app.on_message(filters.command("love", prefixes=".") & filters.me)
def valentine(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .love')
    txt = love.split("\n")
    e = True
    try:
        etime = int(message.text.split('.love', maxsplit=1)[1])
    except IndexError:
        message.edit("<b>Вы не ввели число!\nПример:<b>.love 5</code>")
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                message.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                message.delete()
            except:
                pass
        else:
            try:
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    global number
    number = number + 1
    message.edit(tag)
    message.edit(tager)

@app.on_message(filters.command("zxc", prefixes=".") & filters.me)
def valentine(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .zxc')
    txt = zxc.split("\n")
    e = True
    try:
        etime = int(message.text.split('.zxc', maxsplit=1)[1])
    except ValueError:
        message.edit("<b>Вы не ввели число!\nПример:</b> <code>.zxc 5</code>")
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                message.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                message.delete()
            except:
                pass
        else:
            try:
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
                message.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    global number
    number = number + 1
    message.edit(tag)
    message.edit(tager)

@app.on_message(filters.command("ziga", prefixes=".") & filters.me)
def valentine(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .ziga')
    txt = ziga.split("\n\n")
    e = True
    try:
        etime = int(message.text.split('.ziga', maxsplit=1)[1])
    except IndexError:
        message.edit("<b>Вы не ввели число!\nПример:<b>.ziga 5</code>")
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                message.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                message.delete()
            except:
                pass
        else:
            try:
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
                message.edit(f'{i}')
                sleep(time)
            except:
                pass
    global number
    number = number + 1
    message.edit(tag)
    message.edit(tager)

@app.on_message(filters.command("like", prefixes=".") & filters.me)
async def betaloves(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .like')
    try:
        time = 0.6
        current = ""
        for chunk in list(anlike):
            current += chunk
            if not chunk.strip():
                continue
            await message.edit(current)
            await asyncio.sleep(.01)
        sleep(5)
        global number
        number = number + 1
    except FloodWait as e:
                sleep(e.x)
    finally:
        await message.edit(tag)

anlike = '''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦🟦
'''
@app.on_message(filters.command("dislike", prefixes=".") & filters.me)
async def betaloves(app, message):
    global number
    number = number + 1
    try:
        time = 0.6
        current = ""
        for chunk in list(denlike):
            current += chunk
            if not chunk.strip():
                continue
            await message.edit(current)
            await asyncio.sleep(.01)
    except FloodWait as e:
        sleep(e.x)
    finally:
        await message.edit(f'''
    🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
        await asyncio.sleep(1)
        await message.edit(f'''
    🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
    ''')
        await asyncio.sleep(1)
        await message.edit(f'''
    🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲
''')
        await asyncio.sleep(4)
        await message.edit(tag)

denlike = '''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
'''

@app.on_message(filters.command("loves", prefixes=".") & filters.me)
def betaloves(app, message):
    global number
    number = number + 1
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .loves')
    try:
        time = 0.6
        for i in range(1):
            message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨❤️❤️✨
✨✨❤️✨❤️✨
✨❤️✨✨❤️✨
✨✨✨✨✨✨''')  # red
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨✨✨✨✨''')  # red
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨✨✨
✨❤️❤️❤️✨✨
✨❤️✨✨✨✨
✨❤️❤️❤️❤️✨
✨✨✨✨✨✨''')
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨✨✨✨''')
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨❤️❤️✨
✨✨❤️✨❤️✨
✨❤️✨✨❤️✨
✨✨✨✨✨✨''')
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨❤️❤️✨❤️❤️✨✨
✨❤️❤️❤️❤️❤️❤️❤️✨
✨❤️❤️❤️❤️❤️❤️❤️✨
✨✨❤️❤️❤️❤️❤️✨✨
✨✨✨❤️❤️❤️✨✨✨
✨✨✨✨❤️✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💚💚✨💚💚✨✨
✨💚💚💚💚💚💚💚✨
✨💚💚💚💚💚💚💚✨
✨✨💚💚💚💚💚✨✨
✨✨✨💚💚💚✨✨✨
✨✨✨✨💚✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💙💙✨💙💙✨✨
✨💙💙💙💙💙💙💙✨
✨💙💙💙💙💙💙💙✨
✨✨💙💙💙💙💙✨✨
✨✨✨💙💙💙✨✨✨
✨✨✨✨💙✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💜💜✨💜💜✨✨
✨💜💜💜💜💜💜💜✨
✨💜💜💜💜💜💜💜✨
✨✨💜💜💜💜💜✨✨
✨✨✨💜💜💜✨✨✨
✨✨✨✨💜✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🤍🤍✨🤍🤍✨✨
✨🤍🤍🤍🤍🤍🤍🤍✨
✨🤍🤍🤍🤍🤍🤍🤍✨
✨✨🤍🤍🤍🤍🤍✨✨
✨✨✨🤍🤍🤍✨✨✨
✨✨✨✨🤍✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🖤🖤✨🖤🖤✨✨
✨🖤🖤🖤🖤🖤🖤🖤✨
✨🖤🖤🖤🖤🖤🖤🖤✨
✨✨🖤🖤🖤🖤🖤✨✨
✨✨✨🖤🖤🖤✨✨✨
✨✨✨✨🖤✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💛💛✨💛💛✨✨
✨💛💛💛💛💛💛💛✨
✨💛💛💛💛💛💛💛✨
✨✨💛💛💛💛💛✨✨
✨✨✨💛💛💛✨✨✨
✨✨✨✨💛✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
            sleep(time)
            message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🧡🧡✨🧡🧡✨✨
✨🧡🧡🧡🧡🧡🧡🧡✨
✨🧡🧡🧡🧡🧡🧡🧡✨
✨✨🧡🧡🧡🧡🧡✨✨
✨✨✨🧡🧡🧡✨✨✨
✨✨✨✨🧡✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
            sleep(3)
    except FloodWait as e:
        sleep(e.x)
    finally:
        message.edit(tag)

@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def betalove(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .heart')
    time = 0.6
    global number
    number = number + 1
    for i in range(1):
        try:
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
            sleep(time)
            message.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
            sleep(1)
        except FloodWait as e:
            sleep(e.x)
        finally:      
            message.edit(tag)
            message.edit(tager)




@app.on_message(filters.command("toxic", prefixes=".") & filters.me)
def valentine(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил спам .toxic')
    app.send_message(message.chat.id,f'''
<b>помолчи хуета, сиди в обиде ребёнок мертвой шалавы</b>
''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии.</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>пиздобратия мандопроушечная, уебище залупоглазое</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>дрочепиздище хуеголовое, пробиздоблядская мандопроушина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>гнидопаскудная хуемандовина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>ах ты блядь семитаборная чтоб тебя всем столыпином харили</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>охуевшее блядепиздопроёбище чтоб ты хуем поперхнулся долбоебическая пиздорвань</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>хуй тебе в глотку через анальный проход</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>распизди тебя тройным перебором через вторичный переёб пиздоблятское хуепиздрическое мудовафлоебище сосущее километры трипперных членов</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>трихломидозопиздоеблохуе блядеперепиздическая спермоблевотина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>гандон с гонореей...</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>да разъебись ты троебучим проебом сперматоблятская пиздапроебина </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>охуевающая в своей пидарастической сущности похожаю на ебущегося в жопу енота </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>сортирующего яйца в пизде кастрированной кобылы</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуелептический пиздопрозоид, еблоухий мандохвост</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебун хуеголовый, пидрасня ебаная. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Залупоголовая блядоящерица. .</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Трипиздоблядская промудохуина! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Распроеб твою в крестище через коромысло в копейку мать! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Что за блядская пиздопроебина, охуевающая своей пидорестической заебучестью невъебенной степени охуения. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Мордоблядина залупоглазая.  блядского невъебения! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Шлюшья мразота приохуебенивающая от собственного недохуеплетского злоетрахания. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Да произпездуй с 2000 этажа своей припиздоблядской тушей на землю в труху! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Трипиздоблядское мудопроебное трипиздие, ебоблядище охуевающее от собственной злоебучести.  </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Облямуденный злоебучий страхопизднутый трихуемандаблядский </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебаквакнутый распиздаеб... </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Хуесосляблядивый расхуйдяй припиздоблядского четвертоногого происхождения </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>прошу завали свой хуеобрыганский блядозвукоговоритель. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Промудохуепиздамразоблядское злоепиздие </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебоблядищая пиздопроебина сама ахуевающее от того какая оно пездоблядехуепроклятое.</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Обосробосанная пиздоблядмна двадцати головая семихуюлина припиздовывающее от хуеглотности своей трипиздговноглоталки.</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Облямудевшая хуеблядина четырестохуйная</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>вестипёздная мразотоблядская шлюхасосалка. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Хуесосная мудохуепиздопроебная мудаблядина сука безмаманя </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>блядь шмара козельуебок сдохни </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуесоска  ебланафт чмырь пидорска манда тупая гандопляс пидрила ебалай долбоеб обмудок овцееб дауниха  </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ненавижу гомодрилла сучка шлюха трахарила гавносос миньетчик </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>пидэраст пиздоеб хуеплет кончиглот ебище сын шлюхи гавноеб мудяра </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>еботрон вафлеглот ебалдуй захуятор имбицил подонок пиздопромудище </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>выебок ахуяэетер ебозер пиздолиз злоуебок хуиман ебил долбоебина пиндос мудазвон </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуеб амеба хуйло хуила пиздорвань смесь ебланства и говна ебанат </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>умалишенный дегенерат мандопроушина очкоблут порванный обрубок хуяраспиздяй свинозалупа</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>семиголовый восьмихуй ебоблядище свинохуярище вафлепиздище хуй лохматый жопа рванная мудопроеб </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>страхапиздище ебосос дурфанка косоуебище долбоногий лихохуетень</b>
     ''')
    sleep(0.5)
    global number
    number = number + 1
    app.send_message(message.chat.id, tag)

jopa = '''
           <b>ВЗЛОМ ЖОПЫ</b> 
           <b><i>Loading...</i></b> 
    10%  █▒▒▒▒▒▒▒▒▒▒▒▒
    30%  ███▒▒▒▒▒▒▒▒▒▒    
    50%  █████▒▒▒▒▒▒▒▒
    66%  ██████▒▒▒▒▒▒▒
    79%  ████████▒▒▒▒▒
    84%  █████████▒▒▒▒
    89%  ██████████▒▒▒
    95%  ████████████▒
    99%  █████████████
    100% █████████████
    <b> ВАША ЖОПА ВЗЛОМАНА </b>
    <b><i>Создатель: "Прощайте"</i></b>
    <b><i>Создатель: "Прощайте"</i></b>
    <b><i>Создатель: "Прощайте"</i></b>
'''
zxc = '''
<b>- All my friends are toxic, all ambitionless 💚</b>

<b>- All my friends are toxic, all ambitionless 💜</b>

<b>- All my friends are toxic, all ambitionless 💛</b>

<b>- So rude and always negative 🤍</b>

<b>- So rude and always negative 💚</b>

<b>- So rude and always negative 💛</b>

<b>- I need new friends, but it's not  that quick and easy 💔</b>

<b>- I need new friends, but it's not  that quick and easy 💛</b>

<b>- I need new friends, but it's not  that quick and easy 💚</b>

<b>- Oh, I'm drowning, let me breathe 💜</b>

<b>- Oh, I'm drowning, let me breathe 💛</b>

<b>- Oh, I'm drowning, let me breathe 💛</b>

'''



spanch = '''
╲┏━┳━━━━━━━━┓╲╲
╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲
╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲
╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲
╲┃◯┃╭╮╰╯┏━━━┳╯╲
╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲
╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲
'''

pika = '''
░█▀▀▄░░░░░░░░░░░▄▀▀█
░█░░░▀▄░▄▄▄▄▄░▄▀░░░█
░░▀▄░░░▀░░░░░▀░░░▄▀
░░░░▌░▄▄░░░▄▄░▐▀▀
░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█
░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█
█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀
░▀▄░░▀░░▀▀▀░░▀░░░▄█▀
░░░█░░░░░░░░░░░▄▀▄░▀▄
░░░█░░░░░░░░░▄▀█░░█░░█
░░░█░░░░░░░░░░░█▄█░░▄▀
░░░█░░░░░░░░░░░████▀
░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀
'''

unoo = '''
⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇
'''

piz = '''
█████████████████████████
█────█───█────█────█────█
█─██─██─████──███──█─██─█
█────██─███──███──██────█
█─█████─██──███──███─██─█
█─████───█────█────█─██─█
█████████████████████████
'''


love = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
<b>Загрузка любви...</b>
❤️🤍🤍🤍🤍🤍🤍🤍🤍🤍
❤️❤️🤍🤍🤍🤍🤍🤍🤍🤍
❤️❤️❤️🤍🤍🤍🤍🤍🤍🤍
❤️❤️❤️❤️🤍🤍🤍🤍🤍🤍
❤️❤️❤️❤️❤️🤍🤍🤍🤍🤍
❤️❤️❤️❤️❤️❤️🤍🤍🤍🤍
❤️❤️❤️❤️❤️❤️❤️🤍🤍🤍
❤️❤️❤️❤️❤️❤️❤️❤️🤍🤍
❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>

'''

comp = '''
<b>Крошечные напоминания того, что ты...</b> 

<b>Самая удивительная</b> ✨

<b>Самая внимательная</b> ✨

<b>Самая красивая</b> ✨

<b>Самая успешная</b> ✨

<b>Самая заботливая</b> ✨

<b>Самая милая</b> ✨

<b>Самая прекрасная</b> ✨

<b>Самая умная</b> ✨

<b>Самая шикарная</b> ✨

<b>Самая обалденная ✨</b>

<b>Самая очаровашка</b> ✨

<b>Самая любимая</b> ✨

<b>Самая весёлая</b> ✨

<b>Самая нежная</b> ✨

<b>Самая яркая</b> ✨

<b>Самая прелестная</b> ✨

<b>Самая приятная</b> ✨

<b>Самая сладкая</b> ✨

<b>Самая дивная</b> ✨

<b>Самая ангельская</b> ✨

<b>Самая добрая</b> ✨

<b>Самая бесподобная</b> ✨

<b>Самая волшебная</b> ✨

<b>Самая лучшая</b> ✨

<b>Самая крутышка</b> ✨

<b>Самая аромтная</b> ✨

<b>Самая единственная</b> ✨

<b>Самая искренняя</b> ✨

<b>Самая ласковая</b> ✨

<b>Самая романтичная</b> ✨

<b>Самая великолепная</b> ✨

<b>Самая внимательная</b> ✨

<b>Самая страстная</b> ✨

<b>Самая игривая</b> ✨

<b>Самая стройная</b> ✨

<b>Самая безумная</b> ✨

<b>Самая симпатичная</b> ✨

<b>Самая изящная </b> ✨

<b>Самая талантливая ✨</b>

<b>Самая элегантная ✨</b>

<b>Самая чуткая ✨</b>

<b>Самая отзывчивая ✨</b>

<b>Самая уникальная ✨</b>

<b>Самая смелая ✨</b>

<b>Самая уверенная ✨</b>

<b>Самая особенная ✨</b>

<b>Самая изумительная ✨</b>

<b>Самая настоящая ✨</b>

<b>Самая обаятельная ✨</b>

<b>Самая пушистая ✨</b>

<b>Самая кокетливая ✨</b>

<b>Самая теплая ✨</b>

<b>Самая энергичная ✨</b>

<b>Самая неотразимая ✨</b>

<b>Самая неописуемая ✨</b>

<b>Самая грациозная ✨</b>

<b>Самая сказочная ✨</b>

<b>Самая желанная ✨</b>

<b>Самая изысканная ✨</b>

<b>Самая мечтательная ✨</b>

<b>Самая безупречная ✨</b>

<b>Самая совершеная ✨</b>

<b>Самая честная ✨</b>

<b>Самая улыбчивая ✨</b>

<b>Самая ненаглядная ✨</b>

<b>Самая женственная ✨</b>

<b>Самая цветущая ✨</b>

<b>Самая гармоничная ✨</b>

<b>Самая отрадная ✨</b>
'''

ziga = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️❤️🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️❤️🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

health = '''

💟💟💟💟💟💟💟💟💟
💟☕️♥️♥️♥️♥️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️♥️♥️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️♥️♥️♥️☕️☕️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️♥️☕️☕️♥️☕️💟
💟☕️♥️☕️♥️☕️♥️☕️💟
💟☕️♥️♥️☕️☕️♥️☕️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️☕️♥️♥️♥️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️☕️☕️☕️☕️♥️☕️💟
💟☕️☕️☕️☕️♥️☕️☕️💟
💟☕️☕️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️☕️♥️♥️♥️☕️☕️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️☕️♥️♥️♥️☕️☕️💟
💟☕️☕️♥️☕️♥️☕️☕️💟
💟☕️☕️♥️☕️♥️☕️☕️💟
💟☕️♥️♥️♥️♥️♥️☕️💟
💟♥️♥️♥️♥️♥️♥️♥️💟
💟♥️☕️☕️☕️☕️☕️♥️💟
💟♥️☕️☕️☕️☕️☕️♥️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️☕️♥️♥️♥️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️☕️♥️♥️♥️☕️☕️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️☕️♥️♥️♥️☕️☕️💟
💟☕️☕️♥️☕️☕️♥️☕️💟
💟☕️☕️♥️☕️☕️♥️☕️💟
💟☕️☕️♥️♥️♥️☕️☕️💟
💟☕️☕️♥️☕️☕️☕️☕️💟
💟☕️☕️♥️☕️☕️☕️☕️💟
💟☕️☕️♥️☕️☕️☕️☕️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️☕️♥️♥️♥️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️☕️☕️☕️☕️♥️☕️💟
💟☕️☕️☕️☕️☕️♥️☕️💟
💟☕️♥️♥️♥️♥️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️☕️♥️♥️♥️☕️♥️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️♥️♥️♥️♥️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️♥️♥️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️♥️♥️♥️☕️☕️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️☕️☕️♥️♥️♥️☕️💟
💟☕️☕️♥️☕️☕️♥️☕️💟
💟☕️☕️♥️☕️☕️♥️☕️💟
💟☕️☕️♥️☕️☕️♥️☕️💟
💟☕️☕️♥️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️♥️♥️☕️💟
💟☕️♥️☕️♥️☕️♥️☕️💟
💟☕️♥️♥️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️♥️♥️♥️♥️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️♥️♥️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️♥️♥️♥️☕️☕️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️☕️♥️♥️♥️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️☕️☕️☕️☕️♥️☕️💟
💟☕️☕️☕️☕️☕️♥️☕️💟
💟☕️☕️♥️♥️♥️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️☕️♥️♥️♥️☕️♥️💟
💟💟💟💟💟💟💟💟💟

💟💟💟💟💟💟💟💟💟
💟☕️☕️♥️☕️♥️☕️☕️💟
💟☕️☕️☕️♥️☕️☕️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️♥️♥️☕️💟
💟☕️♥️☕️♥️☕️♥️☕️💟
💟☕️♥️♥️☕️☕️♥️☕️💟
💟☕️♥️☕️☕️☕️♥️☕️💟
💟💟💟💟💟💟💟💟💟

'''


@app.on_message(filters.command("house", prefixes=".") & filters.me)
async def betaloves(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .like')
    try:
        time = 0.6
        current = ""
        for chunk in list(home):
            current += chunk
            if not chunk.strip():
                continue
            await message.edit(current)
            await asyncio.sleep(.01)
        sleep(5)
        global number
        number = number + 1
    except FloodWait as e:
                sleep(e.x)
    finally:
        await message.edit(tag)

@app.on_message(filters.command("tv", prefixes=".") & filters.me)
async def betaloves(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .like')
    try:
        pretext = str(message.text.split()[1])
        TV = f'''
░▀▄░░▄▀
▄▄▄██▄▄▄▄▄░▀█▀▐░▌
█▒░▒░▒░█▀█░░█░▐░▌
█░▒░▒░▒█▀█░░█░░█
█▄▄▄▄▄▄███══════

{pretext}'''
        time = 0.6
        current = ""
        for chunk in list(TV):
            current += chunk
            if not chunk.strip():
                continue
            await message.edit(current)
            await asyncio.sleep(.02)
        sleep(5)
        global number
        number = number + 1
    except FloodWait as e:
                sleep(e.x)
    finally:
        await asyncio.sleep(2)
        await message.edit(tag)

@app.on_message(filters.command("lol", prefixes=".") & filters.me)
async def betaloves(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .like')
    try:
        time = 0.6
        current = ""
        for chunk in list(lol):
            current += chunk
            if not chunk.strip():
                continue
            await message.edit(current)
            await asyncio.sleep(.01)
        sleep(5)
        global number
        number = number + 1
    except FloodWait as e:
                sleep(e.x)
    finally:
        await asyncio.sleep(2)
        await message.edit(tag)


@app.on_message(filters.command("tea", prefixes=".") & filters.me)
async def betaloves(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .like')
    try:
        teatext = str(message.text.split()[1])
        tea = f'''
─▄▀─▄▀
──▀──▀
█▀▀▀▀▀█▄
█░░░░░█─█
▀▄▄▄▄▄▀▀

{teatext}
'''
        time = 0.6
        current = ""
        for chunk in list(tea):
            current += chunk
            if not chunk.strip():
                continue
            await message.edit(current)
            await asyncio.sleep(.01)
        sleep(5)
        global number
        number = number + 1
    except FloodWait as e:
                sleep(e.x)
    finally:
        await asyncio.sleep(2)
        await message.edit(tag)

@app.on_message(filters.command("bruh", prefixes=".") & filters.me)
async def betaloves(app, message):
    #bot.send_message(-733171711, f' - Пользователь @{message.from_user.username} запустил анимацию .like')
    try:
        time = 0.6
        current = ""
        for chunk in list(bruh):
            current += chunk
            if not chunk.strip():
                continue
            await message.edit(current)
            await asyncio.sleep(.01)
        sleep(5)
        global number
        number = number + 1
    except FloodWait as e:
                sleep(e.x)
    finally:
        await asyncio.sleep(2)
        await message.edit(tag)

home = '''
╯▅╰╱▔▔▔▔▔▔▔╲╯╯
▕▕╱╱╱╱╱╱╱╱╱╲╲╭╭
▕▕╱╱╱╱╱╱╱╱┛▂╲╲╭
╱▂▂▂▂▂▂╱╱┏▕╋▏╲╲
▔▏▂┗┓▂▕▔┛▂┏▔▂▕▔
▕▕╋▏▕╋▏▏▕┏▏▕╋▏▏
▕┓▔┗┓▔┏▏▕┗▏ ┓▔┏
'''



lol = '''
┏━┓┈┈╭━━━━╮┏━┓┈┈
┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈
┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓
┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃
┗━━━┛╰━━━━╯┗━━━┛
'''


bruh = '''
╭━━╮╱╱╱╱╱╭╮
┃╭╮┃╱╱╱╱╱┃┃
┃╰╯╰┳━┳╮╭┫╰━╮
┃╭━╮┃╭┫┃┃┃╭╮┃
┃╰━╯┃┃┃╰╯┃┃┃┃
╰━━━┻╯╰━━┻╯╰╯
'''
#@bot.message_handler(commands=['start'])
#def start(message):
   # bot.send_message(-733171711, 'Logs enabled')

heart2='''
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿🕯👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿

👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏻👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏻🕯👍🏻👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏻👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿

👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏽👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏽👍🏻👍🏽👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏽👍🏻🕯👍🏻👍🏽👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏽👍🏻👍🏽👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏽👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿

👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏾👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏾👍🏼👍🏾👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏾👍🏼👍🏻👍🏼👍🏾👍🏿👍🏿
👍🏿👍🏾👍🏼👍🏻🕯👍🏻👍🏼👍🏾👍🏿
👍🏿👍🏿👍🏾👍🏼👍🏻👍🏼👍🏾👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏾👍🏼👍🏾👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏾👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿👍🏿

👍🏿👍🏿👍🏿👍🏿👍🏾👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏾👍🏽👍🏾👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏾👍🏽👍🏼👍🏽👍🏾👍🏿👍🏿
👍🏿👍🏾👍🏽👍🏼👍🏻👍🏼👍🏽👍🏾👍🏿
👍🏾👍🏽👍🏼👍🏻🕯👍🏻👍🏼👍🏽👍🏾
👍🏿👍🏾👍🏽👍🏼👍🏻👍🏼👍🏽👍🏾👍🏿
👍🏿👍🏿👍🏾👍🏽👍🏼👍🏽👍🏾👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏾👍🏽👍🏾👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏾👍🏿👍🏿👍🏿👍🏿

👍🏿👍🏿👍🏿👍🏿👍🏾👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿🔥👍🏽🔥👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏾👍🏽👍🏼👍🏽👍🏾👍🏿👍🏿
👍🏿🔥👍🏽👍🏼👍🏻👍🏼👍🏽🔥👍🏿
👍🏾👍🏽👍🏼👍🏻🕯👍🏻👍🏼👍🏽👍🏾
👍🏿🔥👍🏽👍🏼👍🏻👍🏼👍🏽🔥👍🏿
👍🏿👍🏿👍🏾👍🏽👍🏼👍🏽👍🏾👍🏿👍🏿
👍🏿👍🏿👍🏿🔥👍🏽🔥👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏾👍🏿👍🏿👍🏿👍🏿

👍🏿👍🏿👍🏿👍🏿👍🏾👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏾🔥👍🏾👍🏿👍🏿👍🏿
👍🏿👍🏿🔥👍🏽👍🏼👍🏽🔥👍🏿👍🏿
👍🏿👍🏾👍🏽👍🏼👍🏻👍🏼👍🏽👍🏾👍🏿
👍🏾🔥👍🏼👍🏻🕯👍🏻👍🏼🔥👍🏾
👍🏿👍🏾👍🏽👍🏼👍🏻👍🏼👍🏽👍🏾👍🏿
👍🏿👍🏿🔥👍🏽👍🏼👍🏽🔥👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏾🔥👍🏾👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏾👍🏿👍🏿👍🏿👍🏿

👍🏿👍🏿👍🏿👍🏿👍🏾👍🏿👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿🔥🔥🔥👍🏿👍🏿👍🏿
👍🏿👍🏿🔥👍🏽👍🏼👍🏽🔥👍🏿👍🏿
👍🏿🔥👍🏽👍🏼👍🏻👍🏼👍🏽🔥👍🏿
👍🏾🔥👍🏼👍🏻🕯👍🏻👍🏼🔥👍🏾
👍🏿🔥👍🏽👍🏼👍🏻👍🏼👍🏽🔥👍🏿
👍🏿👍🏿🔥👍🏽👍🏼👍🏽🔥👍🏿👍🏿
👍🏿👍🏿👍🏿🔥🔥🔥👍🏿👍🏿👍🏿
👍🏿👍🏿👍🏿👍🏿👍🏾👍🏿👍🏿👍🏿👍🏿

👍🏿👍🏿👍🏿👍🏿🔥👍🏿👍🏿👍🏿👍🏿
👍🏿🔥👍🏿🔥🔥🔥👍🏿🔥👍🏿
👍🏿👍🏿🔥👍🏽👍🏼👍🏽🔥👍🏿👍🏿
👍🏿🔥👍🏽👍🏼👍🏻👍🏼👍🏽🔥👍🏿
🔥🔥👍🏼👍🏻🕯👍🏻👍🏼🔥🔥
👍🏿🔥👍🏽👍🏼👍🏻👍🏼👍🏽🔥👍🏿
👍🏿👍🏿🔥👍🏽👍🏼👍🏽🔥👍🏿👍🏿
👍🏿🔥👍🏿🔥🔥🔥👍🏿🔥👍🏿
👍🏿👍🏿👍🏿👍🏿🔥👍🏿👍🏿👍🏿👍🏿

🔥👍🏿🔥👍🏿🔥👍🏿🔥👍🏿🔥
👍🏿🔥👍🏿🔥🔥🔥👍🏿🔥👍🏿
🔥👍🏿🔥👍🏽👍🏼👍🏽🔥👍🏿🔥
👍🏿🔥👍🏽👍🏼👍🏻👍🏼👍🏽🔥👍🏿
🔥🔥👍🏼👍🏻🕯👍🏻👍🏼🔥🔥
👍🏿🔥👍🏽👍🏼👍🏻👍🏼👍🏽🔥👍🏿
🔥👍🏿🔥👍🏽👍🏼👍🏽🔥👍🏿🔥
👍🏿🔥👍🏿🔥🔥🔥👍🏿🔥👍🏿
🔥👍🏿🔥👍🏿🔥👍🏿🔥👍🏿🔥

🔥💥🔥💥🔥💥🔥💥🔥
💥🔥💥🔥🔥🔥💥🔥💥
🔥💥🔥👍🏽👍🏼👍🏽🔥💥🔥
💥🔥👍🏽👍🏼👍🏻👍🏼👍🏽🔥💥
🔥🔥👍🏼👍🏻🌫👍🏻👍🏼🔥🔥
💥🔥👍🏽👍🏼👍🏻👍🏼👍🏽🔥💥
🔥💥🔥👍🏽👍🏼👍🏽🔥💥🔥
💥🔥💥🔥🔥🔥💥🔥💥
🔥💥🔥💥🔥💥🔥💥🔥


🔥💥🔥💥🔥💥🔥💥🔥
💥🔥🔥🔥🔥🔥💥🔥💥
🔥💥🔥👍🏽👍🏼👍🏽🔥💥🔥
💥🔥👍🏽👍🏼🌫👍🏼👍🏽🔥🔥
🔥🔥👍🏼🌫🌫🌫👍🏼🔥🔥
🔥🔥👍🏽👍🏼🌫👍🏼👍🏽🔥💥
🔥💥🔥👍🏽👍🏼👍🏽🔥💥🔥
💥🔥💥🔥🔥🔥🔥🔥💥
🔥💥🔥💥🔥💥🔥💥🔥

🔥💥🔥💥🔥🔥🔥💥🔥
💥🔥💥🔥🔥🔥💥🔥💥
🔥💥🔥👍🏽🌫👍🏽🔥💥🔥
🔥🔥👍🏽👍🏼🌫👍🏼👍🏽🔥💥
🔥🔥🌫🌫🌫🌫🌫🔥🔥
💥🔥👍🏽👍🏼🌫👍🏼👍🏽🔥🔥
🔥🔥🔥👍🏽🌫👍🏽🔥💥🔥
💥🔥💥🔥🔥🔥🔥🔥💥
🔥🔥🔥💥🔥💥🔥💥🔥

🔥💥🔥💥🔥🔥🔥💥🔥
💥🔥💥🔥🌫🔥💥🔥💥
🔥💥🌫👍🏽🌫👍🏽🌫💥🔥
🔥🔥👍🏽👍🏼🌫👍🏼👍🏽🔥💥
🔥🌫🌫🌫🌫🌫🌫🌫🔥
💥🔥👍🏽👍🏼🌫👍🏼👍🏽🔥🔥
🔥🔥🌫👍🏽🌫👍🏽🌫💥🔥
💥🔥💥🔥🌫🔥🔥🔥💥
🔥🔥🔥💥🔥💥🔥💥🔥

🔥💥🔥💥🌫🔥🔥💥🔥
💥🔥💥🔥🌫🔥💥🔥💥
🔥🌫🌫🌫🌫🌫🌫🌫🔥
🔥🔥👍🏽👍🏼🌫👍🏼👍🏽🔥💥
🌫🌫🌫🌫🌫🌫🌫🌫🌫
💥🔥👍🏽👍🏼🌫👍🏼👍🏽🔥🔥
🔥🌫🌫🌫🌫🌫🌫🌫🔥
💥🔥💥🔥🌫🔥🔥🔥💥
🔥🔥🔥💥🌫💥🔥💥🔥

🔥💥🔥💥🌫🔥🔥💥🔥
💥🔥💥🔥🌫🔥💥🔥💥
🔥🌫🌫🌫🌫🌫🌫🌫🔥
🔥🔥🌫👍🏼🌫👍🏼🌫🔥💥
🌫🌫🌫🌫🌫🌫🌫🌫🌫
💥🔥🌫👍🏼🌫👍🏼🌫🔥🔥
🔥🌫🌫🌫🌫🌫🌫🌫🔥
💥🔥💥🔥🌫🔥🔥🔥💥
🔥🔥🔥💥🌫💥🔥💥🔥

🌫🌫🌫🌫🌫🌫🌫🌫🌫
🌫🌫🌫🌫🌫🌫🌫🌫🌫
🌫🌫🌫🌫🌫🌫🌫🌫🌫
🌫🌫🌫🌫🌫🌫🌫🌫🌫
🌫🌫🌫🌫🌫🌫🌫🌫🌫
🌫🌫🌫🌫🌫🌫🌫🌫🌫
🌫🌫🌫🌫🌫🌫🌫🌫🌫
🌫🌫🌫🌫🌫🌫🌫🌫🌫
🌫🌫🌫🌫🌫🌫🌫🌫🌫

🌫🌫🌫🌫🌫🌫🌫🌫🌫
🌫🌫♥️♥️🌫♥️♥️🌫🌫
🌫♥️♥️♥️♥️♥️♥️♥️🌫
🌫♥️♥️♥️♥️♥️♥️♥️🌫
🌫♥️♥️♥️♥️♥️♥️♥️🌫
🌫🌫♥️♥️♥️♥️♥️🌫🌫
🌫🌫🌫♥️♥️♥️🌫🌫🌫
🌫🌫🌫🌫♥️🌫🌫🌫🌫
🌫🌫🌫🌫🌫🌫🌫🌫🌫

🌸🌸🌸🌸🌸🌸🌸🌸🌸
🌸🌸♥️♥️🌸♥️♥️🌸🌸
🌸♥️♥️♥️♥️♥️♥️♥️🌸
🌸♥️♥️♥️♥️♥️♥️♥️🌸
🌸♥️♥️♥️♥️♥️♥️♥️🌸
🌸🌸♥️♥️♥️♥️♥️🌸🌸
🌸🌸🌸♥️♥️♥️🌸🌸🌸
🌸🌸🌸🌸♥️🌸🌸🌸🌸
🌸🌸🌸🌸🌸🌸🌸🌸🌸

'''


prelove = '''
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️☁️❤️❤️❤️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️☁️❤️❤️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️☁️❤️❤️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️☁️☁️☁️❤️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️☁️❤️❤️❤️☁️❤️☁️
☁️❤️☁️☁️☁️☁️☁️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️☁️☁️❤️☁️☁️❤️☁️
☁️❤️☁️☁️☁️☁️☁️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️☁️☁️❤️☁️☁️❤️☁️
☁️❤️☁️☁️☁️☁️☁️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️☁️❤️☁️❤️❤️☁️
☁️❤️❤️☁️☁️☁️❤️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️☁️☁️☁️❤️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️☁️❤️❤️❤️☁️
☁️☁️❤️❤️❤️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️☁️❤️❤️❤️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️☁️❤️❤️❤️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️☁️❤️❤️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️☁️❤️❤️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️☁️☁️☁️❤️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️☁️❤️❤️❤️☁️❤️☁️
☁️❤️☁️☁️☁️☁️☁️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️☁️☁️❤️☁️☁️❤️☁️
☁️❤️☁️☁️☁️☁️☁️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️☁️☁️❤️☁️☁️❤️☁️
☁️❤️☁️☁️☁️☁️☁️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️☁️❤️☁️❤️❤️☁️
☁️❤️❤️☁️☁️☁️❤️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️☁️☁️☁️❤️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️☁️❤️❤️❤️☁️
☁️☁️❤️❤️❤️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️☁️❤️❤️❤️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️☁️❤️❤️❤️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️☁️❤️❤️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️☁️❤️❤️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️☁️☁️☁️❤️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️☁️❤️❤️❤️☁️❤️☁️
☁️❤️☁️☁️☁️☁️☁️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️☁️☁️❤️☁️☁️❤️☁️
☁️❤️☁️☁️☁️☁️☁️❤️☁️
☁️☁️❤️☁️☁️☁️❤️☁️☁️
☁️☁️☁️❤️☁️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️☁️☁️❤️☁️☁️❤️☁️
☁️❤️☁️☁️☁️☁️☁️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️☁️❤️☁️❤️❤️☁️
☁️❤️❤️☁️☁️☁️❤️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️☁️☁️☁️❤️❤️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️☁️❤️❤️❤️☁️
☁️☁️❤️❤️❤️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️

☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️❤️❤️☁️❤️❤️☁️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️❤️❤️❤️❤️❤️❤️❤️☁️
☁️☁️❤️❤️❤️❤️❤️☁️☁️
☁️☁️☁️❤️❤️❤️☁️☁️☁️
☁️☁️☁️☁️❤️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️☁️☁️
'''

end_message = '<b> ⭐ @starzedscripts </b>'
try:
    doSomething()
except: 
    pass
app.run()
