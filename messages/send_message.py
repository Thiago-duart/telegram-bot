import os
import telebot
from dotenv import load_dotenv
from messages.message_generator import generator
import base64

load_dotenv()

def bot(img):
        token = os.getenv("BOT_TOKEN")
        bot_telegram = telebot.TeleBot(token)
        group_id =  os.getenv("GROUP_ID")
        
        message_test = generator() 
        
        img_decoded = base64.b64decode(img)
        
        bot_telegram.send_photo(chat_id = group_id, photo = img_decoded,caption= message_test)
        @bot_telegram.message_handler(chat_types=['group'])
        def send_message (message):
            if message.chat.type == "group":
                raise Exception("smurfBlack bahia")
            
       
