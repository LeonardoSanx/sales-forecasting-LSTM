import os, telebot
from telegram import Bot
from telegram.ext import MessageHandler
import requests

import pandas as pd
import matplotlib.pyplot as plt



API_KEY = os.environ.get('1845664289:AAH2ciPcxXuW08LuHXk8-q4Yrlb6kPQObX8')#('FORECASTING_API_KEY')
bot = telebot.TeleBot(API_KEY)

predictions = pd.read_csv('predictions.csv',index_col='date')

shop_ids_list = [str(x) for x in range(60)]

@bot.message_handler(commands=shop_ids_list)
def shops(message):  
    file_path = 'graphs//{}.png'
    #try:
    shop_id = int(message.text[1:])
    total = predictions.iloc[:,shop_id].sum()
    
    bot.send_message(message.chat.id, "Previsão de {} itens vendidos para os próximos 30 dias.".format(total))
    bot.send_photo(message.chat.id, (open(file_path.format(shop_id),'rb') ), )
    #except:
        #bot.send_message(message.chat.id, "Foi nao")

bot.polling()





