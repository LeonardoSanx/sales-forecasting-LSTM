import os, telebot
from telegram.ext import MessageHandler
import requests

import pandas as pd



API_KEY = os.environ.get('FORECASTING_API_KEY')
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

@bot.message_handler(commands=['start'])
def start(message):      
    bot.send_message(message.chat.id, "Para receber as previsões de venda das lojas basta me enviar os comandos com os ID's (de '/0' até '/59').")



bot.polling()





