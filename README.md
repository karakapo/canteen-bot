Hacettepe Üniversitesi Yemek Listesi Telegram Botu

Bu proje, Hacettepe Üniversitesi'nin yemek listesini otomatik olarak belirli bir Telegram kanalına gönderen bir Telegram botudur.
İçindekiler

    Açıklama
    Gereksinimler
    Yapılandırma

Açıklama

Bu bot, Hacettepe Üniversitesi'nin SKSDB web sitesinden günlük yemek listesini çeker ve belirlenen saatte Telegram kanalına gönderir.
Gereksinimler

    Python 3.6 veya üzeri
    Aşağıdaki Python kütüphaneleri:
        telebot
        schedule
        requests
        beautifulsoup4
        re
        datetime

Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

bash

Copy Code
pip install pyTelegramBotAPI schedule requests beautifulsoup4  

Yapılandırma

Botun düzgün çalışması için aşağıdaki değişkenleri doğru bir şekilde yapılandırmanız gerekmektedir:

    TOKEN: Telegram Bot API token'ınız. BotFather üzerinden yeni bir bot oluşturarak bu token'ı edinebilirsiniz.
    CHAT_ID: Mesajların gönderileceği Telegram kanalının veya grubunun ID'si. Kanal ID'sini öğrenmek için @getmyid_bot gibi bir bot kullanabilirsiniz.

Bu değişkenleri bot.py dosyasında ilgili yerlere girin:

python

Copy Code
TOKEN = 'BOT TOKEN'  
CHAT_ID = 'YOUR CHAT ID'
