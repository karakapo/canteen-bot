import telebot
import schedule
import time
from threading import Thread
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime


now = datetime.now()
formatted_date = now.strftime('%d.%m.%Y')


TOKEN = 'BOT TOKEN'
CHAT_ID = 'YOUR CHAT ID'

bot = telebot.TeleBot(TOKEN)



url = 'https://sksdb.hacettepe.edu.tr/new/grid.php?parameters=qbapuL6kmaScnHaup8DEm1B8maqturW8haidnI%2Bsq8F%2FgY1fiZWdnKShq8bTlaOZXq%2BmwWjLzJyPlpmcpbm1kNORopmYXI22tLzHXKmVnZykwafFhImVnZWipbq0f8qRnJ%2BioF6go7%2FOoplWqKSltLa805yVj5agnsGmkNORopmYXam2qbi%2Bo5mqlXRt'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')


yemeklist_div = soup.find('div', class_='col-lg-9 col-12 mb-3')

text = yemeklist_div.get_text()



date_pattern =r'\d{2}\.\d{2}\.\d{4}'

dates = re.findall(date_pattern, text)

yemeklist = []
last_index = 0

for date in dates:
    start_index = text.find(date, last_index)
    if last_index != 0:
        yemeklist.append(text[last_index:start_index].strip())
    yemeklist.append(date)
    last_index = start_index + len(date)

if last_index < len(text):
    yemeklist.append(text[last_index:].strip())


for date in yemeklist:
    if date == formatted_date:
        index = yemeklist.index(date)





def send_auto_message():
    bot.send_message(CHAT_ID, yemeklist[index+1])


def schedule_messages():
    schedule.every().day.at("07:00").do(send_auto_message)
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_bot():
    bot.polling()

if __name__ == "__main__":
    scheduler_thread = Thread(target=schedule_messages)
    scheduler_thread.start()

    start_bot()
