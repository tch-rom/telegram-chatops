import telebot
import requests
import os

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
API_KEY = os.environ.get("API_KEY")

REPO = "tch-rom/telegram-chatops"

payload = {"event_type": "CD triggered via Telegram"}
headers = {'Accept': 'application/vnd.github.everest-preview+json', 'Authorization': f'token {GITHUB_TOKEN}'}

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['deploy'])

def deploy(message):
    bot.send_message(message.chat.id, "Hey! Your deployment must start now.. Please check the link: https://github.com/tch-rom/telegram-chatops/actions")
    requests.post(f"https://api.github.com/repos/{REPO}/dispatches", json=payload, headers=headers)

bot.polling()