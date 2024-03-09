from messages.send_message import bot
import base64
import time

if __name__ == "__main__" :
    with open('./tigrinho.jpg','rb') as f:
        encoded_img = base64.b64encode(f.read())
    while True : 
        bot(encoded_img)
        time.sleep(36)
    
   