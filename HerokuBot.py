{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "connected-stake",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os, telebot\n",
    "from telegram import Update, ForceReply, Bot\n",
    "from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext\n",
    "import requests\n",
    "\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "import pygal\n",
    "from pygal.style import DefaultStyle # PB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "accessible-cartridge",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Shops_forecastBot'"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "API_KEY = os.environ.get('FORECASTING_API_KEY')\n",
    "bot = telebot.TeleBot(API_KEY)\n",
    "'Shops_forecastBot'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "alleged-presentation",
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions = pd.read_csv('predictions.csv',index_col='date')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "certain-camcorder",
   "metadata": {},
   "outputs": [],
   "source": [
    "shop_ids_list = [str(x) for x in range(60)]\n",
    "\n",
    "@bot.message_handler(commands=shop_ids_list)\n",
    "def shops(message):  \n",
    "    file_path = 'graphs//{}.png'\n",
    "    #try:\n",
    "    shop_id = int(message.text[1:])\n",
    "    total = predictions.iloc[:,shop_id].sum()\n",
    "    \n",
    "    bot.send_message(message.chat.id, \"Previsão de {} itens vendidos para os próximos 30 dias.\".format(total))\n",
    "    bot.send_photo(message.chat.id, (open(file_path.format(shop_id),'rb') ), )\n",
    "    #except:\n",
    "        #bot.send_message(message.chat.id, \"Foi nao\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "proper-knife",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2021-07-08 22:10:32,663 (__init__.py:544 MainThread) ERROR - TeleBot: \"A request to the Telegram API was unsuccessful. Error code: 502. Description: Bad Gateway\"\n"
     ]
    }
   ],
   "source": [
    "bot.polling()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "unlikely-poultry",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "extraordinary-drunk",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "marine-worship",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "competent-celebrity",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "designing-giant",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "collective-sensitivity",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "breathing-progressive",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "verified-perspective",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "korean-accountability",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "defensive-kingston",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "outstanding-baptist",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "romance-madness",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "excellent-capability",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "changing-branch",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "black-prevention",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "weekly-advertising",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "authorized-diving",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "uniform-farmer",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cathedral-scene",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "removable-amsterdam",
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
